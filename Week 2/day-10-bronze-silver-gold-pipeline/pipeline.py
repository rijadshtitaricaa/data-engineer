import csv

# BRONZE LAYER



def count_records(filename):
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        return sum(1 for _ in reader)


orders_count = count_records("data/bronze/orders_raw.csv")
customers_count = count_records("data/bronze/customers_raw.csv")
products_count = count_records("data/bronze/products_raw.csv")


print("Bronze Layer:")
print(f"Orders: {orders_count}")
print(f"Customers: {customers_count}")
print(f"Products: {products_count}")



# ------------------------
# SILVER LAYER
# ------------------------


# CLEAN CUSTOMERS

with open("data/bronze/customers_raw.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    customers = list(reader)


city_map = {
    "prishtina": "Prishtina",
    "vushtrri": "Vushtrri",
}


seen_customers = set()
clean_customers = []


for customer in customers:

    if customer["customer_id"] in seen_customers:
        continue

    seen_customers.add(customer["customer_id"])

    city = customer["city"].strip()

    if city == "":
        city = "Unknown"

    else:
        city = city_map.get(city.lower(), city.title())

    customer["city"] = city

    clean_customers.append(customer)



# CLEAN PRODUCTS

with open("data/bronze/products_raw.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    products = list(reader)


clean_products = []


for product in products:

    if product["category"] == "":
        product["category"] = "Unknown"


    try:
        price = float(product["price"])

        if price <= 0:
            continue

    except ValueError:
        continue


    clean_products.append(product)



# LOOKUP DICTIONARIES

customers_dict = {
    c["customer_id"]: c
    for c in clean_customers
}


products_dict = {
    p["product_id"]: p
    for p in clean_products
}




with open("data/bronze/orders_raw.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    orders = list(reader)


clean_orders = []
invalid_orders = []

seen_order_ids = set()



status_map = {
    "completed": "completed",
    "complete": "completed",
    "done": "completed",
    "cancelled": "cancelled",
    "canceled": "cancelled",
    "pending": "pending",
}


channel_map = {
    "online": "online",
    "web": "online",
    "mobile": "online",
    "store": "store",
}



for order in orders:


    # Duplicate order ID

    if order["order_id"] in seen_order_ids:
        order["reason"] = "Duplicate order_id"
        invalid_orders.append(order)
        continue


    seen_order_ids.add(order["order_id"])



    # Missing date

    if order["order_date"].strip() == "":
        order["reason"] = "Missing order date"
        invalid_orders.append(order)
        continue



    # Quantity validation

    try:
        quantity = int(order["quantity"])

        if quantity <= 0:
            raise ValueError

    except ValueError:
        order["reason"] = "Invalid quantity"
        invalid_orders.append(order)
        continue



    # Customer validation

    if order["customer_id"] not in customers_dict:
        order["reason"] = "Customer not found"
        invalid_orders.append(order)
        continue



    # Product validation

    if order["product_id"] not in products_dict:
        order["reason"] = "Product not found"
        invalid_orders.append(order)
        continue



    # Status normalization

    status = order["status"].strip().lower()


    if status in status_map:
        order["status"] = status_map[status]

    else:
        order["reason"] = "Invalid status"
        invalid_orders.append(order)
        continue



    # Channel normalization

    channel = order["channel"].strip().lower()


    if channel == "":
        order["channel"] = "unknown"

    else:
        order["channel"] = channel_map.get(channel, "unknown")



    # Enrichment

    customer = customers_dict[order["customer_id"]]
    product = products_dict[order["product_id"]]


    price = float(product["price"])
    total_amount = quantity * price



    clean_orders.append(
        {
            "order_id": order["order_id"],
            "customer_id": order["customer_id"],
            "customer_name": customer["customer_name"],
            "city": customer["city"],
            "product_id": order["product_id"],
            "product_name": product["product_name"],
            "category": product["category"],
            "quantity": quantity,
            "price": price,
            "total_amount": total_amount,
            "status": order["status"],
            "channel": order["channel"],
            "order_date": order["order_date"],
        }
    )



# ------------------------
# WRITE SILVER FILES
# ------------------------


def write_csv(filename, data, columns):

    with open(filename, "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=columns
        )

        writer.writeheader()
        writer.writerows(data)



write_csv(
    "data/silver/customers_clean.csv",
    clean_customers,
    [
        "customer_id",
        "customer_name",
        "city"
    ]
)



write_csv(
    "data/silver/products_clean.csv",
    clean_products,
    [
        "product_id",
        "product_name",
        "category",
        "price"
    ]
)



write_csv(
    "data/silver/orders_clean.csv",
    clean_orders,
    [
        "order_id",
        "customer_id",
        "customer_name",
        "city",
        "product_id",
        "product_name",
        "category",
        "quantity",
        "price",
        "total_amount",
        "status",
        "channel",
        "order_date"
    ]
)



write_csv(
    "data/silver/invalid_orders.csv",
    invalid_orders,
    [
        "order_id",
        "customer_id",
        "product_id",
        "order_date",
        "quantity",
        "status",
        "channel",
        "reason"
    ]
)



print("\nSilver Layer completed!")
print(f"Clean orders: {len(clean_orders)}")
print(f"Invalid orders: {len(invalid_orders)}")

# ------------------------
# GOLD LAYER
# ------------------------

with open("data/silver/orders_clean.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    silver_orders = list(reader)


revenue_by_category = {}
revenue_by_city = {}
revenue_by_customer = {}
top_products = {}


for order in silver_orders:

    if order["status"] != "completed":
        continue


    revenue = float(order["total_amount"])
    quantity = int(order["quantity"])



    # Revenue by category

    category = order["category"]

    if category not in revenue_by_category:

        revenue_by_category[category] = {
            "category": category,
            "completed_revenue": 0,
            "total_completed_orders": 0
        }


    revenue_by_category[category]["completed_revenue"] += revenue
    revenue_by_category[category]["total_completed_orders"] += 1



    # Revenue by city

    city = order["city"]

    if city not in revenue_by_city:

        revenue_by_city[city] = {
            "city": city,
            "completed_revenue": 0,
            "total_completed_orders": 0
        }


    revenue_by_city[city]["completed_revenue"] += revenue
    revenue_by_city[city]["total_completed_orders"] += 1



    # Revenue by customer

    customer = order["customer_name"]

    if customer not in revenue_by_customer:

        revenue_by_customer[customer] = {
            "customer_name": customer,
            "city": city,
            "completed_revenue": 0,
            "total_completed_orders": 0
        }


    revenue_by_customer[customer]["completed_revenue"] += revenue
    revenue_by_customer[customer]["total_completed_orders"] += 1



    # Top products

    product = order["product_name"]

    if product not in top_products:

        top_products[product] = {
            "product_name": product,
            "category": order["category"],
            "total_quantity_sold": 0,
            "completed_revenue": 0
        }


    top_products[product]["total_quantity_sold"] += quantity
    top_products[product]["completed_revenue"] += revenue



# Convert dictionaries to lists

category_report = list(revenue_by_category.values())

city_report = list(revenue_by_city.values())

customer_report = list(revenue_by_customer.values())

product_report = sorted(
    top_products.values(),
    key=lambda x: x["completed_revenue"],
    reverse=True
)



# Write Gold files


write_csv(
    "data/gold/revenue_by_category.csv",
    category_report,
    [
        "category",
        "completed_revenue",
        "total_completed_orders"
    ]
)



write_csv(
    "data/gold/revenue_by_city.csv",
    city_report,
    [
        "city",
        "completed_revenue",
        "total_completed_orders"
    ]
)



write_csv(
    "data/gold/revenue_by_customer.csv",
    customer_report,
    [
        "customer_name",
        "city",
        "completed_revenue",
        "total_completed_orders"
    ]
)



write_csv(
    "data/gold/top_products.csv",
    product_report,
    [
        "product_name",
        "category",
        "total_quantity_sold",
        "completed_revenue"
    ]
)



print("\nGold Layer completed!")
print("Created:")
print("- revenue_by_category.csv")
print("- revenue_by_city.csv")
print("- revenue_by_customer.csv")
print("- top_products.csv")