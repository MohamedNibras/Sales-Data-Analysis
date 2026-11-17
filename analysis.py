import os
import pandas as pd
import matplotlib.pyplot as plt

# Run this script from the project root folder:
# python python/analysis.py

DATA_PATH = "dataset/sales_data.csv"
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

DATA_PATH = "../dataset/sales_data.csv"

df = pd.read_csv(DATA_PATH, parse_dates=["Order_Date"])

print("\n========== SALES DATA PREVIEW ==========")
print(df.head())
print("\n========== DATASET INFORMATION ==========")
print(df.info())
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Basic data cleaning
df = df.drop_duplicates(subset=["Order_ID"])
df = df.dropna(subset=["Order_ID", "Order_Date", "Product", "Sales", "Profit"])
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
df = df.dropna(subset=["Quantity", "Sales", "Profit"])
df = df[df["Quantity"] > 0]

# Add useful analysis columns
df["Order_Month"] = df["Order_Date"].dt.to_period("M").astype(str)
df["Profit_Margin"] = (df["Profit"] / df["Sales"].replace(0, pd.NA) * 100).round(2)

# Overall KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
total_units = df["Quantity"].sum()
avg_order_value = total_sales / total_orders if total_orders else 0

print("\n========== BUSINESS KPIs ==========")
print(f"Total Revenue: Rs. {total_sales:,.2f}")
print(f"Total Profit: Rs. {total_profit:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Units Sold: {total_units}")
print(f"Average Order Value: Rs. {avg_order_value:,.2f}")

# Business summaries
category_summary = df.groupby("Category", as_index=False).agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Units_Sold=("Quantity", "sum")
).sort_values("Total_Sales", ascending=False)

region_summary = df.groupby("Region", as_index=False).agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Orders=("Order_ID", "nunique")
).sort_values("Total_Sales", ascending=False)

monthly_summary = df.groupby("Order_Month", as_index=False).agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).sort_values("Order_Month")

product_summary = df.groupby("Product", as_index=False).agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Units_Sold=("Quantity", "sum")
).sort_values("Total_Sales", ascending=False)

# Save output files
df.to_csv(f"{OUTPUT_DIR}/cleaned_sales.csv", index=False)
category_summary.to_csv(f"{OUTPUT_DIR}/sales_by_category.csv", index=False)
region_summary.to_csv(f"{OUTPUT_DIR}/sales_by_region.csv", index=False)
monthly_summary.to_csv(f"{OUTPUT_DIR}/monthly_sales_summary.csv", index=False)
product_summary.to_csv(f"{OUTPUT_DIR}/sales_by_product.csv", index=False)

# Chart 1: sales by category
plt.figure(figsize=(8, 5))
plt.bar(category_summary["Category"], category_summary["Total_Sales"])
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales (INR)")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/sales_by_category.png", dpi=150)
plt.close()

# Chart 2: monthly sales trend
plt.figure(figsize=(10, 5))
plt.plot(monthly_summary["Order_Month"], monthly_summary["Total_Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/monthly_sales_trend.png", dpi=150)
plt.close()

# Chart 3: profit by region
plt.figure(figsize=(8, 5))
plt.bar(region_summary["Region"], region_summary["Total_Profit"])
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit (INR)")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/profit_by_region.png", dpi=150)
plt.close()

print("\n========== TOP PRODUCTS BY SALES ==========")
print(product_summary.head(5).to_string(index=False))
print("\nAnalysis completed. Check the output folder for CSV reports and charts.")
