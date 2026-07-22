Mistakes and Fixes

Foreign Key Test 1

Attempt: Inserted an order with `customer_id = 999`.

Results: The database rejected the insert because the customer does not exist.

Correct Insert: Use a valid customer_id such as `1`.

---

Foreign Key Test 2

**Attempt:** Inserted an order_item with `order_id = 999`.

**Result:** The database rejected the insert because the order does not exist.

**Correct Insert:** Use an existing order_id.

---

## Foreign Key Test 3

**Attempt:** Inserted an order_item with `product_id = 999`.

**Result:** The database rejected the insert because the product does not exist.

**Correct Insert:** Use an existing product_id.

---

## CHECK Test 1

**Attempt:** Inserted a product with a price of `0`.

**Result:** The database rejected the insert because the price must be greater than 0.

**Correct Insert:** Use a positive price such as `150`.

---

## CHECK Test 2

**Attempt:** Inserted an order_item with a quantity of `0`.

**Result:** The database rejected the insert because quantity must be greater than 0.

**Correct Insert:** Use a quantity of at least `1`.

---

## Status CHECK Test

**Attempt:** Inserted an order with status `done`.

**Result:** The database rejected the insert because only `completed`, `pending`, and `cancelled` are allowed.

**Correct Insert:** Use one of the allowed status values.
