import pandas as pd
import streamlit as st
from sklearn.impute import SimpleImputer
from scipy import stats
import re

def clean_data(df, handle_missing, remove_duplicates, remove_outliers, standardize_columns, remove_special_chars, remove_invalid_entries, trim_whitespace):
    """
    Cleans the given DataFrame based on user selections.
    Logs the changes made to the dataset.
    """
    log = []
    
    if remove_duplicates:
        initial_rows = df.shape[0]
        df = df.drop_duplicates()
        log.append(f"Removed {initial_rows - df.shape[0]} duplicate rows.")
    
    if handle_missing:
        missing_values_before = df.isnull().sum().sum()
        imputer = SimpleImputer(strategy='most_frequent')
        df[df.columns] = imputer.fit_transform(df)
        missing_values_after = df.isnull().sum().sum()
        log.append(f"Filled {missing_values_before - missing_values_after} missing values.")
    
    if remove_outliers:
        numeric_cols = df.select_dtypes(include=['number']).columns
        initial_rows = df.shape[0]
        df = df[(stats.zscore(df[numeric_cols]) < 3).all(axis=1)]
        log.append(f"Removed {initial_rows - df.shape[0]} outlier rows.")
    
    if standardize_columns:
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
        log.append("Standardized column names.")
    
    if remove_special_chars:
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].apply(lambda x: re.sub(r'[^a-zA-Z0-9 ]', '', str(x)) if pd.notnull(x) else x)
        log.append("Removed special characters from text columns.")
    
    if remove_invalid_entries:
        if 'age' in df.columns:
            initial_rows = df.shape[0]
            df = df[df['age'] >= 0]  # Remove negative ages
            log.append(f"Removed {initial_rows - df.shape[0]} rows with invalid age values.")
    
    if trim_whitespace:
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].str.strip()
        log.append("Trimmed whitespace from text columns.")
    
    return df, log

st.title("Automated Data Cleaning Tool")

uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])

if uploaded_file:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith("csv") else pd.read_excel(uploaded_file)
    
    st.write("### Preview of Uploaded Data")
    st.write(df.head())
    
    handle_missing = st.checkbox("Handle Missing Values")
    remove_duplicates = st.checkbox("Remove Duplicates")
    remove_outliers = st.checkbox("Remove Outliers")
    standardize_columns = st.checkbox("Standardize Column Names")
    remove_special_chars = st.checkbox("Remove Special Characters from Text Columns")
    remove_invalid_entries = st.checkbox("Remove Invalid Data Entries")
    trim_whitespace = st.checkbox("Trim Whitespace from Text Columns")
    
    if st.button("Clean Data"):
        cleaned_df, cleaning_log = clean_data(df, handle_missing, remove_duplicates, remove_outliers, standardize_columns, remove_special_chars, remove_invalid_entries, trim_whitespace)
        st.write("### Cleaned Data Preview")
        st.write(cleaned_df.head())
        
        if cleaning_log:
            st.write("### Cleaning Log")
            for entry in cleaning_log:
                st.write(f"- {entry}")
        
        # Provide download option
        cleaned_df.to_csv("cleaned_data.csv", index=False)
        st.download_button("Download Cleaned Data", "cleaned_data.csv")
