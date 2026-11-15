import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

csv_path = BASE_DIR / "Dataset" / "cleaned_retail_sales.csv"
db_path = BASE_DIR / "Dataset" / "retail_sales.db"

df = pd.read_csv(csv_path)

print("CSV Dataset Loaded Successfully!")
print("Number of Records:", len(df))

connection = sqlite3.connect(db_path)

df.to_sql(
    name="retail_sales",
    con=connection,
    if_exists="replace",
    index=False
)

print("\nData inserted into SQLite successfully!")

query = "SELECT * FROM retail_sales LIMIT 5"

result = pd.read_sql_query(query, connection)

print("\n========== FIRST 5 RECORDS ==========")
print(result)

count_query = "SELECT COUNT(*) AS total_records FROM retail_sales"

count_result = pd.read_sql_query(count_query, connection)

print("\nTotal Records in SQL Database:")
print(count_result)

connection.close()

print("\n========== DATABASE CREATION COMPLETED ==========")
print("Database Location:", db_path)