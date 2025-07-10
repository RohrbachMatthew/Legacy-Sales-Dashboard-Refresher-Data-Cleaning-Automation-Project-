import mysql.connector
from config import DB_CONFIG, CLEAN_TABLE_NAME

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

cursor.execute(f"select count(*) from {CLEAN_TABLE_NAME}")
row_count = cursor.fetchone()[0]
print(f"Total rows in `{CLEAN_TABLE_NAME}`: {row_count}")

cursor.close()
conn.close()
