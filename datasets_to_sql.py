import pandas as pd
import sqlite3

# Load CSVs
ads = pd.read_csv("datasets/Ad_Sales.csv")
eligibility = pd.read_csv("datasets/Eligibility.csv")
sales = pd.read_csv("datasets/Total_sales.csv")

# Create SQLite DB
conn = sqlite3.connect("ecommerce.db")

# Write to SQL tables
ads.to_sql("AdSales", conn, if_exists="replace", index=False)
eligibility.to_sql("Eligibility", conn, if_exists="replace", index=False)
sales.to_sql("TotalSales", conn, if_exists="replace", index=False)

conn.close()

print("ecommerce.db created with 3 tables!")
