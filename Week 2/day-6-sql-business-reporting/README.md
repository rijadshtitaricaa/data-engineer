# Day 6 - SQL Business Reporting Sprint

## Practice Overview

This practice focused on using SQL for business reporting and analytics.

The main goal was to move from simple row-level queries into business-level questions such as:

- How many orders exist?
- How much revenue was generated?
- Which products perform best?
- Which customers are most valuable?
- Which cities generate the most business?

During this practice, I worked with three related database tables:

- `orders`
- `customers`
- `products`

The main SQL concepts practiced were:

- COUNT
- SUM
- AVG
- MIN
- MAX
- GROUP BY
- HAVING
- INNER JOIN


---

# Files Included


day-6-sql-business-reporting/

│
├── setup.sql
├── basic_aggregations.sql
├── group_by_reports.sql
├── join_reports.sql
├── business_report.md
├── query_explanations.md
├── daily_report.txt
├── README.md
│
└── screenshots/
├── setup_tables.png
├── aggregation_results.png
├── group_by_report.png
├── having_result.png
├── join_report.png
├── revenue_by_product.png
└── revenue_by_category.png



---

# Environment Used

This practice was completed using:

- SQLiteOnline.com for creating and running SQL queries
- GitHub for organizing and submitting the project


---

# Database Structure

The database contains three tables.


## orders table

Stores transaction information:

- order_id
- customer_id
- product_id
- order_date
- quantity
- status


## customers table

Stores customer information:

- customer_id
- customer_name
- city


## products table

Stores product information:

- product_id
- product_name
- category
- price


The tables are separated because real-world databases usually store different types of information in different tables.

JOIN operations are used to combine this information when creating reports.


---

# How To Run

Run the SQL files in this order:


## 1. Setup Database

Run:


setup.sql


This file:

- Deletes old tables if they exist
- Creates the three tables
- Inserts all dataset records
- Verifies that the data was inserted correctly


## 2. Basic Aggregations

Run:


basic_aggregations.sql


This file uses:

- COUNT
- SUM
- AVG
- MIN
- MAX

to calculate basic business metrics.


## 3. GROUP BY Reports

Run:


group_by_reports.sql


This file creates grouped reports by:

- status
- date
- customer
- product
- category


It also uses HAVING to filter grouped results.


## 4. JOIN Reports

Run:


join_reports.sql


This file combines:

- orders
- customers
- products

to create business-friendly reports.


---

# SQL Concepts Learned


## Basic Aggregation

Aggregation functions summarize data into useful numbers.

Examples:

### COUNT

Counts records.

Example business question:

"How many completed orders do we have?"


### SUM

Calculates totals.

Example:

"How much completed revenue was generated?"


### AVG

Calculates averages.

Example:

"What is the average product price?"


### MIN and MAX

Find the smallest and largest values.

Example:

"What is the cheapest and most expensive product?"


---

# GROUP BY

GROUP BY creates summary reports by categories.

Examples:

- Orders by status
- Revenue by product
- Revenue by city
- Orders by customer


Instead of seeing every individual row, GROUP BY creates useful summaries.


---

# HAVING

HAVING filters grouped results.

Difference:

WHERE:
- Filters individual rows before grouping.

HAVING:
- Filters groups after aggregation.


Example:

Showing only customers with more than one order.


---

# JOIN

JOIN combines data from multiple tables.

The orders table contains IDs, but not complete information.

For example:

orders:


customer_id = 2
product_id = 102


customers:


customer_id = 2
customer_name = Blend


products:


product_id = 102
product_name = Mouse
price = 15


Using JOIN allows us to create a complete report with:

- Customer name
- City
- Product name
- Category
- Price
- Total amount


---

# Important Business Insight

After analyzing the data:

- Total orders: 14
- Completed orders: 10
- Completed revenue: $3,062

The highest revenue category was:

**Electronics**

The highest revenue product was:

**Laptop**

The city with the highest completed revenue was:

**Prishtina**

The highest-value customer was:

**Blend**


This shows that Electronics products and high-value customers have the biggest impact on revenue.


---

# Business Value of This Report

This SQL reporting workflow can help managers:

- Track sales performance
- Identify successful products
- Understand customer behavior
- Compare city performance
- Make better business decisions


---

# Final Learning Summary

This practice showed that SQL is not only about retrieving rows from a database.

SQL can transform raw data into business reports that support analytics and decision-making.

I learned how to:

- Build a database structure
- Calculate business metrics
- Create grouped reports
- Connect multiple tables using JOIN
- Explain the meaning behind SQL results