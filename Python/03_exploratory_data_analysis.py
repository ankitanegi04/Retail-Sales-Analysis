import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

file_path = BASE_DIR / "Dataset" / "cleaned_retail_sales.csv"

df = pd.read_csv(file_path)

print("\n========== DATASET LOADED ==========")
print("Dataset Loaded Successfully!")
print("Dataset Shape:", df.shape)

print("\nFirst 5 Records:")
print(df.head())

print("\n========== SALES BY CATEGORY ==========")

category_sales = df.groupby("Category")["Sales"].sum()

category_sales = category_sales.sort_values(ascending=False)

print(category_sales)

print("\n========== PROFIT BY REGION ==========")

region_profit = df.groupby("Region")["Profit"].sum()

region_profit = region_profit.sort_values(ascending=False)

print(region_profit)

print("\n========== SALES BY CUSTOMER SEGMENT ==========")

segment_sales = df.groupby("Segment")["Sales"].sum()

segment_sales = segment_sales.sort_values(ascending=False)

print(segment_sales)

print("\n========== TOP 10 PROFITABLE PRODUCTS ==========")

product_profit = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print(product_profit.head(10))

print("\n========== TOP 10 PRODUCTS BY SALES ==========")

product_sales = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(product_sales.head(10))

print("\n========== OVERALL BUSINESS SUMMARY ==========")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)

print("\n========== EDA COMPLETED ==========")