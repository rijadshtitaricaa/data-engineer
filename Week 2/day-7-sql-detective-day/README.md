# Day 7 - SQL Detective Day

## Practice Goal

The goal of this practice was to develop SQL debugging and business verification skills. We started with broken SQL queries that contained real-world errors—missing JOINs, incorrect table references, syntax errors, and logic mistakes. By identifying and fixing these queries, we learned how to read error messages, understand table relationships, and write correct SQL. We then created validation queries to verify business metrics and compiled a professional business report backed entirely by SQL results, not assumptions.

---

## Files Included

```
day-7-sql-detective-day/
├── setup.sql                      # Creates and populates the database tables
├── table_inspection.sql           # Verifies table structure and row counts
├── broken_queries.sql             # Original broken queries with intentional errors
├── fixed_queries.sql              # Corrected queries with explanatory comments
├── validation_queries.sql         # Comprehensive business metric queries
├── verified_business_report.md    # Business insights backed by verified SQL results
├── query_explanations.md          # Detailed explanations of query logic
├── bonus.sql                      # Bonus challenge queries
├── README.md                      # This file
├── daily_report.txt               # Daily practice summary
└── screenshots/                   # Screenshot evidence of successful execution
```

---

## How to Run the SQL Files

Execute the SQL files in this exact order to properly set up and validate the database:

### 1. **setup.sql** (First - Database Creation)
- Creates three tables: `customers`, `products`, and `orders`
- Drops existing tables to ensure clean state
- Inserts 10 customers across 6 cities
- Inserts 8 products across 3 categories (Electronics, Accessories, Office)
- Inserts 14 orders with various statuses (completed, pending, cancelled)
- **Purpose**: Establish the database foundation

### 2. **table_inspection.sql** (Second - Verification)
- Verifies the three tables were created correctly
- Shows the structure and row count of each table
- Confirms data integrity before running queries
- **Purpose**: Confirm the database is ready

### 3. **fixed_queries.sql** (Third - Fixed Queries)
- Contains 10 corrected SQL queries
- Each has explanatory comments about what was wrong
- Shows how to properly JOIN tables and handle common errors
- **Purpose**: Learn from corrected mistakes

### 4. **validation_queries.sql** (Fourth - Business Metrics)
- Contains 15 validation queries
- Calculates key business metrics (revenue, counts, distributions)
- Provides the data used in the verified business report
- **Purpose**: Generate verified numbers for decision-making

### 5. **Review verified_business_report.md** (Final - Business Insights)
- Presents 8 key business insights
- Each insight includes the verified SQL result
- References the specific validation query used
- Explains the business meaning behind each number
- **Purpose**: Transform SQL results into business context

**Bonus queries**: Run **bonus.sql** to explore advanced aggregations and comparisons.

---

## What Was Learned About Debugging SQL

### 1. **Read the Error Message Carefully**
Broken queries taught us that SQL error messages are usually specific. "Column 'city' not found" immediately tells us to check which table has the city column. We learned not to ignore or guess at errors, but to use them as debugging tools.

### 2. **Understand Table Relationships**
Many broken queries failed because they tried to access columns from the wrong table. The key lesson: know which table stores which information. Customers table has cities, products table has prices, orders table has quantities. When you need data from multiple tables, you must JOIN them.

### 3. **JOIN is Required When Data Spans Tables**
If a query needs information from more than one table, a JOIN is not optional—it's required. Query 1 was broken because it tried to get city from orders table (where city doesn't exist). Adding the JOIN to customers fixed it instantly.

### 4. **Column Selection Affects Query Validity**
Broken Query 7 had `GROUP BY status;` instead of `GROUP BY status` (extra semicolon). The semicolon ends the query prematurely. This taught us that syntax matters—every character affects whether the query runs.

### 5. **Filtering Status Matters for Business Logic**
Broken Query 10 tried to show "revenue-worthy" orders but showed all orders including pending. We learned that WHERE clauses aren't just technical details—they encode business rules. "Completed" orders = real revenue. "Pending" and "cancelled" = not revenue.

### 6. **JOIN Conditions Must Be Correct**
Query 9 was broken because it tried to JOIN orders to products on customer_id (wrong!). The correct condition is `ON o.product_id = p.product_id`. This taught us that JOINs don't just need to exist—they need to connect the right columns or you get nonsensical results.

---

## What Was Learned About Verifying Business Reports

### 1. **Every Number Must Have a Source Query**
In the verified business report, we didn't just write "Revenue is $1,639" and hope it's true. We backed it with Query V7 that calculates exactly that result. This is how real data teams work—every claim must be auditable.

### 2. **Context Matters More Than Numbers**
The number "$1,640" is meaningless without context. Is that good or bad? Our report explains: it's 50% of total order value because the other 50% is pending or cancelled. This context lets business leaders make decisions.

### 3. **Different Queries Answer Different Questions**
- V1 answers "How many orders total?" (14)
- V7 answers "How much verified revenue?" ($1,639)
- V10 answers "Where are our customers?" (Prishtina and Vushtrri)

Each query is targeted. We don't try to answer all questions with one query.

### 4. **Filter for Business Reality**
Query V7 filters to `WHERE status = 'completed'` because pending and cancelled orders aren't revenue. This is a business decision encoded in SQL. It teaches us that queries must reflect real business logic, not just raw data.

### 5. **Aggregation Reveals Patterns**
Raw order data (14 rows) is hard to interpret. But when we aggregate by city, category, status, and product, patterns emerge: Electronics dominates revenue, Prishtina is the strongest market, 40% of customers are repeat buyers. SQL aggregation transforms raw data into insights.

### 6. **Recommendations Require Multiple Data Points**
Our final recommendation to "Focus on revenue protection, geographic expansion, and loyalty programs" came from synthesizing multiple verified metrics—not from a single query. This teaches us that business decisions need multiple angles of data analysis.

---

## Key Takeaways

- **SQL debugging is detective work**: Read errors carefully, test hypotheses, verify with data.
- **Table relationships matter**: Understand your schema before writing queries.
- **Business logic belongs in queries**: Use WHERE, GROUP BY, and HAVING to encode what counts.
- **Verified reports > guesses**: Always back claims with queries.
- **Aggregation reveals patterns**: GROUP BY and SUM transform rows into insights.
