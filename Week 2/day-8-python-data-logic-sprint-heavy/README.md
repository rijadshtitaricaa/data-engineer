# Day 8 - Python Data Logic Sprint Heavy Version

## Business Scenario

This project simulates a small business order analysis pipeline.

The company receives raw order data that may contain invalid records, inconsistent values, and different formats. The goal is to clean the data, validate orders, calculate business metrics, and generate reports that help understand sales performance.

The pipeline performs:
- Data validation
- Data cleaning and normalization
- Revenue calculations
- Order analysis
- Customer and product reporting
- Business summary generation


## Files and Folders Included


day-8-python-data-logic-sprint-heavy/

│
├── python_data_analysis.py
│ Main Python script containing validation, cleaning, calculations, and reports.
│
├── order_data.py
│ Contains the raw order dataset.
│
├── output/
│ │
│ ├── invalid_records.txt
│ │ Shows invalid orders and the reasons they were removed.
│ │
│ ├── validation_report.txt
│ │ Contains validation statistics.
│ │
│ └── business_report.txt
│ Contains business metrics, rankings, and revenue reports.
│
├── README.md
│ Project documentation.
│
└── logic_explanations.md
Explanation of the main Python logic used.



## How to Run

1. Make sure Python is installed.

2. Open the project folder in the terminal.

3. Run:

```bash
python python_data_analysis.py
After execution, the generated reports will appear inside the output folder.
Generated Output Files

The script creates:

invalid_records.txt

Contains:

Invalid order IDs
Validation errors
Reasons why records were rejected
validation_report.txt

Contains:

Total number of records
Valid records count
Invalid records count
business_report.txt

Contains:

Completed revenue
Top 5 completed orders
Top customers by revenue
Top products by revenue
Top cities by revenue
Revenue ranking by category
Revenue ranking by channel
Main Python Concepts Practiced

This project practiced:

Lists and dictionaries
Functions
Loops
Conditional statements
Data validation
Data cleaning
String normalization
Dictionary counting patterns
Aggregation logic
Sorting data
Reading and writing files
Building reusable functions
Creating a structured Python data pipeline
What Was Difficult

The most difficult part of this practice was thinking about the order of the data processing steps. The data needed to be validated and cleaned before calculating business metrics because invalid records could create incorrect results. Another challenging part was creating dynamic reports using dictionaries instead of hardcoding values, because the logic needed to work even when new customers, cities, categories, or channels appeared in the data.