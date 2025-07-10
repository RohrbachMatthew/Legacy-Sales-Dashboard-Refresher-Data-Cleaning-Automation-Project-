import mysql.connector
from config import DB_CONFIG

try:
    conn = mysql.connector.connect(**DB_CONFIG)
    print("Successfully connected to MySQL")
    conn.close()
except mysql.connector.Error as err:
    print("Connection failed:", err)