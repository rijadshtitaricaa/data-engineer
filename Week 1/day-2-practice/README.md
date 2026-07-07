# Day 2 Practice - CSV Mini Data Pipeline

This project reads raw student data from a CSV file, checks data quality issues, cleans the data, saves a cleaned CSV file, and generates a summary report.

The goal of this mini pipeline is to practice basic Data Engineering concepts such as extracting data, validating information, transforming raw records, and creating useful reports.

## Input:
- `data/students_raw.csv`

The input file contains raw student records that may include missing values, invalid data, and inconsistent text formats.

## Outputs:
- `output/students_clean.csv`
  - Contains the cleaned and transformed student dataset.

- `output/data_quality_report.txt`
  - Contains detected data quality issues such as missing values, invalid numbers, and inconsistent values.

- `output/summary_report.txt`
  - Contains a final analysis report with statistics about the cleaned dataset.

## How to run:

Run the pipeline from the project folder:

```bash
python csv_pipeline.py

After running the script, the cleaned data and reports will be generated inside the output folder.

Concepts practiced:
CSV file handling
Lists and dictionaries
Loops and conditions
Data cleaning and validation
Functions
Data transformation
Generating terminal reports