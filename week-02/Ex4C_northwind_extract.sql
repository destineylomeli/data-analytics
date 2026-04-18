-- The table that holds the irems Northwind sells is the products table
-- The table that holds the categories of items is the Categories table.

SELECT * FROM northwind.employees;
-- The employee whos name looks like a bird is Nancy Davolio. 

SELECT * FROM northwind.products;
-- This query returns all records from the Products table.
-- To limit rows using the toolbar, change "Limit to 1000 rows" to 10.

SELECT * FROM northwind.categories;
-- The category ID of seafood is 8.

SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM orders
LIMIT 50;
