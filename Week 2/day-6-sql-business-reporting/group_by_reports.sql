-- Count orders by status.
SELECT status,COUNT(order_id) AS order_count
FROM orders
GROUP BY status;

-- Count orders by order_date.
SELECT order_date,COUNT(order_id) AS total_orders
FROM orders
GROUP BY order_date;

-- Count orders by customer_id.
SELECT customer_id,COUNT(order_id) AS total_customers
FROM orders
GROUP BY customer_id;

-- Count orders by product_id
SELECT product_id,COUNT(order_id) AS total_products
FROM orders
GROUP BY product_id;

-- Calculate total quantity by product_id for completed orders only.
SELECT product_id, SUM(quantity) AS total_quantity
FROM orders
WHERE status = 'completed'
GROUP BY product_id
ORDER BY total_quantity DESC;

-- Calculate completed revenue by product_id.
SELECT orders.product_id,products.product_name,SUM(orders.quantity * products.price) AS completed_revenue
FROM  orders
JOIN products ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY orders.product_id,products.product_name
ORDER BY completed_revenue DESC;

-- Calculate completed revenue by status and explain why the result is not always a good business report.
SELECT orders.status,SUM(orders.quantity * products.price) AS total_revenue
FROM orders
JOIN  products ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY orders.status;

-- Use HAVING to show only customer_id values with more than one order.
SELECT customer_id,COUNT(order_id) AS order_count 
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 1
ORDER BY order_count DESC;

-- Use HAVING to show only product_id values where completed quantity is greater than 2.x`
SELECT  product_id, SUM(quantity) AS total_completed_quantity
FROM orders
WHERE status = 'completed'
GROUP BY  product_id
HAVING SUM(quantity) > 2
ORDER BY total_completed_quantity DESC;

-- Sort every grouped report from highest to lowest where it makes sense.
SELECT product_id,SUM(quantity) AS total_quantity
FROM  orders
WHERE status = 'completed'
GROUP BY product_id
ORDER BY total_quantity DESC;