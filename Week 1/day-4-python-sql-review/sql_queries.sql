-- TASK 1 

-- SHOW ALL ORDERS
SELECT * FROM orders 

--SHOW ONLY COSTUMER NAME AND ORDERS
SELECT customer_name, product from orders

--Show order_id,costumer_name,city,status
SELECT order_id, customer_name, city,status FROM orders

--Show prodouct,category,quantity,price
SELECT product,category,quantity,price from orders;


-- TASK 2 

-- Show only orders that are completed
SELECT * FROM orders WHERE status = 'completed';

--Show only orders that are pending
SELECT * FROM orders WHERE status = 'pending';

-- Show only orders that are cancelled
SELECT * FROM orders WHERE status = 'cancelled';

-- Show only order where price is greater than 100
SELECT * from orders WHERE price > 100;

-- Show only orders where city is Vushtrri
SELECT * FROM orders WHERE city = 'Vushtrri';

-- Show only orders where category is Accsesories
SELECT * FROM orders WHERE category = 'Accessories'


-- TASK 3 --

-- Show completed orders where price is greater than 100.
SELECT * FROM orders WHERE status = 'completed' and price > 100

-- Show completed orders from Prishtina.
SELECT * FROM orders WHERE status = 'completed' and city = 'Prishtina'

-- Show orders where status is pending OR cancelled.
SELECT * FROM orders WHERE status = 'completed' or status = 'cancelled'

-- Show Accessories orders where price is less than 50.

SELECT * FROM orders WHERE category = 'Accessories' and price < 50


-- TASK 4 --

-- show orders by cheap to expensive
SELECT * FROM orders ORDER BY price desc;

-- Show orders by most expensive to cheapest
SELECT * FROM orders ORDER BY price asc;

-- SELECT * FROM orders ORDER BY price asc;
SELECT * FROM orders ORDER BY price DESC LIMIT 3;

-- Show top 3 orders by total_amount.

SELECT order_id, customer_name, price FROM orders ORDER BY price DESC LIMIT 3;

-- Show customer_name, product, quantity, price, and total_amount.
SELECT  customer_name,  product,  quantity,  price,  (quantity * price) AS total_amountFROM orders;


-- Show only completed orders with total_amount.
SELECT 
    customer_name, 
    product, 
    quantity, 
    price, 
    (quantity * price) AS total_amount
FROM orders
WHERE status = 'completed';

--how completed orders with total_amount sorted from highest to lowest.
SELECT 
    customer_name, 
    product, 
    quantity, 
    price, 
    (quantity * price) AS total_amount
FROM orders
WHERE status = 'completed'
ORDER BY total_amount DESC;




-- PART 4 ---

SELECT customer_name, product, price  FROM orders  ORDER BY price DESC  LIMIT 1;

SELECT customer_name, product, (quantity * price) AS total_amount  FROM orders  ORDER BY (quantity * price) DESC  LIMIT 1;

SELECT customer_name, product, status, (quantity * price) AS total_amount  FROM orders WHERE status = 'pending' OR status = 'cancelled';

SELECT SUM(quantity * price) AS completed_revenue 
FROM orders 
WHERE status = 'completed';