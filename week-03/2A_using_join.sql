USE northwind;

-- 1
SELECT
p.ProductID,
p.ProductName, 
p.UnitPrice,
c.CategoryName 
FROM Products p
JOIN Categories c
ON p.CategoryID = c.CategoryID
ORDER BY c.CategoryName, p.ProductName;

-- 2 
SELECT 
p.ProductID,
p.ProductName,
p.UnitPrice,
s.CompanyName AS SupplierName
FROM Products p 
JOIN Suppliers s
ON p.supplierID = s.SupplierID
WHERE p.UnitPrice > 75
ORDER BY p.ProductName; 

-- 3
SELECT 
p.ProductID,
p.ProductName,
p.UnitPrice,
c.CategoryName,
s.CompanyName AS SupplierName
FROM Products p
JOIN Categories c
ON p.CategoryID = c.CategoryID
JOIN Suppliers s 
ON p.SupplierID = s.SupplierID
ORDER BY p.ProductName; 

-- 4
SELECT o.OrderID,
o.ShipName,
o.ShipAddress,
sh.CompanyName AS Shipper
FROM Orders o 
JOIN Shippers sh
ON o.ShipVia = sh.ShipperID
WHERE o.ShipCountry = 'Germany'
ORDER BY sh.CompanyName, o.ShipName;

-- 5
SELECT 
o.ShipName,
COUNT(*) AS OrderCount
FROM Orders o
JOIN Shippers sh
ON o.ShipVia = sh.ShipperID
WHERE o.ShipCountry = 'Germany' 
GROUP BY o.ShipName
ORDER BY o.ShipName; 

-- 6
SELECT
o.OrderID,
o.OrderDate,
o.ShipName,
o.ShipAddress
FROM Orders o
JOIN `Order Details` od
ON o.OrderID = od.OrderID
JOIN Products p
ON od.ProductID = p.ProductID
WHERE p.ProductName = 'Sasquatch Ale';
















