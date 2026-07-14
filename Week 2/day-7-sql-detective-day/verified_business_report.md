# Verified Business Report - Day 7 SQL Detective Day

## 1. Total order activity
**Insight:** The business has processed a significant volume of orders across the July period, representing various customer interactions and revenue opportunities.

**Verified result:** 14 total orders

**SQL query used:** [V1](validation_queries.sql) - `SELECT COUNT(*) AS total_orders FROM orders;`

**Business meaning:** With 14 orders in the dataset, this establishes the baseline transaction volume. This metric helps track business activity and serves as the denominator for calculating order conversion rates and other performance metrics.

---

## 2. Completed revenue
**Insight:** The business has generated verified revenue only from completed orders, excluding pending and cancelled transactions which represent lost or uncertain revenue.

**Verified result:** $1,639.00 in completed revenue from 10 completed orders

**SQL query used:** [V7](validation_queries.sql) - `SELECT SUM(o.quantity * p.price) AS completed_revenue FROM orders o JOIN products p ON o.product_id = p.product_id WHERE o.status = 'completed';`

**Business meaning:** Only orders with "completed" status count as actual revenue. The remaining 4 orders (2 pending + 2 cancelled) worth approximately $1,660 represent lost or uncertain revenue. This distinction is critical for accurate financial reporting and forecasting.

---

## 3. Revenue by product
**Insight:** Product performance varies significantly. High-value electronics generate substantial revenue despite lower transaction volumes, while accessories drive revenue through volume.

**Verified result:**
- Monitor: $540.00 (3 completed orders)
- Laptop: $700.00 (1 completed order)
- Mouse: $105.00 (3 completed orders)
- Headphones: $150.00 (2 completed orders)
- Desk Chair: $120.00 (1 completed order)
- USB Cable: $24.00 (1 completed order)

**SQL query used:** [V8](validation_queries.sql) - `SELECT p.product_name, SUM(o.quantity * p.price) AS revenue FROM orders o JOIN products p ON o.product_id = p.product_id WHERE o.status = 'completed' GROUP BY p.product_name;`

**Business meaning:** Laptops generate the highest single-product revenue ($700), followed by Monitors ($540). However, Laptops sold through fewer units, suggesting these are premium items. Mice and Headphones show strong volume-based revenue performance, indicating consistent demand for accessories.

---

## 4. Revenue by category
**Insight:** Electronics is the dominant revenue category, contributing nearly 76% of all completed revenue, while Accessories and Office furniture represent smaller revenue streams.

**Verified result:**
- Electronics: $1,240.00 (75.7% of completed revenue)
- Accessories: $279.00 (17.0% of completed revenue)
- Office: $120.00 (7.3% of completed revenue)

**SQL query used:** [V9](validation_queries.sql) - `SELECT p.category, SUM(o.quantity * p.price) AS revenue FROM orders o JOIN products p ON o.product_id = p.product_id WHERE o.status = 'completed' GROUP BY p.category;`

**Business meaning:** Electronics category is the business's primary revenue driver. The data suggests the target customer base prioritizes technology purchases. Marketing and inventory decisions should reflect this strong preference for electronics over office furniture.

---

## 5. Orders by city
**Insight:** Customer orders are distributed across 6 cities in the region, with Prishtina and Vushtrri showing the strongest order activity, suggesting these are the primary market zones.

**Verified result:**
- Prishtina: 5 orders
- Vushtrri: 4 orders
- Mitrovica: 2 orders
- Peja: 1 order
- Prizren: 1 order
- Ferizaj: 1 order

**SQL query used:** [V10](validation_queries.sql) - `SELECT c.city, COUNT(*) AS order_count FROM orders o JOIN customers c ON o.customer_id = c.customer_id GROUP BY c.city;`

**Business meaning:** Prishtina and Vushtrri represent 64% of order activity (9 of 14 orders). This geographic concentration indicates these cities are the strongest markets for expansion or customer retention focus. The remaining cities show minimal activity, representing potential growth opportunities or underserved markets.

---

## 6. Customers with more than one order
**Insight:** A portion of customers demonstrate repeat purchase behavior, which indicates customer loyalty and recurring revenue potential.

**Verified result:** 4 customers placed more than one order:
- Arta (Customer 1): 2 orders
- Blend (Customer 2): 2 orders
- Dren (Customer 3): 2 orders
- Elira (Customer 4): 2 orders

**SQL query used:** [V11](validation_queries.sql) - `SELECT c.customer_id, c.customer_name, COUNT(o.order_id) AS order_count FROM orders o JOIN customers c ON o.customer_id = c.customer_id GROUP BY c.customer_id, c.customer_name HAVING COUNT(o.order_id) > 1;`

**Business meaning:** 40% of active customers (4 of 10 customers) are repeat buyers, suggesting good product satisfaction and customer retention. These repeat customers are ideal candidates for loyalty programs or personalized marketing campaigns to increase lifetime value.

---

## 7. Orders not counted as revenue
**Insight:** A significant amount of potential revenue ($1,660.00) has been lost or remains uncertain due to pending and cancelled orders, representing a 50% gap between order volume and actual revenue.

**Verified result:** 4 orders worth $1,660.00 are not counted as revenue:
- 2 cancelled orders: $740.00
- 2 pending orders: $920.00

**SQL query used:** [V13](validation_queries.sql) - `SELECT * FROM orders WHERE status IN ('pending', 'cancelled');`

**Business meaning:** The pending orders ($920) represent immediate revenue at risk if customers don't complete payment or change their minds. The cancelled orders ($740) indicate lost opportunities. Combined, these represent 50% of total order value, highlighting the critical importance of improving order completion rates and reducing cancellations. Investigating why orders are being cancelled is essential for revenue optimization.

---

## 8. Final recommendation
Based on the verified data, my recommendation is: 

**Focus on three strategic priorities:**

1. **Revenue Protection**: Implement order follow-up procedures for the 2 pending orders ($920 at risk) to ensure completion. Investigate why 2 orders were cancelled ($740 lost) and implement preventive measures.

2. **Geographic Expansion**: Concentrate marketing efforts on Prishtina and Vushtrri where 64% of orders originate, but explore untapped markets in Peja, Prizren, and Ferizaj with targeted campaigns.

3. **Customer Loyalty Program**: Leverage the 4 repeat customers (40% retention rate) with exclusive offers and loyalty rewards. Simultaneously, develop strategies to convert the 6 one-time customers into repeat buyers, focusing on high-value product bundling and personalized recommendations.

**Immediate action**: The $1,660 in non-completed orders represents as much value as the confirmed revenue. Reducing cancellation rate by just 50% would add $370 in immediate revenue (23% increase). Completing all pending orders would add $920 (56% increase).
