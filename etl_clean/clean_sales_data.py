import pandas as pd
from config import RAW_DATA_PATH
import os


# load the raw data
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", RAW_DATA_PATH))
df = pd.read_csv(file_path, sep=';', encoding='utf-8', engine="python")

# Drop bad columns
df = df.drop(columns=[col for col in df.columns if 'Unnamed' in col or col.strip() == ""])

# Rename columns to clean names
df.columns = ["employee", "total_sales", "sale_date", "region", "notes"]

# remove white space and standardize casing
df["employee"] = df["employee"].str.strip().str.title()
df["region"] = df["region"].str.strip().str.title()
df["notes"] = df["notes"].fillna("").str.strip()

# Clean currency
def clean_currency(value):
    value = str(value).replace("$", "").replace('"', "").replace(",", "").replace(" ", "")
    try:
        return float(value)
    except:
        return None
df["total_sales"] = df["total_sales"].apply(clean_currency)

df["sale_date"] = pd.to_datetime(df["sale_date"], errors="coerce")

#  Drop rows with invalid data
df = df.dropna(subset=["employee", "total_sales", "sale_date", "region"])

print("Cleaned Data Preview:\n")
print(df.head())
print(f"Cleaned DataFrame Shape: {df.shape}")

df.to_csv("cleaned_sales_data.csv", index=False, encoding="utf-8")
print("Saved Clean CSV")
