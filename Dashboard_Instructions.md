# Power BI Dashboard Instructions

## 1. Import data
1. Open Power BI Desktop.
2. Select Home > Get Data > Text/CSV.
3. Select `dataset/sales_data.csv`.
4. Select Transform Data.
5. Confirm Order_Date is Date; Quantity is Whole Number; Sales, Cost, Profit and Unit_Price are Decimal Number.
6. Select Close & Apply.

## 2. Create measures
Select Modeling > New measure and create each measure:

Total Revenue = SUM(sales_data[Sales])

Total Profit = SUM(sales_data[Profit])

Total Orders = DISTINCTCOUNT(sales_data[Order_ID])

Units Sold = SUM(sales_data[Quantity])

Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)

Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)

Format Profit Margin % as Percentage.

## 3. Add visuals
- Card: Total Revenue
- Card: Total Profit
- Card: Total Orders
- Card: Units Sold
- Line chart: Order_Date on X-axis; Total Revenue on Y-axis
- Clustered bar chart: Category on Y-axis; Total Revenue on X-axis
- Bar chart: Region on Y-axis; Total Profit on X-axis
- Bar chart: Product on Y-axis; Total Revenue on X-axis
- Donut chart: Payment_Mode as Legend; Total Orders as Values
- Slicers: Order_Date, Region, Category

## 4. Format
- Set page title to Sales Performance Dashboard.
- Format revenue and profit as Indian Rupees (₹).
- Sort product chart by Total Revenue descending.
- Turn on data labels where useful.
- Use a consistent, readable theme.

## 5. Expected dashboard
A single-page interactive report showing revenue, profit, orders, units sold, monthly trend, category performance, regional profit and payment preferences.

Note: Save your Power BI report as `powerbi/Sales_Analysis_Dashboard.pbix`.
