

SELECT c.city, SUM(o.quantity * p.price) AS completed_revenue
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
WHERE o.status = 'completed'
GROUP BY c.city
ORDER BY completed_revenue DESC;


SELECT p.category, 
       AVG(o.quantity * p.price) AS avg_order_value,
       COUNT(*) AS completed_orders_in_category
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.status = 'completed'
GROUP BY p.category
ORDER BY avg_order_value DESC;



SELECT p.product_name, 
       p.category,
       SUM(o.quantity * p.price) AS total_revenue,
       COUNT(*) AS order_count
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.status = 'completed'
GROUP BY p.product_id, p.product_name, p.category
HAVING SUM(o.quantity * p.price) > 100
ORDER BY total_revenue DESC;


SELECT c.city,
       SUM(CASE WHEN o.status = 'completed' THEN 1 ELSE 0 END) AS completed_count,
       SUM(CASE WHEN o.status = 'pending' THEN 1 ELSE 0 END) AS pending_count,
       SUM(CASE WHEN o.status = 'cancelled' THEN 1 ELSE 0 END) AS cancelled_count,
       COUNT(*) AS total_orders,
       ROUND(100.0 * SUM(CASE WHEN o.status = 'completed' THEN 1 ELSE 0 END) / COUNT(*), 1) AS completion_rate_pct
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.city
ORDER BY total_orders DESC;


-- FIXED VERSION (corrected):
SELECT p.product_name, SUM(o.quantity * p.price) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name;

-- EXPLANATION OF FIX:
-- Fix 1: Added JOIN products table to access product_name and price
-- Fix 2: Used table aliases (o for orders, p for products) for clarity
-- Fix 3: Specified which table columns come from: p.product_name, o.quantity, p.price
-- Fix 4: Query now correctly JOINs on product_id and can access all needed columns
-- Result shows revenue per product: Laptop $700, Monitor $540, Mouse $105, etc.

-- ============================================================================
-- SUMMARY OF BONUS CHALLENGES
-- ============================================================================
-- Challenge 1: Demonstrates 3-table JOIN with business insight (geographic revenue)
-- Challenge 2: Shows AVG() on derived columns and category analysis
-- Challenge 3: Demonstrates HAVING clause for filtering aggregated results
-- Challenge 4: Shows advanced conditional aggregation with CASE statements
-- Challenge 5: Real-world debugging scenario with intentional errors and fixes
-- ============================================================================
