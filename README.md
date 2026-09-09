# Employee Data Cleaning and Exploratory Data Analysis

## Project Overview
This project focuses on cleaning and analyzing an employee dataset using Python. The dataset was first cleaned by removing duplicate records and checking for missing values. Then, Exploratory Data Analysis (EDA) was performed to identify trends, patterns, and insights using statistical analysis and data visualization.

## Dataset
- **File:** `Employee.csv`
- **Source:** Public employee dataset from Kaggle

## Tools Used
- Python 3
- Pandas
- Matplotlib
- Seaborn
- VS Code

---

## Task 1: Data Cleaning and Preparation

### Cleaning Steps Performed
- Loaded the dataset using Pandas.
- Checked for missing values.
- Checked for duplicate records.
- Removed duplicate records.
- Verified the data types of all columns.
- Saved the cleaned dataset as `Employee_Cleaned.csv`.

### Results
- Original Records: **4653**
- Duplicate Records Removed: **1889**
- Cleaned Records: **2764**
- Missing Values Found: **0**

---

## Task 2: Exploratory Data Analysis (EDA)

### Analysis Performed
- Displayed the first five rows of the dataset.
- Checked the dataset shape.
- Displayed column names.
- Examined data types and dataset information.
- Generated summary statistics.
- Analyzed:
  - Education Distribution
  - City Distribution
  - Gender Distribution
  - Payment Tier Distribution
  - Employee Leave Distribution
- Created bar charts to visualize the data.

### Key Insights
- Most employees hold a Bachelor's degree.
- Bangalore has the highest number of employees.
- Male employees slightly outnumber female employees.
- Payment Tier 3 contains the highest number of employees.
- More employees stayed with the company than left.

---

## Project Files

- `Employee.csv` – Original dataset
- `Employee_Cleaned.csv` – Cleaned dataset
- `task1.py` – Data Cleaning and Preparation
- `task2.py` – Exploratory Data Analysis
- `README.md` – Project documentation

---

## How to Run

### Task 1

```bash
python task1.py
```

### Task 2

```bash
python task2.py
```

---

## Project Outcome

This project demonstrates the complete data analysis workflow, starting from data cleaning and preparation to exploratory data analysis using Python. It showcases skills in data preprocessing, statistical analysis, and visualization.