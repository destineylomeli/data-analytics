USE northwind;

-- 1. List product id, product name, and unit price
SELECT productID, productName, unitPrice
FROM products;

-- 2. Products where unit price is $7.50 or less
SELECT productName, unitPrice
FROM products
WHERE unitPrice <= 7.50;

-- 3. Products with no units in stock but on backorder
SELECT productName, unitsInStock, unitsOnOrder
FROM products
WHERE unitsInStock = 0 
AND unitsOnOrder > 0;

-- Look at category ID in products table
SELECT productName, categoryID
FROM products;

-- List all categories 
SELECT *
FROM categories;

-- ALL seafood products
SELECT p.productName
FROM products p
JOIN categories c
ON p.categoryID = c.categoryID
WHERE c.categoryName = 'Seafood';

-- Find Tokyo Traders supplier ID
SELECT supplierID, companyName
FROM suppliers
WHERE companyName = 'Tokyo Traders';

-- Products from Tokyo Traders
SELECT productName, supplierID
FROM products
WHERE supplierID = (
SELECT supplierID
FROM suppliers
WHERE companyName = 'Tokyo Traders'
);

-- Count employees 
SELECT COUNT(*) AS totalEmployees
FROM employees;

-- Employees with manager in title 
SELECT firstName, lastName, title
FROM employees
WHERE title LIKE '%manager%'; 
