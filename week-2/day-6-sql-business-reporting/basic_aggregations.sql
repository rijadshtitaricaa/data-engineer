-- Count all orders
SELECT COUNT(*) AS total_orders
FROM orders;

-- Count only completed orders
SELECT COUNT(*) AS completed_orders 
FROM orders where status = 'completed';

-- Count only pending orders
SELECT COUNT(*) AS pending_orders 
FROM orders where status = 'pending';

-- Count only cancelled orders
SELECT COUNT(*) AS cancelled_orders 
FROM orders where status = 'cancelled';

-- Calculate total quantity orderd across all statuses.
SELECT SUM(quantity)  as total_quantity_orderd 
from orders;

-- Calculate total quantity ordered only from completed orders.
SELECT SUM(quantity) as total_quantity_orderd
from orders 
WHERE status = 'completed';

-- Find the average product price.
SELECT AVG(price) 
from products;

-- Find the cheapest product price.
SELECT MIN(price) as cheapest_product
FROM products;

-- Find the most expensive product price.
SELECT max(price) as most_expensive_product
FROM products;

-- Calculate completed revenue using quantity * price. This requires connecting orders with products.
SELECT SUM(orders.quantity * products.price) AS completed_revenue
FROM orders
JOIN products on orders.product_id = products.product_id
WHERE orders.status = 'completed';

-- Calculate non-completed potential value from pending and cancelled orders. Explain why this should not be counted as real revenue.   
SELECT SUM(orders.quantity * products.price) AS completed_revenue
FROM orders
JOIN products ON orders.product_id = products.product_id
WHERE orders.status = 'completed';