import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

file_path = BASE_DIR / "Dataset" / "Sample - Superstore.csv"

df = pd.read_csv(file_path, encoding="cp1252")

print("\n========== ORIGINAL DATASET ==========")
print("Original Dataset Shape:", df.shape)
print(df.head())

df.columns = df.columns.str.strip()

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

print("\n========== MISSING VALUES ==========")
missing_values = df.isnull().sum()
print(missing_values)
print("Total Missing Values:", df.isnull().sum().sum())

print("\n========== DUPLICATE RECORDS ==========")
duplicate_count = df.duplicated().sum()
print("Duplicate Rows:", duplicate_count)

df = df.drop_duplicates()

print("Shape After Removing Duplicates:", df.shape)

print("\n========== DATE CONVERSION ==========")

for col in ["Order Date", "Ship Date"]:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")
        print(col, "converted to:", df[col].dtype)

print("\n========== NUMERICAL DATA CONVERSION ==========")

numeric_columns = ["Sales", "Profit", "Quantity", "Discount"]

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        print(col, "converted to:", df[col].dtype)

print("\n========== FINAL DATASET INFORMATION ==========")

df.info()

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicates After Cleaning:")
print(df.duplicated().sum())

print("\nFinal Dataset Shape:", df.shape)

output_path = BASE_DIR / "Dataset" / "cleaned_retail_sales.csv"

df.to_csv(output_path, index=False)

print("\n========== PROJECT STATUS ==========")
print("Cleaned Dataset Saved Successfully!")
print("File Location:", output_path)