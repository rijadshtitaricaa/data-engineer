# Part 3 - Python vs SQL logic comparison

### Task 1: Show completed orders
**Python approach:**
* Loop through the `orders` list.
* Check if `order["status"] == "completed"`.
* Print matching orders.

**SQL approach:**
* SELECT the columns we need.
* FROM the `orders` table.
* Use `WHERE status = 'completed'`.

**What I understood:**
Python uses an imperative, step-by-step approach where the script manually iterates through elements in system memory to filter them. SQL uses a declarative approach where we simply describe the target state using a filtering predicate (`WHERE`), leaving the search optimization to the database engine.

---

### Task 2: Show orders with price > 100
**Python approach:**
* Loop through the `orders` list.
* Apply an conditional statement checking if `order["price"] > 100`.
* Print or save the filtered records.

**SQL approach:**
* SELECT the required attributes.
* FROM the `orders` table.
* Use `WHERE price > 100`.

**What I understood:**
In Python, conditional logic runs row-by-row during execution to evaluate truth values for every item. In SQL, the `WHERE` clause filters rows directly at the storage level, reducing disk I/O and processing only the rows that meet the criteria.

---

### Task 3: Calculate total_amount
**Python approach:**
* Iterate through the dataset using a loop.
* Multiply `order["quantity"] * order["price"]` dynamically.
* Assign the calculation to a temporary local variable or print it.

**SQL approach:**
* SELECT the base columns along with the mathematical expression.
* Compute `quantity * price`.
* Use the `AS total_amount` alias to name the resulting column.

**What I understood:**
Python modifies data or creates new attributes dynamically in memory during iteration. SQL projects computed columns inline as part of the query layout, meaning calculations are processed instantly on the retrieved records without altering the underlying table scheme.

---

### Task 4: Sort by price descending
**Python approach:**
* Use the built-in `sorted()` function or `.sort()` method.
* Define a function or key targeting `price`.
* Set the parameter `reverse=True` to flip the default ascending order.

**SQL approach:**
* SELECT data from the table.
* Add an `ORDER BY price` clause at the end of the query.
* Append the `DESC` modifier to sort from highest to lowest.

**What I understood:**
Python sorts by tracking an evaluation key for every element in an array structure and rearranging their indexes in memory. SQL handles sorting as a final presentation layer step in the database execution pipeline using the `ORDER BY` clause.

---

### Task 5: Show top 3 orders
**Python approach:**
* Sort the entire dataset first by the chosen metric.
* Apply a list slice using the `[:3]` syntax.
* Extract and print the first three array positions.

**SQL approach:**
* Use `ORDER BY` to sort the values sequentially.
* Append a `LIMIT 3` clause to truncate the final output.

**What I understood:**
Python loads and processes the complete collection, and then uses index boundaries to slice out a subset. SQL optimizes memory and network bandwidth by terminating row evaluation as soon as the `LIMIT` threshold is met, preventing unnecessary rows from being sent over the connection.