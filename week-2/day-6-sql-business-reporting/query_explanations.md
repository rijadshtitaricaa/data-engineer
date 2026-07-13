# Query Explanations - Day 6 SQL Business Reporting


## Query 1: Completed Revenue by Category

**File:**  
join_reports.sql

**Business question:**  
Which product category generated the highest completed revenue?

**Tables used:**  
orders and products

**Why JOIN is needed:**  
The orders table only contains product_id. The product name, category, and price are stored inside the products table. JOIN allows us to combine both tables.

**Why WHERE is needed:**  
Only completed orders should be included because pending and cancelled orders are not real revenue.

**Why GROUP BY is needed:**  
We need one result row for each category so we can compare category performance.

**What I understood:**  
This query helps the business understand which product categories generate the most income. Electronics generated the highest completed revenue.


---

## Query 2: Completed Revenue by Product Name

**File:**  
join_reports.sql

**Business question:**  
Which products generate the most completed revenue?

**Tables used:**  
orders and products

**Why JOIN is needed:**  
The orders table stores product_id, while products stores the product name and price.

**Why WHERE is needed:**  
Only completed orders should be counted as revenue.

**Why GROUP BY is needed:**  
Revenue needs to be calculated separately for every product.

**What I understood:**  
This report shows the best-performing products and helps managers understand what products bring the most value.


---

## Query 3: Top 3 Customers by Completed Revenue

**File:**  
join_reports.sql

**Business question:**  
Which customers have generated the most completed revenue?

**Tables used:**  
orders and customers

**Why JOIN is needed:**  
Orders only contains customer_id. Customer names are stored in the customers table.

**Why WHERE is needed:**  
Only completed transactions should affect customer revenue.

**Why GROUP BY is needed:**  
Each customer needs their own revenue calculation.

**Why ORDER BY and LIMIT are needed:**  
ORDER BY sorts customers from highest to lowest revenue and LIMIT returns only the top 3.

**What I understood:**  
This query identifies the most valuable customers and can help create customer loyalty strategies.


---

## Query 4: Count Orders by Status

**File:**  
group_by_reports.sql

**Business question:**  
How many orders are completed, pending, or cancelled?

**Tables used:**  
orders

**Why GROUP BY is needed:**  
Orders need to be separated into groups based on their status.

**Why COUNT is needed:**  
COUNT calculates how many orders exist in each status.

**What I understood:**  
This report gives a quick overview of order performance and transaction health.


---

## Query 5: Customers With More Than One Order

**File:**  
join_reports.sql

**Business question:**  
Which customers have placed multiple orders?

**Tables used:**  
orders and customers

**Why JOIN is needed:**  
The customer name is stored in the customers table, while order information is stored in orders.

**Why GROUP BY is needed:**  
Orders must be counted separately for each customer.

**Why HAVING is needed:**  
HAVING filters grouped results. It only shows customers where the order count is greater than one.

**What I understood:**  
This query helps identify returning customers who may have higher business value.


---

## Query 6: Completed Revenue by City

**File:**  
join_reports.sql

**Business question:**  
Which city generates the highest completed revenue?

**Tables used:**  
orders and customers

**Why JOIN is needed:**  
The orders table has customer_id, but city information exists in the customers table.

**Why WHERE is needed:**  
Only completed orders should contribute to revenue.

**Why GROUP BY is needed:**  
Revenue must be calculated separately for each city.

**What I understood:**  
This report helps businesses understand which locations perform better.


---

## Query 7: Completed Revenue Calculation

**File:**  
basic_aggregations.sql

**Business question:**  
How much real revenue has been generated?

**Tables used:**  
orders and products

**Why JOIN is needed:**  
The price is stored in the products table, while quantity and status are stored in orders.

**Why WHERE is needed:**  
Pending and cancelled orders should not be included.

**Why SUM is needed:**  
SUM adds all completed order values together.

**Calculation:**  
quantity * price

**What I understood:**  
Revenue calculations must use only completed transactions to avoid incorrect business reports.


---

## Query 8: Product Quantity Report

**File:**  
group_by_reports.sql

**Business question:**  
Which products have the highest completed quantity sold?

**Tables used:**  
orders

**Why WHERE is needed:**  
Only completed orders should be counted.

**Why GROUP BY is needed:**  
Each product needs its own total quantity.

**Why SUM is needed:**  
SUM calculates the total number of units sold.

**What I understood:**  
This report shows product demand and helps businesses understand inventory needs.


---

## Overall Understanding

Through these queries I learned that SQL is not only used to display data. SQL can transform raw transaction data into business reports.

Aggregation functions create metrics, GROUP BY creates summaries, HAVING filters grouped results, and JOIN connects multiple tables to create useful reports for decision-making.