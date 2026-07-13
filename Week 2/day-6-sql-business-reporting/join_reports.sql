SELECT orders.order_id, customers.customer_name, customers.city, orders.order_date, orders.status
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id;



SELECT orders.order_id,  products.product_name,  products.category,  orders.quantity,  products.price,  (orders.quantity * products.price) AS total_amount, 
 orders.status
FROM  orders
JOIN products ON orders.product_id = products.product_id;




SELECT customers.customer_name, customers.city, products.product_name, products.category, orders.quantity, products.price, (orders.quantity * products.price)
AS total_amount, 
orders.status, orders.order_dateFROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id;



SELECT products.product_name,  SUM(orders.quantity * products.price) AS completed_revenue
FROM  orders
JOIN products ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY products.product_name
ORDER BY completed_revenue DESC;


SELECT products.category, SUM(orders.quantity * products.price) AS completed_revenue
FROM orders
JOIN products ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY products.category
ORDER BY completed_revenue DESC;

SELECT 
    customers.city, 
    COUNT(orders.order_id) AS order_count
FROM 
    orders
JOIN 
    customers ON orders.customer_id = customers.customer_id
GROUP BY 
    customers.city
ORDER BY 
    order_count DESC;