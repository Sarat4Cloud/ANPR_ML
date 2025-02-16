import sqlite3

conn = sqlite3.connect("anpr.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM anpr_records;")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='anpr_records';")

conn.commit()
conn.close()