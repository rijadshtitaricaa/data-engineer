# Day 11 - Python + SQL Pipeline Preparation

## Project Goal

The goal of this project was to build a small data pipeline that transforms messy raw business data into clean and trusted reporting data.

The pipeline follows the Bronze → Silver → Gold structure:

- Bronze: Raw CSV files
- Silver: Clean and validated data
- Gold: Business reports for analysis

Python was used for data cleaning and transformation, while SQL was used for business reporting from trusted Silver data.

---

# Bronze Data

## What raw files did you receive?

The Bronze layer contained three raw CSV files:

- orders_raw.csv
- customers_raw.csv
- products_raw.csv

These files represented orders, customer information, and product information from a technology and training business.

## What problems did you notice?

The raw data contained multiple quality issues:

- Missing quantities
- Negative quantities
- Non-numeric quantities
- Missing statuses
- Invalid statuses
- Different status formats (Completed, completed, done)
- Different city casing (prishtina, VUSHTRRI)
- Missing order dates
- Invalid customer IDs
- Invalid product IDs
- Missing channels
- Cancelled orders that should not count as completed revenue

---

# Silver Data

## What validation rules did you apply?

The pipeline applied these validation rules:

- Quantity must exist
- Quantity must be numeric
- Quantity must be greater than 0
- Status must be valid
- Order date cannot be empty
- Customer ID must exist
- Product ID must exist
- Duplicate records should be rejected
- Invalid records are separated from clean data

Invalid records were stored separately in:


data/silver/invalid_orders.csv


Trusted records were stored in:


data/silver/orders_clean.csv


## Which records became invalid and why?

The following records were removed from trusted data:

- Order 3: Missing quantity
- Order 6: Negative quantity
- Order 7: Invalid quantity value
- Order 8: Missing status
- Order 9: Missing order date
- Order 14: Invalid status (returned)
- Order 16: Invalid customer ID
- Order 17: Invalid product ID
- Order 22: Quantity was 0

## What did you normalize?

The pipeline normalized:

### Status

Examples:

- Completed → completed
- done → completed
- canceled → cancelled

### City names

Examples:

- prishtina → Prishtina
- VUSHTRRI → Vushtrri

### Channel values

Accepted values:

- online
- store
- web
- bank

Missing or unknown values became:

- unknown

---

# Gold Reports

## What business reports did you create?

The Gold layer contains:

- revenue_by_city.csv
- revenue_by_category.csv
- top_customers.csv
- executive_summary.txt

These reports answer business questions such as:

- Which cities generate the most revenue?
- Which categories perform best?
- Which customers bring the most revenue?
- How much completed revenue was generated?

## Which report is most useful for a manager?

The most useful report is the executive summary because it gives a quick overview of business performance.

It shows:

- Completed revenue
- Number of completed orders
- Best performing city

A manager can quickly understand the current situation without checking every record.

---

# Python vs SQL

## What did Python help you do?

Python was used for:

- Reading raw CSV files
- Cleaning invalid data
- Validating records
- Normalizing values
- Joining customer and product information
- Creating Silver data
- Generating Gold reports

Python was useful because it allowed custom validation logic before storing trusted data.

## What did SQL help you do?

SQL was used for:

- Querying clean Silver data
- Aggregating business metrics
- Using GROUP BY operations
- Calculating revenue
- Answering reporting questions

SQL was useful because it is designed for fast business analysis.

---

# Data Quality Notes

Data quality was improved by separating invalid records instead of deleting them.

The pipeline keeps:

- Trusted records for reporting
- Invalid records for investigation

This makes the data process more reliable and easier to debug.

---

# Business Insights

From the cleaned data:

- Completed orders are the only orders counted as revenue.
- Different product categories contribute different amounts of revenue.
- Some cities generate higher completed revenue than others.
- Customer performance can be compared using completed revenue.

---

# What I Can Explain Live

I can explain:

- Bronze, Silver, and Gold data layers
- How CSV files are loaded using Python
- How dictionaries were used as lookup tables
- How validation rules remove bad data
- How clean data is enriched with customer and product information
- How Python dictionaries compare to SQL GROUP BY
- How SQL reports are created from trusted data

---

# What I Would Improve Next

Possible improvements:

- Move the pipeline into separate functions and modules
- Add automated tests
- Add logging instead of print statements
- Add duplicate record detection
- Connect the pipeline to a database
- Move the workflow into Databricks with Spark
- Schedule the pipeline to run automatically