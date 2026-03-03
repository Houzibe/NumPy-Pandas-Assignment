import numpy as np
import pandas as pd

print("\n"+"*"*50)
print("ASSIGNMENT 3: NUMPY OPERATIONS ")
print("*"*50)

#--------------------------------------------------------------------------------------------
# Question 1: Revenue Simulation
#--------------------------------------------------------------------------------------------

print("\nQUESTION 1: Revenue Simulation")
print(""+"-"*50)
np.random.seed(42)

#product parameters
products = {
    "A" : {"mean": 50, "std": 10},
    "B" : {"mean": 30, "std": 5},
    "C" : {"mean": 70, "std": 15},
    "D" : {"mean": 40, "std": 8}
}

#Generate daily sales for 30 days
daily_sales = np.zeros((30,4))

for i, (products, params) in enumerate(products.items()):
    sales = np.random.normal(params["mean"], params["std"],30)
    sales = np.maximum(0, sales)
    daily_sales[:, i] = np.round(sales)

#print the shape
print(f"- Shape of daily_sales array:", daily_sales.shape)
print("\n")
print("First 5 days of sales:")
print("-"*50)
#Create DataFrame for display
days = [f"Day {i+1}" for i in range(5)]
products_list = ["Product A", "Product B", "Product C", "Product D"]
df_first5 = pd.DataFrame(
    daily_sales[:5],
    index=days,
    columns=products_list
) 
print(df_first5.to_string())

#show some basic statistics
print("\n")
print("Summary Statistics (30 days):")
print("-"*50)

df_all = pd.DataFrame(
    daily_sales,
    columns=products_list
)

print("- Mean daily sales:")
print(df_all.mean().round(1))
print("\n- Standard deviation:")
print(df_all.std().round(1))
print("\n- Minimum sales (any zero days?):")
print(df_all.min())
print("\n- Maximum sales:")
print(df_all.max())

#Check if any days had zero sales
zero_days = (daily_sales == 0).any(axis=1)
if zero_days.any():
    print(f"\nDays with zero sales for some products: {np.where(zero_days)[0] + 1}")

print("\n")
#--------------------------------------------------------------------------------------------
# Question 3: Price & Revenue Calculation
#--------------------------------------------------------------------------------------------
#Created data
prices = np.array([200, 350, 150, 280]) #Price of tomato, rice, pepper, onion
quantities = np.array([10, 3, 15, 12]) #Daily quantities for each product

print()
print("="*50)
print("ASSIGNMENT 3 [NUMPY]: PRICE & REVENUE CALCULATOR")
print("="*50)

# 1- Calculate daily revenue (price × quantity for each product)
daily_revenue_per_product = prices*quantities
daily_total_revenue = np.sum(daily_revenue_per_product)

print(f"\n1. DAILY REVENUE:")
print("\n   Products: Tomato, Rice, Pepper, Onion.")
print(f"   Prices: {prices} NGN")
print(f"   Quantities sold daily: {quantities} units")
print(f"   Daily revenue per product: {daily_revenue_per_product} NGN")
print(f"\n   Total Daily Revenue: {daily_total_revenue:,.2f} NGN")

#2. Calculate total revenue over 30 days
days = 30
total_revenue_over_30_days = daily_total_revenue * days

print(f"\n2. TOTAL REVENUE OVER 30 DAYS:")
print(f"   The total revenue over 30 days is {daily_total_revenue} NGN * {days} days = {total_revenue_over_30_days:,.2f} NGN")

#3. Apply a promotional discount:
# Create a copy of the daily revenue for each day
# Shape: (30, 4) - 30 days, 4 products
daily_revenue_matrix = np.tile(daily_revenue_per_product, (days, 1))

# Create discount matrices
discount_matrix = np.zeros((days, 4))

# Days 1-5: 15% off all products
discount_matrix[0:5, :] = 0.15  # 15% discount

# Days 15-20: 10% off Product A and Product B only
discount_matrix[14:20, [0, 1]] = 0.10  # 10% discount

print(f"\n3. PROMOTIONAL DISCOUNT:")
print(f"   Days 1-5: 15% off ALL products")
print(f"   Days 15-20: 10% off Product A and B only")
print(f"   Other days: No discount")

#Calculate revenue with discounts
revenue_with_discounts = daily_revenue_matrix * (1-discount_matrix)

#Calculate revenue over 30 days with discounts
total_revenue_with_discounts = np.sum(revenue_with_discounts)

print(f"\n4. TOTAL REVENUE OVER 30 DAYS (WITH DISCOUNTS):")
print(f"   The total revenue with discount is {total_revenue_with_discounts:,.2f} NGN")

#5. How much discount did you give away?
total_discount_given = total_revenue_over_30_days - total_revenue_with_discounts
discount_percentage = (total_discount_given / total_revenue_over_30_days) * 100

print(f"\n5. DISCOUNT ANALYSIS:")
print(f"   Total discount given away: {total_discount_given:,.2f} NGN")
print(f"   Discount as percentage of revenue: {discount_percentage:.2f}%")
print()