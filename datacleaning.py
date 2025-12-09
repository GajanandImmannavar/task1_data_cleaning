import pandas as pd
df = pd.read_csv("netflix_titles.csv")
df.head()

df.info()
df.describe(include="all")
df.isnull().sum()

# Filling missing values with 'Unknown'
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['date_added'] = df['date_added'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Unknown')
df['duration'] = df['duration'].fillna('Unknown')

# Confirm no missing values remain
df.isnull().sum()



duplicates_before = df.duplicated().sum()

print("Duplicates before removing them ->>",duplicates_before)

df = df.drop_duplicates()

duplicates_after = df.duplicated().sum()

print("Duplicates after removing them ->> ", duplicates_after)

rows_columns =  df.shape
print("No of rows and No columns Respectively", rows_columns)


for col in df.select_dtypes(include="object"):
    df[col] =df[col].str.lower().str.strip()

df.head()

# Fix incorrect spellings
df['country'] = df['country'].replace('unknow', 'unknown')
df['cast'] = df['cast'].replace('unknow', 'unknown')
df['director'] = df['director'].replace('unknow', 'unknown')

# Optional: replace spaces with underscores in type column
df['type'] = df['type'].str.replace(" ", "_")

df.head()


df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')


df['date_added'].head()


df[['duration_int', 'duration_type']] = df['duration'].str.extract(r'(\d+)\s*(\w+)')

df['duration_int'] = pd.to_numeric(df['duration_int'], errors='coerce')

df[['duration', 'duration_int', 'duration_type']].head()

df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('[^a-zA-Z0-9_]', '', regex=True)

df.columns


print("Shape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nSample Rows:\n", df.head())

# Fix remaining missing dates
df['date_added'] = df['date_added'].fillna('Unknown')

# Fix duration missing values
df['duration_int'] = df['duration_int'].fillna(0)
df['duration_type'] = df['duration_type'].fillna('unknown')

# Confirm everything is fixed
df.isnull().sum()


df.to_csv("netflix_titles_cleaned.csv", index=False)

import os
os.listdir()

os.getcwd()

