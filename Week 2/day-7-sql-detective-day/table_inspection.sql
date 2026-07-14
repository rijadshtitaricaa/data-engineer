-- Check all order records in the orders table.
SELECT * FROM orders;

-- Check all customer records in the customers table.
SELECT * FROM customers;

-- Check all products records in the products table.
SELECT * FROM products;

-- Check how many order records exist in the orders table.
SELECT COUNT(*) as total_orders
from orders;

-- Check how many customer records exist in the customers table.
SELECT COUNT(*) as total_customers
from customers;

-- Check how many product records exist in the products table.
SELECT COUNT(*) as total_products
from products;