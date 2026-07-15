# Logic Explanations

## 1. Why validation was done before revenue calculation

Validation was done before revenue calculation because invalid records should not affect business reports.

The function `validate_order()` checks every order for problems:
- Empty customer name
- Quantity less than or equal to zero
- Price less than or equal to zero

The function `split_valid_and_invalid_orders()` separates the data into:
- Valid orders
- Invalid orders with reasons

Only valid orders are cleaned and used for revenue calculations.

If revenue was calculated before validation, incorrect records could create false revenue numbers. For example, an order with quantity 0 or a negative price would make the revenue report inaccurate.

---

## 2. How status normalization works

Status normalization is handled by the function `normalize_status()`.

The function receives a status value and converts it to lowercase:

Example:
