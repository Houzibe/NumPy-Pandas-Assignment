import numpy as np 
#import pandas as pd 

#Load datasets
#nigerian_market_prices = pd.read_csv('./datasets/nigerian_market_prices_assignment.csv')
#nigerian_market_prices = pd.read_csv('./datasets/nigerian_market_transaction_assignment.csv')

#--------------------------------------------------------------------------------------------
# Question 3: Price & Revenue Calculation
#--------------------------------------------------------------------------------------------
#Created data
prices = np.array([200, 350, 150, 280]) #Price of tomato, rice, pepper, onion
quantities = np.array([10, 3, 15, 12]) #Daily quantities for each product

print("="*50)
print("PRICE & REVENUE CALCULATOR")
print("="*50)

# 1- Calculate daily revenue (price × quantity for each product)
daily_revenue_per_product = prices*quantities
daily_total_revenue = np.sum(daily_revenue_per_product)

print(f"\n1. DAILY REVENUE:")
print("\nProducts: Tomato, Rice, Pepper, Onion.")
print(f"Prices: {prices} NGN")
print(f"Quantities sold daily: {quantities} units")
print(f"Daily revenue per product: {daily_revenue_per_product} NGN")
print(f"\nTotal Daily Revenue: {daily_total_revenue} NGN")

