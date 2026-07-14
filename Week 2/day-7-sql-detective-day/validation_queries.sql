-- V1: Check the total number of orders in the orders table.
SELECT COUNT(*) AS total_orders FROM orders;


-- V2: Check how many orders have been completed.
SELECT COUNT(*) AS completed_orders FROM orders
WHERE status = 'completed';


-- V3: Check how many orders are still pending.
SELECT COUNT(*) AS pending_orders FROM orders
WHERE status = 'pending';


-- V4: Check how many orders have been cancelled.
SELECT COUNT(*) AS cancelled_orders FROM orders
WHERE status = 'cancelled';


-- V5: Check the total number of customers.
SELECT COUNT(*) AS total_customers
FROM customers;


-- V6: Check the total number of products.
SELECT COUNT(*) AS total_products
FROM products;


-- V7: Calculate total revenue from completed orders only.
-- Pending and cancelled orders are excluded.
SELECT SUM(o.quantity * p.price) AS completed_revenue FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.status = 'completed';


-- V8: Calculate completed revenue grouped by product name.
-- Shows which products generated the most revenue.
SELECT  p.product_name, SUM(o.quantity * p.price) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.status = 'completed'
GROUP BY p.product_name;

-- V9: Calculate completed revenue by product category.
-- Shows which categories generate the most revenue from completed orders.
SELECT p.category, SUM(o.quantity * p.price) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.status = 'completed'
GROUP BY p.category;


-- V10: Count orders by customer city.
-- Shows order activity based on customer location.
SELECT c.city, COUNT(*) AS order_count
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.city;


-- V11: Find customers who placed more than one order.
-- Helps identify repeat customers.
SELECT c.customer_id,c.customer_name,COUNT(o.order_id) AS order_count
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(o.order_id) > 1;


-- V12: Find the top 3 completed orders by total amount.
-- Shows the highest value completed transactions.
SELECT  o.order_id,c.customer_name,p.product_name,(o.quantity * p.price) AS total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
WHERE o.status = 'completed'
ORDER BY total_amount DESC
LIMIT 3;


-- V13: Find orders that should not count as real revenue.
-- Shows pending and cancelled orders that should be excluded.
SELECT * FROM orders
WHERE status IN ('pending', 'cancelled');


-- V14: Find the category with the highest completed revenue.
-- Identifies the best-performing product category.
SELECT  p.category, SUM(o.quantity * p.price) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.status = 'completed'
GROUP BY p.category
ORDER BY revenue DESC
LIMIT 1;


-- V15: Find the city with the highest order activity.
-- Identifies the city generating the most orders.
SELECT  c.city, COUNT(o.order_id) AS order_count
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.city
ORDER BY order_count DESC
LIMIT 1; 