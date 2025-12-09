📌 Task 1 — Data Cleaning & Preprocessing
Data Analyst Internship Project
Dataset: Netflix Movies & TV Shows (Kaggle)
✅ Objective

The objective of this task is to clean a raw dataset by handling:

Missing values

Duplicate records

Inconsistent formatting

Incorrect data types

Non-standard column names

This prepares the dataset for analysis and modeling.

📁 Dataset Used

Raw Dataset: netflix_titles.csv

Source: Kaggle (Netflix Movies and TV Shows dataset)

Rows: 8807

Columns: 12

🧹 Data Cleaning Steps Performed
🔹 1. Importing Dataset
import pandas as pd
df = pd.read_csv("netflix_titles.csv")
df.head()

🔹 2. Checking Data Information

Used:

df.info()
df.describe(include="all")
df.isnull().sum()


Found many null values in:

director

cast

country

date_added

rating

duration

🔹 3. Handling Missing Values

Replaced missing values with "Unknown":

df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['date_added'] = df['date_added'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Unknown')
df['duration'] = df['duration'].fillna('Unknown')


After handling missing values:

df.isnull().sum()

🔹 4. Removing Duplicate Rows
duplicates_before = df.duplicated().sum()
df = df.drop_duplicates()
duplicates_after = df.duplicated().sum()

🔹 5. Standardizing Text Columns

Converted all text to lowercase and removed extra spaces:

for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.lower().str.strip()


Fixed incorrect spellings:

df['country'] = df['country'].replace('unknow', 'unknown')
df['cast'] = df['cast'].replace('unknow', 'unknown')
df['director'] = df['director'].replace('unknow', 'unknown')


Standardized type column:

df['type'] = df['type'].str.replace(" ", "_")

🔹 6. Converting date_added to Datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['date_added'].head()

🔹 7. Cleaning the duration Column

Extracted numeric and text parts:

df[['duration_int', 'duration_type']] = df['duration'].str.extract(r'(\d+)\s*(\w+)')

df['duration_int'] = pd.to_numeric(df['duration_int'], errors='coerce')

🔹 8. Renaming Columns

Made column names clean and standardized:

df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('[^a-zA-Z0-9_]', '', regex=True)

🔹 9. Final Dataset Verification
print("Shape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nSample Rows:\n", df.head())


Handled final missing values:

df['date_added'] = df['date_added'].fillna('Unknown')
df['duration_int'] = df['duration_int'].fillna(0)
df['duration_type'] = df['duration_type'].fillna('unknown')

🔹 10. Saving Cleaned Dataset
df.to_csv("netflix_titles_cleaned.csv", index=False)

📂 Project Folder Structure
Task1/
 ├── Raw_Data/
 │     └── netflix_titles.csv
 ├── netflix_titles_cleaned.csv
 ├── datacleaning.py
 └── README.md

🎉 Task Completed Successfully

This cleaned dataset is now ready for:

Analysis

Visualization

Machine learning

Reporting

🧠 Skills Learned

Data cleaning with Pandas

Handling missing & inconsistent values

Cleaning text data

Converting date formats

Splitting columns

Renaming columns

Preparing datasets for analysis

🙌 Prepared by:

Gajanand Immannavar
Data Analyst — Internship Project