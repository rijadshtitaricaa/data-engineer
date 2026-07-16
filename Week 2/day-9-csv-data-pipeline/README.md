# Day 9 - CSV Data Pipeline: From Raw Data to Clean Reports

## Practice Goal

The goal of this practice is to build a complete data pipeline using Python's built-in CSV tools.

The pipeline takes messy raw CSV data, validates and cleans it, enriches orders using customer and product information, and creates trusted business reports.

This practice helps understand the foundations of data engineering before working with tools like Databricks.

---

# Medallion Architecture in This Task

## Bronze Layer

The Bronze layer contains the original raw data.

In this project:
- orders_raw.csv
- customers_raw.csv
- products_raw.csv

The data is loaded exactly as received without manual changes.

---

## Silver Layer

The Silver layer contains cleaned and validated data.

In this project:
- Invalid records are separated into invalid_orders.csv.
- Valid orders are enriched with customer and product information.
- Status, city, and channel values are normalized.
- Data types are cleaned.

The result is:

- orders_clean.csv

---

## Gold Layer

The Gold layer contains business-ready outputs used for reporting and analysis.

In this project:

- business_summary.txt
- data_quality_report.txt

These files contain trusted business metrics such as:
- Completed revenue
- Orders by status
- Revenue by category
- Top customers
- Top products

---

# Project Structure


day-9-csv-data-pipeline/

├── data/
│ ├── orders_raw.csv
│ ├── customers_raw.csv
│ └── products_raw.csv
│
├── output/
│ ├── orders_clean.csv
│ ├── invalid_orders.csv
│ ├── business_summary.txt
│ └── data_quality_report.txt
│
├── csv_pipeline.py
├── pipeline_explanation.md
├── daily_report.txt
├── README.md
└── screenshots/


---

# How to Run the Pipeline

1. Make sure Python is installed.

2. Navigate to the project folder:


cd day-9-csv-data-pipeline


3. Run the pipeline:


python csv_pipeline.py


4. The script will automatically generate all output files inside the `output/` folder.

---

# Generated Output Files

## orders_clean.csv

Contains validated and enriched orders.

Includes:
- Customer information
- Product information
- Calculated total amount
- Normalized values

---

## invalid_orders.csv

Contains orders that failed validation.

Each invalid record includes a reason, such as:

- missing_quantity
- invalid_customer_id
- invalid_product_id
- invalid_status

---

## data_quality_report.txt

Contains information about:

- Total raw records
- Valid records
- Invalid records
- Data quality problems found

---

## business_summary.txt

Gold-level business report containing:

- Completed revenue
- Orders by status
- Orders by city
- Revenue by category
- Revenue by channel
- Top customers
- Top products

---

# Why pandas was not used

Pandas was intentionally not used in this practice.

The goal was to understand the manual logic behind a data pipeline first:
- Reading CSV files
- Cleaning data
- Validating records
- Creating lookup tables
- Performing joins
- Transforming data

Understanding these concepts manually makes it easier to work later with tools like Databricks, Spark, and Delta Lake.