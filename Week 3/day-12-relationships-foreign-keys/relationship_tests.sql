-- Foreign Key Test 1
INSERT INTO orders (customer_id, order_date, status, channel)
VALUES (999, '2026-07-10', 'completed', 'Online');

-- Foreign Key Test 2
INSERT INTO order_items (order_id, product_id, quantity)
VALUES (999, 1, 1);

-- Foreign Key Test 3
INSERT INTO order_items (order_id, product_id, quantity)
VALUES (1, 999, 1);

-- CHECK Test 1
INSERT INTO products (product_name, category, price)
VALUES ('Tablet', 'Electronics', 0);

-- CHECK Test 2
INSERT INTO order_items (order_id, product_id, quantity)
VALUES (1, 1, 0);

-- Status CHECK Test
INSERT INTO orders (customer_id, order_date, status, channel)
VALUES (1, '2026-07-10', 'done', 'Online');