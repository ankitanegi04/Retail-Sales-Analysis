import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

file_path = BASE_DIR / "Dataset" / "cleaned_retail_sales.csv"

df = pd.read_csv(file_path)

df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

visualization_dir = BASE_DIR / "Visualizations"
visualization_dir.mkdir(parents=True, exist_ok=True)

print("Dataset Loaded Successfully!")

category_sales = df.groupby("Category")["Sales"].sum()
category_sales = category_sales.sort_values(ascending=False)

plt.figure(figsize=(9, 5))
category_sales.plot(kind="bar")

plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(visualization_dir / "sales_by_category.png")
plt.show()
plt.close()

region_profit = df.groupby("Region")["Profit"].sum()
region_profit = region_profit.sort_values(ascending=False)

plt.figure(figsize=(9, 5))
region_profit.plot(kind="bar")

plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(visualization_dir / "profit_by_region.png")
plt.show()
plt.close()

segment_sales = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(7, 7))

plt.pie(
    segment_sales,
    labels=segment_sales.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales Distribution by Customer Segment")
plt.tight_layout()

plt.savefig(visualization_dir / "sales_by_segment.png")
plt.show()
plt.close()

product_profit = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(11, 6))
product_profit.sort_values().plot(kind="barh")

plt.title("Top 10 Most Profitable Products")
plt.xlabel("Total Profit")
plt.ylabel("Product Name")
plt.tight_layout()

plt.savefig(visualization_dir / "top_10_profitable_products.png")
plt.show()
plt.close()

df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(12, 5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.savefig(visualization_dir / "monthly_sales_trend.png")
plt.show()
plt.close()

plt.figure(figsize=(9, 5))

plt.scatter(df["Sales"], df["Profit"], alpha=0.5)

plt.title("Relationship Between Sales and Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True)
plt.tight_layout()

plt.savefig(visualization_dir / "sales_vs_profit.png")
plt.show()
plt.close()

print("\n========== VISUALIZATION COMPLETED ==========")
print("All graphs have been generated successfully!")
print("Saved Location:", visualization_dir)