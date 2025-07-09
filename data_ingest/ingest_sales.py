import pandas as pd
from config import RAW_DATA_PATH

# Load the data
df = pd.read_csv(RAW_DATA_PATH, sep=';', encoding='utf-8', engine='python')

# view the first 5 rows
print("First 5 rows of the dataframe:")
print(df.head())

# Display shape and column names
print(f"\nTotal number of rows: {df.shape[0]}\nTotal columns: {df.shape[1]}")
print("\ncolumn names:")
for col in df.columns:
    print(f"- {repr(col)}")
