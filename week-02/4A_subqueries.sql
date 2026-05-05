USE northwind;

-- 1. What is the product name(s) of the most expensive products?
SELECT productname
FROM products 
WHERE unitprice = (
SELECT MAX(unitprice)
FROM products);

-- 2. What is the product name(s) and categories of the least expensive products?
SELECT p.productname, c.categoryname
FROM products p
JOIN categories c ON p.categoryid = c.categoryid
WHERE p.unitprice = (
SELECT MIN(unitprice)
FROM products
);

-- 3. What is the order id, shipping name and shipping address of all orders shipped via "Federal Shipping"?
SELECT orderid, shipname, shipaddress
FROM orders
WHERE shipvia = (
SELECT shipperid
FROM shippers
WHERE companyname = 'Federal Shipping'
);

-- 4. What are the order ids of the orders that included "Sasquatch Ale"?
SELECT DISTINCT orderid
FROM `order details`
WHERE productid = (
SELECT productid 
FROM products
WHERE productname = 'Sasquatch Ale' 
);

-- 5. What is the name of the employee that sold order 10266?
SELECT firstname, lastname
FROM employees 
WHERE employeeid = (
SELECT employeeid
FROM orders
WHERE orderid = 10266
);

-- 6. What is the name of the customer that bought order 10266?
SELECT companyname 
FROM customers
WHERE customerid = (
SELECT customerid
FROM orders
WHERE orderid = 10266
);