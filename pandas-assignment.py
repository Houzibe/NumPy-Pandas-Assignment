#------------------------------------------------------
#                               Pandas Data Analysis
#------------------------------------------------------

import pandas as pd
import numpy as np

#Question 4: Load and Explore Your Dataset

#1. Load the dataset using Pandas
df = pd.read_csv('./datasets/nigerian_market_prices_assignment.csv')

#2. Display basic information:
print("-"*50)
print("DATASET BASIC INFORMATION")
print("-"*50)
print("Dataset: Nigeria Market Price")
print(f"\nNumber of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")
print(f"\nColumn names and data types:")
print(df.dtypes)

print(f"\nFirst 10 rows:")
print(df.head(10))

print("\nStatistical Summary")
print(df.describe())

print("\n Missing values")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])
print(f"\nTotal missing values: {df.isnull().sum().sum()}")
print(f"Percentage of missing data: {(df.isnull().sum().sum()/(df.shape[0]*df.shape[1]))*100: .2f}%")

#3. Write 2-3 sentences describing what this dataset contains
print("\nDataset Description:")
print("""This dataset is Nigerian market prices for some products. it contains the market name, 
state, products and their units of measurement, price of purchase of the product on a specific date
and the trader name""")



print()
