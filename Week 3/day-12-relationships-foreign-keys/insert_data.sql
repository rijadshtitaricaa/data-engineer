-- Customers
INSERT INTO customers (customer_name, city, segment) VALUES
('Arta', 'Vushtrri', 'Business'),
('Blend', 'Prishtina', 'Student'),
('Dren', 'Mitrovica', 'Business'),
('Elira', 'Peja', 'Individual'),
('Leart', 'Ferizaj', 'Business'),
('Gresa', 'Gjakova', 'Student');

-- Products
INSERT INTO products (product_name, category, price) VALUES
('Laptop', 'Electronics', 950),
('Mouse', 'Accessories', 25),
('Monitor', 'Electronics', 220),
('Keyboard', 'Accessories', 60),
('Desk', 'Furniture', 180),
('Headphones', 'Accessories', 90);

-- Orders
INSERT INTO orders (customer_id, order_date, status, channel) VALUES
(1, '2026-07-01', 'completed', 'Online'),
(2, '2026-07-02', 'completed', 'Store'),
(3, '2026-07-03', 'pending', 'Online'),
(1, '2026-07-04', 'completed', 'Store'),
(4, '2026-07-05', 'cancelled', 'Online'),
(5, '2026-07-06', 'completed', 'Store'),
(6, '2026-07-07', 'completed', 'Online'),
(2, '2026-07-08', 'completed', 'Store');

-- Order Items
INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1, 1, 1),
(1, 2, 2),
(2, 3, 1),
(2, 4, 1),
(3, 2, 1),
(4, 1, 1),
(4, 6, 2),
(5, 5, 1),
(6, 3, 2),
(7, 4, 3),
(7, 2, 1),
(8, 6, 1);  