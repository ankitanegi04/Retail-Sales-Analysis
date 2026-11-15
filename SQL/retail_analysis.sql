SELECT *
FROM retail_sales
LIMIT 10;

SELECT
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM retail_sales;

SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM retail_sales
GROUP BY Category
ORDER BY Total_Sales DESC;

SELECT
    Region,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM retail_sales
GROUP BY Region
ORDER BY Total_Profit DESC;

SELECT
    Segment,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM retail_sales
GROUP BY Segment
ORDER BY Total_Sales DESC;

SELECT
    "Product Name",
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM retail_sales
GROUP BY "Product Name"
ORDER BY Total_Profit DESC
LIMIT 10;

SELECT
    "Product Name",
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM retail_sales
GROUP BY "Product Name"
ORDER BY Total_Sales DESC
LIMIT 10;

SELECT
    "Product Name",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM retail_sales
GROUP BY "Product Name"
HAVING SUM(Profit) < 0
ORDER BY Total_Profit ASC
LIMIT 10;

SELECT
    strftime('%Y', "Order Date") AS Year,
    strftime('%m', "Order Date") AS Month,
    ROUND(SUM(Sales), 2) AS Monthly_Sales
FROM retail_sales
GROUP BY Year, Month
ORDER BY Year, Month;

SELECT
    "Customer ID",
    "Customer Name",
    COUNT(DISTINCT "Order ID") AS Total_Orders,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM retail_sales
GROUP BY "Customer ID", "Customer Name"
ORDER BY Total_Sales DESC
LIMIT 10;