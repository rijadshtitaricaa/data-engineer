drop table if EXISTS oders;

create table orders(
order_id INTEGER PRIMARY KEY AUTOINCREMENT,
customer_name TEXT NOT NULL,
city TEXT NOT NULL,
product TEXT NOT NULL,
category TEXT NOT NULL,
quantity INTEGER NOT NULL,
price REAL NOT NULL,
status TEXT NOT NULL,
order_date TEXT NOT NULL
);

INSERT INTO orders (customer_name, city, product, category, quantity, price, status, order_date) 
VALUES 
('Arta', 'Prishtina', 'Laptop', 'Electronics', 1, 700.00, 'completed', '2026-07-01'),
('Blend', 'Mitrovica', 'Mouse', 'Accessories', 2, 15.00, 'completed', '2026-07-01'),
('Era', 'Prizren', 'Desk Chair', 'Office', 1, 120.00, 'pending', '2026-07-02'),
('Genci', 'Vushtrri', 'Monitor', 'Electronics', 1, 250.00, 'cancelled', '2026-07-02'),
('Dona', 'Prishtina', 'Keyboard', 'Accessories', 1, 45.00, 'completed', '2026-07-03'),
('Valon', 'Mitrovica', 'Notebook', 'Office', 5, 3.50, 'completed', '2026-07-03'),
('Lira', 'Prizren', 'Smartphone', 'Electronics', 1, 600.00, 'pending', '2026-07-04'),
('Yll', 'Gjilan', 'USB Drive', 'Accessories', 3, 12.00, 'completed', '2026-07-04'),
('Hana', 'Prishtina', 'Pens Pack', 'Office', 10, 1.50, 'completed', '2026-07-05'),
('Arian', 'Mitrovica', 'Headphones', 'Electronics', 1, 85.00, 'cancelled', '2026-07-05'),
('Besa', 'Prizren', 'Charging Cable', 'Accessories', 2, 20.00, 'pending', '2026-07-06'),
('Ilir', 'Prishtina', 'Desk Lamp', 'Office', 1, 30.00, 'completed', '2026-07-06');


