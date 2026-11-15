
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent

file_path = BASE_DIR / "Dataset" / "Sample - Superstore.csv"

df = pd.read_csv(file_path, encoding='cp1252')

print("\n----- FIRST 5 ROWS -----")
print(df.head())


print("\n----- DATASET SHAPE -----")
print(df.shape)


print("\n----- COLUMN NAMES -----")
print(df.columns)


print("\n----- DATASET INFORMATION -----")
df.info()


print("\n----- STATISTICAL SUMMARY -----")
print(df.describe())


print("\n----- CATEGORICAL SUMMARY -----")
print(df.describe(include='object'))


print("\n----- UNIQUE VALUES -----")
print(df.nunique())


print("\n----- MISSING VALUES -----")
print(df.isnull().sum())


print("\n----- DUPLICATE RECORDS -----")
print(df.duplicated().sum())


print("\n----- DATA TYPES -----")
print(df.dtypes)


print("\n----- PRODUCT CATEGORIES -----")
print(df['Category'].unique())

print("\n----- REGIONS -----")
print(df['Region'].unique())


print("\n----- LAST 5 ROWS -----")
print(df.tail())
