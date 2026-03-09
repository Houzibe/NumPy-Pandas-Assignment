#------------------------------------------------------
#               Pandas Data Analysis
#------------------------------------------------------

import pandas as pd
import numpy as np

#-------------------------------------------------------
#Question 4: Load and Explore Your Dataset
#-------------------------------------------------------

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

#-------------------------------------------------------
#Question 5: Data Filtering & Selection
#-------------------------------------------------------

print("=" * 60)
print(" QUESTION 5: DATA FILTERING AND SELECTION")
print("=" * 60)

# 1. Select 3 columns of interest and display first 10 rows
print("1. SELECTED COLUMNS (First 10 rows)")
print("-" * 60)

selected_columns = ['market_name', 'product', 'price']
df_selected = df[selected_columns]
print(f"Selected columns: {selected_columns}")
print(f"Shape: {df_selected.shape}")
print(df_selected.head(10))

# 2. Filter data based on a numeric condition (Fare > $100)
print("\n2. NUMERIC FILTER: Price > 100 Naira")
print("-" * 60)
df["price"] = df['price'].str.replace('₦', '').str.replace(',', '')

numeric_filter = df[df["price"].notna()]
print(f"Condition: Price > 100 Naira")
print(f"Number of products with price > 100 Naira: {len(numeric_filter)}")
print(f"Shape: {numeric_filter.shape}")
print("\nFirst 5 rows of filtered data:")
print(numeric_filter[['market_name', 'product', 'price']].head())

# 3. Filter data based on a categorical condition (Embarked from 'C' - Cherbourg)
print("\n3. Filter data based on a categorical condition")
print("-" * 60)

categorical_filter = df[df['state'] == 'Enugu']
print(f"Condition: state == 'Enugu'")
print(f"Number of filter data from Enugu: {len(categorical_filter)}")
print(f"Shape: {categorical_filter.shape}")
print("\nFirst 5 rows of filtered data:")
print(categorical_filter[['market_name', 'state', 'product']].head())

# 4. Combine two conditions using AND (&)
print("\n4. Combine two conditions using AND (&)")
print("-" * 60)

and_filter = df[(df['state'] == 'Enugu') & (df['product'] == "Gari")]
print(f"Conditions: State == 'Enugu' AND Product == 'Gari'")
print(f"Number of product: {len(and_filter)}")
print(f"Shape: {and_filter.shape}")
print("\nFirst 5 rows of filtered data:")
print(and_filter[['market_name', 'state', 'product']].head())

print("\n5. Combine two conditions using OR (|)")
print("-" * 60)

or_filter = df[(df['state'] == 'Oyo') | (df['product'] == "Yam")]
print(f"Conditions: state == 'Oyo' OR product == 'Yam'")
print(f"Number of  items: {len(or_filter)}")
print(f"Shape: {or_filter.shape}")
print("\nFirst 5 rows of filtered data:")
print(or_filter[['market_name', 'state', 'product']].head())

print()
