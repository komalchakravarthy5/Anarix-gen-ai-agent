import sqlite3

db_path = "ecommerce.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# List tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("🧾 Tables:", tables)

# Inspect columns of AdSales
cursor.execute("PRAGMA table_info(AdSales);")
columns = cursor.fetchall()
print("📊 AdSales columns:")
for col in columns:
    print(col)

conn.close()
