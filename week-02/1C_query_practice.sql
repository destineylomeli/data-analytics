USE northwind; 

-- 1. List the product id, product name, and unite price of every product, in ascending order by price
SELECT productID, productName, unitPrice
FROM products
ORDER BY unitPrice ASC;

-- 2. Products with at least 100 units on hand, ordered by price descending
SELECT productID, productName, unitPrice, unitsInStock
FROM products
WHERE unitsInStock >= 100
ORDER BY unitPrice DESC;

-- 3. If prices tie, order those by product name descending
SELECT productID, productName, unitPrice, unitsInStock
FROM products
WHERE unitsInStock >= 100
ORDER BY unitPrice DESC, productName ASC;

-- 4. Total number of distinc customers who have placed orders
SELECT COUNT(DISTINCT customerID) AS CustomerCount
FROM orders; 

-- 5. Distinct customers who placed shipped orders, by ship country
SELECT shipCountry, COUNT(DISTINCT customerID) AS CustomerCount
FROM orders
WHERE shippedDate IS NOT NULL
GROUP BY shipCountry
ORDER BY CustomerCount DESC;

-- 6. Products with less than 25 units in stock, but 1 or more on order
SELECT productName, unitsInStock, unitsOnOrder
FROM products
WHERE unitsInStock < 25
AND unitsOnOrder >= 1
ORDER BY unitsOnOrder DESC, productName ASC;

-- 7. Each job title and how many employees have it
SELECT title, COUNT(*) AS EmployeeCount
FROM employees
GROUP BY title
ORDER BY EmployeeCount DESC;

-- 8. Employees with monthly salary between $2000 and $2500, ordered by job title
SELECT firstName, lastName, title, salary
FROM employees
WHERE salary BETWEEN 2000 AND 2500
ORDER BY title ASC;