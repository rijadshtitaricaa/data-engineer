-- Show all customers
SELECT * FROM customers;

-- Show all products
SELECT * FROM products;

-- Show all orders
SELECT * FROM orders;

-- Show all order_items
SELECT * FROM order_items;

-- Show only completed orders
SELECT * FROM orders WHERE status = 'completed';

--Show only pending or cancelled orders
SELECT * FROM orders WHERE status = 'cancelled' OR status = 'pending';

-- Show each order with customer_name, city, order_date, status, and channel.
SELECT o.order_id, c.customer_name, c.city, o.order_date, o.status, o.channel
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id;


-- Show each order_item with product_name, category, price, and quantity.
SELECT oi.order_item_id,p.product_name,p.category,p.price,oi.quantity
FROM order_items oi
INNER JOIN products p 
ON oi.product_id = p.product_id;

-- 17. Show order_id, customer_name, product_name, quantity, price, and total_amount

SELECT 
    o.order_id,
    c.customer_name,
    p.product_name,
    oi.quantity,
    p.price,
    (oi.quantity * p.price) AS total_amount
FROM orders o
INNER JOIN customers c 
    ON o.customer_id = c.customer_id
INNER JOIN order_items oi 
    ON o.order_id = oi.order_id
INNER JOIN products p 
    ON oi.product_id = p.product_id;


-- 18. Show only completed orders with their customer and product details

SELECT 
    o.order_id,
    c.customer_name,
    p.product_name,
    oi.quantity,
    p.price,
    (oi.quantity * p.price) AS total_amount
FROM orders o
INNER JOIN customers c 
    ON o.customer_id = c.customer_id
INNER JOIN order_items oi 
    ON o.order_id = oi.order_id
INNER JOIN products p 
    ON oi.product_id = p.product_id
WHERE o.status = 'completed';


-- Level 3 - Multi-table JOINs


-- 19. Join customers + orders + order_items + products in one query

SELECT 
    c.customer_name,
    o.order_id,
    p.product_name,
    oi.quantity,
    p.price
FROM customers c
INNER JOIN orders o 
    ON c.customer_id = o.customer_id
INNER JOIN order_items oi 
    ON o.order_id = oi.order_id
INNER JOIN products p 
    ON oi.product_id = p.product_id;


-- 20. Show customer_name, city, order_id, product_name, category, quantity, price, total_amount

SELECT 
    c.customer_name,
    c.city,
    o.order_id,
    p.product_name,
    p.category,
    oi.quantity,
    p.price,
    (oi.quantity * p.price) AS total_amount
FROM customers c
INNER JOIN orders o 
    ON c.customer_id = o.customer_id
INNER JOIN order_items oi 
    ON o.order_id = oi.order_id
INNER JOIN products p 
    ON oi.product_id = p.product_id;


-- 21. Sort the result by order_id and then by product_name

SELECT c.customer_name,c.city,o.order_id,p.product_name,p.category,oi.quantity,p.price,(oi.quantity * p.price) AS total_amount
FROM customers c
INNER JOIN orders o 
    ON c.customer_id = o.customer_id
INNER JOIN order_items oi 
    ON o.order_id = oi.order_id
INNER JOIN products p 
    ON oi.product_id = p.product_id
ORDER BY 
    o.order_id,
    p.product_name;


-- 22. Filter the joined result to show only completed orders

SELECT c.customer_name,c.city,o.order_id,p.product_name,p.category,oi.quantity,p.price,(oi.quantity * p.price) AS total_amount
FROM customers c
INNER JOIN orders o 
    ON c.customer_id = o.customer_id
INNER JOIN order_items oi 
    ON o.order_id = oi.order_id
INNER JOIN products p 
    ON oi.product_id = p.product_id
WHERE o.status = 'completed';


-- 23. Calculate completed revenue by city

SELECT 
    c.city,
    SUM(oi.quantity * p.price) AS completed_revenue
FROM customers c
INNER JOIN orders o 
    ON c.customer_id = o.customer_id
INNER JOIN order_items oi 
    ON o.order_id = oi.order_id
INNER JOIN products p 
    ON oi.product_id = p.product_id
WHERE o.status = 'completed'
GROUP BY c.city;


-- 24. Calculate completed revenue by product category

SELECT 
    p.category,
    SUM(oi.quantity * p.price) AS completed_revenue
FROM orders o
INNER JOIN order_items oi 
    ON o.order_id = oi.order_id
INNER JOIN products p 
    ON oi.product_id = p.product_id
WHERE o.status = 'completed'
GROUP BY p.category;


-- 25. Show top 5 customers by completed revenue

SELECT 
    c.customer_name,
    SUM(oi.quantity * p.price) AS completed_revenue
FROM customers c
INNER JOIN orders o 
    ON c.customer_id = o.customer_id
INNER JOIN order_items oi 
    ON o.order_id = oi.order_id
INNER JOIN products p 
    ON oi.product_id = p.product_id
WHERE o.status = 'completed'
GROUP BY c.customer_name
ORDER BY completed_revenue DESC
LIMIT 5;


-- 26. Show top 5 products by completed revenue

SELECT 
    p.product_name,
    SUM(oi.quantity * p.price) AS completed_revenue
FROM products p
INNER JOIN order_items oi 
    ON p.product_id = oi.product_id
INNER JOIN orders o 
    ON oi.order_id = o.order_id
WHERE o.status = 'completed'
GROUP BY p.product_name
ORDER BY completed_revenue DESC
LIMIT 5;


-- 27. Count how many orders each customer has

SELECT 
    c.customer_name,
    COUNT(o.order_id) AS order_count
FROM customers c
LEFT JOIN orders o 
    ON c.customer_id = o.customer_id
GROUP BY c.customer_name;


-- 28. Count how many items each order has

SELECT 
    o.order_id,
    COUNT(oi.order_item_id) AS item_count
FROM orders o
LEFT JOIN order_items oi 
    ON o.order_id = oi.order_id
GROUP BY o.order_id;


-- 29. Find customers who have more than one order

SELECT 
    c.customer_name,
    COUNT(o.order_id) AS order_count
FROM customers c
INNER JOIN orders o 
    ON c.customer_id = o.customer_id
GROUP BY c.customer_name
HAVING COUNT(o.order_id) > 1;


-- 30. Find products that were sold more than once

SELECT 
    p.product_name,
    COUNT(oi.order_item_id) AS times_sold
FROM products p
INNER JOIN order_items oi 
    ON p.product_id = oi.product_id
GROUP BY p.product_name
HAVING COUNT(oi.order_item_id) > 1;


-- 31. Show all customers and their orders. Include customers even if they have no orders.

SELECT 
    c.customer_name,
    o.order_id,
    o.status
FROM customers c
LEFT JOIN orders o 
    ON c.customer_id = o.customer_id;


-- 32. Show all products and how many times each product appears in order_items.
-- Include products that were never sold.

SELECT 
    p.product_name,
    COUNT(oi.order_item_id) AS times_sold
FROM products p
LEFT JOIN order_items oi 
    ON p.product_id = oi.product_id
GROUP BY p.product_name;


-- 33. INNER JOIN vs LEFT JOIN explanation:
-- INNER JOIN returns only records where both tables have a matching value.
-- LEFT JOIN returns all records from the left table and matching records from the right table.
-- If there is no match, LEFT JOIN shows NULL values.