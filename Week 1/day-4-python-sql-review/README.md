# Day 4 - Python and SQL Logic Review

## Project Goal
The goal of this practice is to bridge the gap between procedural programming in Python and declarative data querying in SQL. By solving identical data manipulation tasks—such as filtering, calculating values, sorting records, and aggregating statistics—across both technologies, this project reinforces how different backend layers process and optimize data structures.

---

## Files Included
This repository contains the following core files:
* **`python_orders.py`** – A structured Python script executing imperative data tasks using loops, conditional filters, standard sorting functions, and dictionary counters.
* **`setup.sql`** – The initialization script that drops pre-existing tables, creates the `orders` relational schema, and seeds it with custom test records.
* **`sql_queries.sql`** – A collection of analytical queries mapping directly to the business logic handled in the Python script.
* **`comparison.md`** – A detailed technical breakdown comparing row-by-row procedural logic with set-based execution pipelines.
* **`daily_report.txt`** – A concise business summary answering key financial and operational questions regarding the dataset.

---

## Execution Guide

### How to run python_orders.py
Ensure you have Python 3 installed on your local environment. Run the script directly from your terminal or command prompt:

```bash
python python_orders.py