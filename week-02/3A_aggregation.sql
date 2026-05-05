USE northwind;

-- 1a
SELECT MIN(UnitPrice) AS CheapestPrice
FROM Products;

-- 1b
SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = (
SELECT MIN(UnitPrice)
FROM Products 
);

-- 2 
SELECT AVG(UnitPrice) AS AveragePrice
FROM Products; 

SELECT ROUND(AVG(UnitPrice), 2) AS AveragePrice
FROM Products; 

-- 3a
SELECT MAX(UnitPrice) AS MostExpensivePrice
FROM Products;

-- 3b
SELECT 
p.ProductName,
p.UnitPrice,
s.CompanyName AS SUpplierName
FROM Products p
JOIN Suppliers s 
ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice = (
SELECT MAX(UnitPrice)
FROM products
);

-- 4 
SELECT SUM(Salary) AS TotalMonthlyPayroll
FROM Employees;

-- 5 
SELECT 
MAX(Salary) AS HighestSalary,
MIN(Salary) AS LowestSalary
FROM Employees; 

-- 6 
SELECT 
s.SupplierID,
s.CompanyName AS SupplierName, 
COUNT(p.ProductID) AS NumberOfItems
FROM Suppliers s
JOIN Products p
ON s.SupplierID = p.SupplierID
GROUP BY s.SUpplierID, s.CompanyName;

-- 7
SELECT 
c.CategoryName,
ROUND(AVG(p.UnitPrice), 2) AS AveragePrice
FROM Categories c
Join Products p
ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName;

-- 8 
SELECT 
s.CompanyName AS SupplierName,
COUNT(p.ProductID) AS NumberOfItems
FROM Suppliers s
JOIN Products p 
ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName
HAVING COUNT(p.ProductID) >= 5;

-- 9
SELECT 
ProductID
ProductName,
UnitPrice * UnitsInStock AS InventoryValue
FROM Products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName; 


