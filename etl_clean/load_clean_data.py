import pandas as pd
import mysql.connector
from config import CLEAN_TABLE_NAME, DB_CONFIG

# Load clean CSV
df = pd.read_csv("cleaned_sales_data.csv")

# Connect to MySQL Database
conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

# Insert each row
for i, row in df.iterrows():
    cursor.execute(f"""
insert into {CLEAN_TABLE_NAME} (employee, total_sales, sale_date, region, notes)
values (%s, %s, %s, %s, %s)""", (
        #  Any NaN or NaT values are converted to None in Python
        # Python None becomes SQL NULL
        row["employee"] if pd.notnull(row["employee"]) else None,
        row["total_sales"] if pd.notnull(row["total_sales"]) else None,
        row["sale_date"] if pd.notnull(row["sale_date"]) else None,
        row["region"] if pd.notnull(row["region"]) else None,
        row["notes"] if pd.notnull(row["notes"]) else None,
    ))

conn.commit()
cursor.close()
conn.close()
print("All Rows Entered Into MySQL")