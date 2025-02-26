# Automated Data Cleaning Tool

##  Overview
The **Automated Data Cleaning Tool** is a web-based application designed to streamline the process of cleaning datasets. Built with **Streamlit**, it offers multiple data preprocessing options to enhance data quality and ensure cleaner datasets for analysis.

##  Features
-  Handle Missing Values (Fill with most frequent value)
-  Remove Duplicate Rows
-  Remove Outliers (Z-score method)
-  Standardize Column Names (Lowercase & Replace Spaces)
-  Remove Special Characters from Text Columns
-  Remove Invalid Data Entries (e.g., Negative Age)
-  Trim Whitespace from Text Columns
-  Generate a Cleaning Log for tracking changes

## ▶ Usage
You can access and use the tool directly via the following link:

🔗 **[Automated Data Cleaning Tool](https://automateddatacleaningtool.streamlit.app/)**

### Steps:
1. Upload a **CSV/XLSX** file.
2. Select the cleaning options via checkboxes.
3. Click **"Clean Data"** to process your dataset.
4. Download the cleaned file for further use.

##  Dependencies
- Python 3.7+
- `pandas`
- `streamlit`
- `scikit-learn`
- `scipy`

##  Future Enhancements
- Add more advanced data cleaning techniques.
- Provide detailed data summary reports.
- Support for additional file formats.

## 📩 Contribution
Contributions are welcome! Feel free to fork, contribute, and submit PRs to improve this tool.

---
© 2025 Shubneet | Open Source Initiative
