import sqlite3
import os

# Define the correct database path
DB_PATH = "D:/Project/instance/anpr.db"  # Use absolute path

# Connect to the SQLite database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Check if the table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='anpr_records';")
table_exists = cursor.fetchone()

if not table_exists:
    print("Error: Table 'anpr_records' does not exist in anpr.db")
else:
    # Fetch and print all records
    cursor.execute("SELECT * FROM anpr_records;")
    records = cursor.fetchall()

    if records:
        print("Database Records:")
        for record in records:
            print(record)
    else:
        print("No records found in 'anpr_records' table.")

# Close connection
conn.close()
