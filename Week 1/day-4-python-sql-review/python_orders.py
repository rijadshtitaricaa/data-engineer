import csv
orders = [
    {
        "order_id": 1,
        "customer_name": "Arta",
        "city": "Vushtrri",
        "product": "Laptop",
        "category": "Electronics",
        "quantity": 1,
        "price": 700,
        "status": "completed",
        "order_date": "2026-07-01"
    },
    {
        "order_id": 2,
        "customer_name": "Blend",
        "city": "Prishtina",
        "product": "Mouse",
        "category": "Accessories",
        "quantity": 2,
        "price": 15,
        "status": "completed",
        "order_date": "2026-07-01"
    },
    {
        "order_id": 3,
        "customer_name": "Arta",
        "city": "Vushtrri",
        "product": "Keyboard",
        "category": "Accessories",
        "quantity": 1,
        "price": 40,
        "status": "cancelled",
        "order_date": "2026-07-02"
    },
    {
        "order_id": 4,
        "customer_name": "Dren",
        "city": "Mitrovica",
        "product": "Monitor",
        "category": "Electronics",
        "quantity": 1,
        "price": 180,
        "status": "completed",
        "order_date": "2026-07-02"
    },
    {
        "order_id": 5,
        "customer_name": "Elira",
        "city": "Prishtina",
        "product": "Mouse",
        "category": "Accessories",
        "quantity": 1,
        "price": 15,
        "status": "completed",
        "order_date": "2026-07-03"
    },
    {
        "order_id": 6,
        "customer_name": "Dren",
        "city": "Mitrovica",
        "product": "Laptop",
        "category": "Electronics",
        "quantity": 1,
        "price": 700,
        "status": "pending",
        "order_date": "2026-07-03"
    },
    {
        "order_id": 7,
        "customer_name": "Nora",
        "city": "Vushtrri",
        "product": "Headphones",
        "category": "Accessories",
        "quantity": 1,
        "price": 50,
        "status": "completed",
        "order_date": "2026-07-04"
    },
    {
        "order_id": 8,
        "customer_name": "Leart",
        "city": "Peja",
        "product": "Monitor",
        "category": "Electronics",
        "quantity": 2,
        "price": 180,
        "status": "completed",
        "order_date": "2026-07-04"
    },
    {
        "order_id": 9,
        "customer_name": "Faton",
        "city": "Prizren",
        "product": "Desk Chair",
        "category": "Office",
        "quantity": 1,
        "price": 120,
        "status": "completed",
        "order_date": "2026-07-05"
    },
    {
        "order_id": 10,
        "customer_name": "Gresa",
        "city": "Prishtina",
        "product": "USB Cable",
        "category": "Accessories",
        "quantity": 3,
        "price": 8,
        "status": "completed",
        "order_date": "2026-07-05"
    },
    {
        "order_id": 11,
        "customer_name": "Rina",
        "city": "Vushtrri",
        "product": "Laptop",
        "category": "Electronics",
        "quantity": 1,
        "price": 650,
        "status": "cancelled",
        "order_date": "2026-07-06"
    },
    {
        "order_id": 12,
        "customer_name": "Arben",
        "city": "Ferizaj",
        "product": "Desk",
        "category": "Office",
        "quantity": 1,
        "price": 220,
        "status": "pending",
        "order_date": "2026-07-06"
    }
]

# TASK P1 - PRINT BASIC DATA

# TOTAL NUMBER 
print("Total number of orders:", len(orders))

# COSTUMER NAME
print("Costumer names:")
for order in orders[:2]:
    print(order["customer_name"])

# ORDER DETAILS
print("Order Details:")
for order in orders[:1]:
    print(f"{order["customer_name"]} ordered {order["product"]} from {order["city"]} and the status is {order["status"]}\n\n")

print("Task P2: \n")
# TASK P2 - FILTER RECORDS
# Only Completed Orders
print("Completed Orders:")
for order in orders[:2]:
    if order["status"] == "completed":
        print(f"{order["order_id"]} - {order["customer_name"]} - {order["product"]}") 

# Only pending orders
print("Pending Orders:")
for order in orders:
    if order["status"] == "pending":
        print(f"{order["order_id"]} - {order["customer_name"]} - {order["product"]}")

# Only cancelled orders
print("Cancelled Orders:")
for order in orders:
    if order["status"] == "cancelled":
        print(f"{order["order_id"]} - {order["customer_name"]} - {order["product"]}")

# Orders with price greater than 100
print("Orders with price greater than 100:")
for order in orders:
    if order["price"] > 100:
        print(f"{order["customer_name"]} - {order["product"]} ")

# Order where category is Accsesories
print("Category Accessories.\n")
for order in orders:
    if order["category"] == "Accessories":
        print(f"{order["customer_name"]} - {order["category"]}")

# TASK P3 - CALCULATED VALUES
print("Order totals:")
for order in orders:
    total_amount = order["quantity"] * order["price"]
    print(f"{order['customer_name']} - {order['product']} - {order['quantity']} x {order['price']} = {total_amount}")

print("task 4\n")
# TASK P4 - Sorting and top records

def get_price(order):
    return order["price"]

def get_total_amount(order):
    return order["quantity"] * order["price"]

print("Highest to lowest:")
by_price = sorted(orders, key=get_price, reverse=True)
for order in by_price:
    print(f"{order['customer_name']} - {order['product']}: {order['price']}")

print("Orders sorted by total_amount")
by_total = sorted(orders, key=get_total_amount, reverse=True)
for order in by_total:
    print(f"{order['customer_name']} - {order['product']}: {get_total_amount(order)}")


print("Top 3 orders by total amount:")
for order in by_total[:3]:
    print(f"{order['customer_name']} - {order['product']}: {get_total_amount(order)}")

# TASK P5

status_counts = {
    "completed": 0,
    "pending": 0,
    "cancelled": 0
}
customer_counts = {}
completed_revenue = 0

# Loop 
for order in orders:
    status = order["status"]
    if status in status_counts:
        status_counts[status] += 1
    if status == "completed":
        completed_revenue += order["quantity"] * order["price"]
        
    name = order["customer_name"]
    if name in customer_counts:
        customer_counts[name] += 1
    else:
        customer_counts[name] = 1

print("Status counts:")
print(f"completed: {status_counts['completed']}")
print(f"pending: {status_counts['pending']}")
print(f"cancelled: {status_counts['cancelled']}")

print(f"\nCompleted revenue: {completed_revenue}")

print("\nCustomers with more than one order:")
for name, count in customer_counts.items():
    if count > 1:
        print(f"{name} ({count} orders)")