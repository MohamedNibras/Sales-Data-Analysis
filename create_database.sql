CREATE DATABASE sales_analysis;
USE sales_analysis;

DROP TABLE IF EXISTS sales;

CREATE TABLE sales (
    Order_ID VARCHAR(20) PRIMARY KEY,
    Order_Date DATE,
    Customer_Name VARCHAR(100),
    Product VARCHAR(100),
    Category VARCHAR(50),
    Region VARCHAR(30),
    City VARCHAR(50),
    Quantity INT,
    Unit_Price DECIMAL(12,2),
    Discount DECIMAL(5,2),
    Sales DECIMAL(14,2),
    Cost DECIMAL(14,2),
    Profit DECIMAL(14,2),
    Payment_Mode VARCHAR(40)
);

-- Import dataset/sales_data.csv into this table using MySQL Workbench:
-- Table Data Import Wizard > select CSV > map columns > import.
