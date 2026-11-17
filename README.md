# Sales Data Analysis Project

A beginner-friendly end-to-end sales analytics project using Python, SQL and Power BI.

## Dataset
`dataset/sales_data.csv` is a generated practice dataset containing 300 fictional order records. It is for learning and portfolio demonstration, not real company data.

Columns include:
- Order_ID, Order_Date, Customer_Name
- Product, Category, Region, City
- Quantity, Unit_Price, Discount
- Sales, Cost, Profit, Payment_Mode

## Requirements
- Python 3.10 or newer
- VS Code (or another Python editor)
- MySQL Server and MySQL Workbench (for SQL section)
- Power BI Desktop (for dashboard section)

## Run Python analysis
1. Extract the ZIP file.
2. Open the extracted `Sales_Data_Analysis` folder in VS Code.
3. Open Terminal > New Terminal.
4. Install libraries:
   `python -m pip install -r python/requirements.txt`
5. Run from the project root:
   `python python/analysis.py`
6. Open the `output` folder to see cleaned CSV files and PNG charts.

If `python` does not work on Windows, try `py` instead:
`py python/analysis.py`

## Run SQL section
1. Open MySQL Workbench and connect to your local MySQL server.
2. Open and run `sql/create_database.sql`.
3. In the Schemas panel, right-click `sales_analysis` > Table Data Import Wizard.
4. Select `dataset/sales_data.csv`.
5. Set destination table to `sales`.
6. Confirm column mappings and finish import.
7. Open and run `sql/analysis_queries.sql`.

## Build Power BI dashboard
Follow `powerbi/Dashboard_Instructions.md`. Import `dataset/sales_data.csv` directly into Power BI.

## Expected outputs
Python creates:
- output/cleaned_sales.csv
- output/sales_by_category.csv
- output/sales_by_region.csv
- output/monthly_sales_summary.csv
- output/sales_by_product.csv
- output/sales_by_category.png
- output/monthly_sales_trend.png
- output/profit_by_region.png

## Business questions
1. Which category generates the most revenue?
2. Which region generates the most profit?
3. Which products are top sellers?
4. How does revenue change month by month?
5. Which payment methods are most used?

## Portfolio note
Clearly label the dataset as synthetic/generated practice data. Do not describe it as actual company experience or real business results.
