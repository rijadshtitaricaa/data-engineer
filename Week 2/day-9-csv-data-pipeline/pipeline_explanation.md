# Day 9 CSV Data Pipeline

## Source Data
Three raw CSV files:
- orders_raw.csv
- customers_raw.csv
- products_raw.csv

## Ingestion
The Python pipeline loads all CSV files using csv.DictReader.

## Bronze layer
The raw CSV files are stored exactly as received without modification.

## Cleaning rules
- Standardize status values.
- Standardize channel values.
- Standardize city names.
- Convert quantity to integer.
- Validate dates.
- Remove invalid records.

## Validation rules
- Customer ID must exist.
- Product ID must exist.
- Quantity must be positive.
- Date must be valid.
- Status must be valid.

## Silver layer
Contains cleaned and validated order records.

## Transformation rules
- Normalize text.
- Convert data types.
- Separate valid and invalid records.

## Gold layer
Generate business-ready reports and summaries.

## Business Output
- Clean orders CSV
- Invalid orders CSV
- Data quality report
- Business summary

## What makes this data trusted
Every record has been validated, cleaned, and checked against customers and products before being used in reporting.