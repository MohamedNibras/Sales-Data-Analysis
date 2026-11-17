USE sales_analysis;

-- 1. Overall business KPIs
SELECT
    SUM(Sales) AS Total_Revenue,
    SUM(Profit) AS Total_Profit,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    SUM(Quantity) AS Units_Sold,
    ROUND(SUM(Sales) / COUNT(DISTINCT Order_ID), 2) AS Average_Order_Value
FROM sales;

-- 2. Sales and profit by category
SELECT Category, SUM(Sales) AS Total_Sales, SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Category
ORDER BY Total_Sales DESC;

-- 3. Sales by region
SELECT Region, SUM(Sales) AS Total_Sales, SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Region
ORDER BY Total_Sales DESC;

-- 4. Top 5 products by revenue
SELECT Product, SUM(Sales) AS Total_Sales, SUM(Quantity) AS Units_Sold
FROM sales
GROUP BY Product
ORDER BY Total_Sales DESC
LIMIT 5;

-- 5. Monthly sales trend
SELECT DATE_FORMAT(Order_Date, '%Y-%m') AS Sales_Month,
       SUM(Sales) AS Total_Sales,
       SUM(Profit) AS Total_Profit
FROM sales
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY Sales_Month;

-- 6. Payment mode analysis
SELECT Payment_Mode, COUNT(*) AS Orders, SUM(Sales) AS Revenue
FROM sales
GROUP BY Payment_Mode
ORDER BY Revenue DESC;

-- 7. Customers with highest purchase value
SELECT Customer_Name, COUNT(DISTINCT Order_ID) AS Orders,
       SUM(Sales) AS Customer_Revenue
FROM sales
GROUP BY Customer_Name
ORDER BY Customer_Revenue DESC
LIMIT 10;
