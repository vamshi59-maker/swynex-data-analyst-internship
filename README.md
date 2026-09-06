 # Employee Data Cleaning and Preparation

## Objective
This project cleans and prepares an employee dataset for analysis using Python and Pandas.

## Dataset
- File: `Employee.csv`
- Source: Public employee dataset from Kaggle

## Tools Used
- Python 3
- Pandas
- VS Code

## Cleaning Steps Performed
- Loaded the dataset using Pandas.
- Checked for missing values.
- Checked for duplicate records.
- Removed duplicate records.
- Verified the data types of all columns.
- Saved the cleaned dataset as `Employee_Cleaned.csv`.

## Results
- Original Records: 4653
- Duplicate Records Removed: 1889
- Cleaned Records: 2764
- Missing Values Found: 0

## Files
- `Employee.csv` - Original dataset
- `Employee_Cleaned.csv` - Cleaned dataset
- `cleaning.py` - Python script used for cleaning

## How to Run

```bash
python cleaning.py
```

The script reads `Employee.csv` and writes the cleaned data to `Employee_Cleaned.csv`.