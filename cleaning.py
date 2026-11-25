import pandas as pd

df = pd.read_csv("netflix_sample.csv")

print(df.head())
df.info()

print(df.isnull().sum())
df['director'].fillna("Unknown", inplace=True)
df['date_added'].fillna("Not Available", inplace=True)
print(df.isnull().sum())
df = df.drop_duplicates()
print("Rows before:", len(df))
df = df.drop_duplicates()
print("Rows after:", len(df))
df.columns = df.columns.str.lower().str.replace(" ", "_")
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df.to_csv("cleaned_netflix_data.csv", index=False)