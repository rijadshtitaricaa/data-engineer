# Day 11 - Python + SQL Pipeline Preparation

## Data Understanding

### 1. How many raw orders exist?
There are **24 raw orders** in `orders_raw.csv`.

### 2. Which columns are used to join the datasets?

- `customer_id` → joins `orders_raw.csv` with `customers_raw.csv`
- `product_id` → joins `orders_raw.csv` with `products_raw.csv`

### 3. Which values look inconsistent?

Some examples of inconsistent or invalid data:

- Missing quantity
- Negative quantity (`-1`)
- Zero quantity (`0`)
- Non-numeric quantity (`abc`)
- Missing status
- Different status formats (`completed`, `Completed`, `done`, `canceled`, `cancelled`, `returned`)
- Missing order date
- Invalid product ID (`P999`)
- Missing channel
- Different channel casing (`online`, `Online`, `Store`)
- Different city casing (`prishtina`, `Prishtina`, `VUSHTRRI`, `ferizaj`)

### 4. Which records should not be trusted for revenue?

Orders with:
- Missing quantity
- Quantity less than or equal to 0
- Non-numeric quantity
- Invalid product IDs
- Missing order date
- Missing status
- Cancelled or canceled status
- Returned status
- "done" status (until standardized)
- Pending orders (not completed)

These records should either be cleaned, standardized, or moved to the invalid orders file.

### 5. Bronze, Silver, and Gold layers

#### Bronze
Raw input files without any modifications:
- orders_raw.csv
- customers_raw.csv
- products_raw.csv

#### Silver
Validated and cleaned data:
- orders_clean.csv
- invalid_orders.csv

#### Gold
Business-ready reporting files:
- revenue_by_city.csv
- revenue_by_category.csv
- top_customers.csv
- executive_summary.txt