-- Query 1: Show all orders
SELECT *
FROM orders;

-- Query 2: Show only costumer names and products
SELECT costumer_name, products
FROM orders;

-- Query 3: Show only order_id, product, and status.
SELECT order_id, product,status
FROM orders;

-- Query 4: Show customer_name as customer and product as item using aliases.

SELECT cosutmer_name AS costumer, product AS item
FROM orders;

-- Query 5: Show product, quantity, and price only.
SELECT product,quantity,price 
FROM orders;

-- Query 6: Show order_id and customer_name only.
SELECT order_id,costumer_name
FROM orders;



-- LEVEL 2

-- Query 7:  Show only completed orders.
SELECT * FROM orders WHERE status = "completed";

-- Query 8:   Show only pending orders.
SELECT * FROM orders WHERE status = "pending";

-- Query 9: Show only cancelled orders.
SELECT * FROM orders WHERE status = "cancelled"

-- Query 10: Show orders where price is greater than 100.
SELECT * FROM orders WHERE price > 100;

-- Query 11: Show orders where price is less than 100.
SELECT * FROM orders WHERE price < 100;

-- Query 12: Show orders where price is greater than or equal to 180.
SELECT *
FROM orders
WHERE price >= 180;

-- Query 13: Show orders where status is not cancelled.
SELECT *
FROM orders
WHERE status != 'cancelled';

-- Query 14: Show orders where customer_name is Arta.
SELECT *
FROM orders
WHERE customer_name = 'Arta';

-- Query 15: Show orders where product is Mouse.
SELECT *
FROM orders
WHERE product = 'Mouse';

-- LEVEL 3

-- Query 16: Show completed orders where price is greater than 50.
SELECT *
FROM orders
WHERE status = 'completed'
AND price > 50;

-- Query 17: Show completed orders where product is Mouse.
SELECT *
FROM orders
WHERE status = 'completed'
AND product = 'Mouse';

-- Query 18: Show orders where status is pending OR status is cancelled.
SELECT *
FROM orders
WHERE status = 'pending'
OR status = 'cancelled';

-- Query 19: Show orders where customer_name is Dren AND status is completed.
SELECT *
FROM orders
WHERE customer_name = 'Dren'
AND status = 'completed';

-- Query 20: Show orders where product is Laptop AND price is 700.
SELECT *
FROM orders
WHERE product = 'Laptop'
AND price = 700;

-- Query 21: Show orders where status is completed OR price is greater than 500.
SELECT *
FROM orders
WHERE status = 'completed'
OR price > 500;

-- Query 22: Show orders where status is not cancelled AND price is greater than 100.
SELECT *
FROM orders
WHERE status != 'cancelled'
AND price > 100;

-- LEVEL 4

-- Query 23: Show all orders from cheapest to most expensive.
SELECT *
FROM orders
ORDER BY price ASC;

-- Query 24: Show all orders from most expensive to cheapest.
SELECT *
FROM orders
ORDER BY price DESC;

-- Query 25: Show the top 3 most expensive orders.
SELECT *
FROM orders
ORDER BY price DESC
LIMIT 3;

-- Query 26: Show the cheapest 2 orders.
SELECT *
FROM orders
ORDER BY price ASC
LIMIT 2;

-- Query 27: Show completed orders from highest price to lowest price.
SELECT *
FROM orders
WHERE status = 'completed'
ORDER BY price DESC;

-- Query 28: Show products sorted alphabetically by product name.
SELECT product
FROM orders
ORDER BY product ASC;

-- Query 29: Show customers sorted alphabetically by customer_name.
SELECT customer_name
FROM orders
ORDER BY customer_name ASC;

-- LEVEL 5

-- Query 30: Show customer_name, product, quantity, price, and total_amount.
SELECT customer_name, product, quantity, price,
quantity * price AS total_amount
FROM orders;

-- Query 31: Show only completed orders with total_amount.
SELECT customer_name, product, quantity, price,
quantity * price AS total_amount
FROM orders
WHERE status = 'completed';

-- Query 32: Show completed orders with total_amount sorted from highest to lowest.
SELECT customer_name, product, quantity, price,
quantity * price AS total_amount
FROM orders
WHERE status = 'completed'
ORDER BY total_amount DESC;

-- Query 33: Show cancelled or pending orders with total_amount.
SELECT customer_name, product, quantity, price,
quantity * price AS total_amount
FROM orders
WHERE status = 'cancelled'
OR status = 'pending';

-- Query 34: Show customer_name as customer, product as item, and quantity * price as total_amount.
SELECT customer_name AS customer,
product AS item,
quantity * price AS total_amount
FROM orders;

-- Query 35: Show the top 3 orders by total_amount.
SELECT customer_name, product,
quantity * price AS total_amount
FROM orders
ORDER BY total_amount DESC
LIMIT 3;

-- Query 36: Show only orders where total_amount is greater than 100.
SELECT customer_name, product,
quantity * price AS total_amount
FROM orders
WHERE quantity * price > 100;


-- Explanation: This query shows only completed orders.
-- It filters the table so we only see orders with the status "completed".

-- Explanation: This query shows orders where the price is greater than 100.
-- It helps us find higher-value orders.

-- Explanation: This query sorts all orders from the cheapest to the most expensive.
-- It uses ORDER BY price ASC to arrange the results.

-- Explanation: This query calculates the total amount of each order.
-- It multiplies quantity by price and displays the result as total_amount.

-- Explanation: This query shows the top 3 orders with the highest total amount.
-- It sorts the orders by total_amount in descending order and returns only the first three rows.