import csv

def load_csv(filename):
    with open(filename,"r",newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)
    

orders = load_csv("data/bronze/orders_raw.csv")
customers = load_csv("data/bronze/customers_raw.csv")
products = load_csv("data/bronze/products_raw.csv")

print(len(orders))
print(len(customers))
print(len(products))

customer_lookup = {}

for customer in customers:
    customer_lookup[customer["customer_id"]] = customer
print(customer_lookup["C001"])

product_lookup = {}

for product in products:
    product_lookup[product["product_id"]] = product

print(product_lookup["P004"])

clean_orders = []
invalid_orders = []
for order in orders:
    status = order["status"].strip().lower() if order["status"] else ""
    channel = order["channel"].strip().lower() if order["channel"] else ""

    if status == "completed":
        order["status"] = "completed"

    elif status == "done":
        order["status"] = "completed"

    elif status == "canceled" or status == "cancelled":
        order["status"] = "cancelled"

    elif status == "pending":
        order["status"] = "pending"

    else:
        order["invalid_reason"] = "Invalid status"
        invalid_orders.append(order)
        continue


    try:
        quantity = int(order["quantity"])

        if quantity <= 0:
            order["invalid_reason"] = "Quantity must be greater than 0"
            invalid_orders.append(order)
            continue

        order["quantity"] = quantity

    except ValueError:
        order["invalid_reason"] = "Invalid quantity"
        invalid_orders.append(order)
        continue


    if order["order_date"] == "":
        order["invalid_reason"] = "Missing order date"
        invalid_orders.append(order)
        continue


    if order["customer_id"] not in customer_lookup:
        order["invalid_reason"] = "Invalid customer ID"
        invalid_orders.append(order)
        continue


    if order["product_id"] not in product_lookup:
        order["invalid_reason"] = "Invalid product ID"
        invalid_orders.append(order)
        continue


    if channel in ["online", "store", "web", "bank"]:
        order["channel"] = channel

    else:
        order["channel"] = "unknown"


    customer = customer_lookup[order["customer_id"]]
    product = product_lookup[order["product_id"]]

    clean_order = {
        "order_id": order["order_id"],
        "customer_id": order["customer_id"],
        "customer_name": customer["customer_name"],
        "city": customer["city"].strip().title(),
        "segment": customer["segment"],
        "product_id": order["product_id"],
        "product_name": product["product_name"],
        "category": product["category"],
        "quantity": order["quantity"],
        "price": int(product["price"]),
        "status": order["status"],
        "order_date": order["order_date"],
        "channel": order["channel"],
        "total_amount": order["quantity"] * int(product["price"])
    }

    clean_orders.append(clean_order)



print(len(clean_orders))
print(len(invalid_orders))

print(clean_orders[0])
print(invalid_orders[0])

def write_csv(filename,data):
    if not data:
        return
    with open(filename,"w",newline="")as file:
        writer = csv.DictWriter(file,fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


write_csv("data/silver/orders_clean.csv",clean_orders)
write_csv("data/silver/invalid_orders.csv",invalid_orders)


order["status"] == "completed"


revenue_by_city = {}

for order in clean_orders:
    if order["status"] == "completed":
        city = order["city"]

    if city not in revenue_by_city:
        revenue_by_city[city] = 0

    revenue_by_city[city] += order["total_amount"]

print(revenue_by_city)

city_report = []

for city,revenue in revenue_by_city.items():
    city_report.append({"city":city,"revenue":revenue})

write_csv(
    "data/gold/revenue_by_city.csv",city_report
)

revenue_by_category = {}

for order in clean_orders:
    if order["status"] == "completed":

        category = order["category"]

        if category not in revenue_by_category:
            revenue_by_category[category] = 0

        revenue_by_category[category] += order["total_amount"]


category_report = []

for category, revenue in revenue_by_category.items():
    category_report.append({
        "category": category,
        "revenue": revenue
    })


write_csv(
    "data/gold/revenue_by_category.csv",
    category_report
)


customer_revenue = {}

for order in clean_orders:
    if order["status"] == "completed":

        customer = order["customer_name"]

        if customer not in customer_revenue:
            customer_revenue[customer] = 0

        customer_revenue[customer] += order["total_amount"]

top_customers = []

for customer, revenue in customer_revenue.items():
    top_customers.append({
        "customer_name": customer,
        "revenue": revenue
    })

top_customers = sorted(
    top_customers,
    key=lambda x: x["revenue"],
    reverse=True
)

write_csv(
    "data/gold/top_customers.csv",
    top_customers
)




def main():

    orders = load_csv("data/bronze/orders_raw.csv")
    customers = load_csv("data/bronze/customers_raw.csv")
    products = load_csv("data/bronze/products_raw.csv")

    print(len(orders))
    print(len(customers))
    print(len(products))


    # CUSTOMER LOOKUP
    customer_lookup = {}

    for customer in customers:
        customer_lookup[customer["customer_id"]] = customer


    # PRODUCT LOOKUP
    product_lookup = {}

    for product in products:
        product_lookup[product["product_id"]] = product


    clean_orders = []
    invalid_orders = []


    # SILVER CLEANING
    for order in orders:

        status = order["status"].strip().lower() if order["status"] else ""
        channel = order["channel"].strip().lower() if order["channel"] else ""


        # STATUS NORMALIZATION
        if status == "completed":
            order["status"] = "completed"

        elif status == "done":
            order["status"] = "completed"

        elif status == "canceled" or status == "cancelled":
            order["status"] = "cancelled"

        elif status == "pending":
            order["status"] = "pending"

        else:
            order["invalid_reason"] = "Invalid status"
            invalid_orders.append(order)
            continue


        # QUANTITY VALIDATION
        try:
            quantity = int(order["quantity"])

            if quantity <= 0:
                order["invalid_reason"] = "Quantity must be greater than 0"
                invalid_orders.append(order)
                continue

            order["quantity"] = quantity

        except ValueError:
            order["invalid_reason"] = "Invalid quantity"
            invalid_orders.append(order)
            continue


        # DATE VALIDATION
        if order["order_date"] == "":
            order["invalid_reason"] = "Missing order date"
            invalid_orders.append(order)
            continue


        # CUSTOMER VALIDATION
        if order["customer_id"] not in customer_lookup:
            order["invalid_reason"] = "Invalid customer ID"
            invalid_orders.append(order)
            continue


        # PRODUCT VALIDATION
        if order["product_id"] not in product_lookup:
            order["invalid_reason"] = "Invalid product ID"
            invalid_orders.append(order)
            continue


        # CHANNEL NORMALIZATION
        if channel in ["online", "store", "web", "bank"]:
            order["channel"] = channel

        else:
            order["channel"] = "unknown"



        # ENRICH DATA
        customer = customer_lookup[order["customer_id"]]
        product = product_lookup[order["product_id"]]


        clean_order = {
            "order_id": order["order_id"],
            "customer_id": order["customer_id"],
            "customer_name": customer["customer_name"],
            "city": customer["city"].strip().title(),
            "segment": customer["segment"],
            "product_id": order["product_id"],
            "product_name": product["product_name"],
            "category": product["category"],
            "quantity": order["quantity"],
            "price": int(product["price"]),
            "status": order["status"],
            "order_date": order["order_date"],
            "channel": order["channel"],
            "total_amount": order["quantity"] * int(product["price"])
        }


        clean_orders.append(clean_order)



    print("Clean orders:", len(clean_orders))
    print("Invalid orders:", len(invalid_orders))


    # WRITE SILVER
    write_csv(
        "data/silver/orders_clean.csv",
        clean_orders
    )

    write_csv(
        "data/silver/invalid_orders.csv",
        invalid_orders
    )



    # =====================
    # GOLD - REVENUE CITY
    # =====================

    revenue_by_city = {}

    for order in clean_orders:

        if order["status"] == "completed":

            city = order["city"]

            if city not in revenue_by_city:
                revenue_by_city[city] = 0

            revenue_by_city[city] += order["total_amount"]


    city_report = []

    for city, revenue in revenue_by_city.items():

        city_report.append({
            "city": city,
            "revenue": revenue
        })


    write_csv(
        "data/gold/revenue_by_city.csv",
        city_report
    )



    # ==========================
    # GOLD - REVENUE CATEGORY
    # ==========================

    revenue_by_category = {}

    for order in clean_orders:

        if order["status"] == "completed":

            category = order["category"]

            if category not in revenue_by_category:
                revenue_by_category[category] = 0

            revenue_by_category[category] += order["total_amount"]


    category_report = []

    for category, revenue in revenue_by_category.items():

        category_report.append({
            "category": category,
            "revenue": revenue
        })


    write_csv(
        "data/gold/revenue_by_category.csv",
        category_report
    )



    # =====================
    # GOLD - TOP CUSTOMERS
    # =====================

    customer_revenue = {}

    for order in clean_orders:

        if order["status"] == "completed":

            customer = order["customer_name"]

            if customer not in customer_revenue:
                customer_revenue[customer] = 0

            customer_revenue[customer] += order["total_amount"]


    top_customers = []

    for customer, revenue in customer_revenue.items():

        top_customers.append({
            "customer_name": customer,
            "revenue": revenue
        })


    top_customers = sorted(
        top_customers,
        key=lambda x: x["revenue"],
        reverse=True
    )


    write_csv(
        "data/gold/top_customers.csv",
        top_customers
    )



    # =====================
    # EXECUTIVE SUMMARY
    # =====================

    total_revenue = sum(
        order["total_amount"]
        for order in clean_orders
        if order["status"] == "completed"
    )


    with open(
        "data/gold/executive_summary.txt",
        "w"
    ) as file:

        file.write("Executive Summary\n")
        file.write("=================\n\n")
        file.write(f"Completed Revenue: {total_revenue}\n")
        file.write(f"Completed Orders: {len(clean_orders)}\n")

        if revenue_by_city:
            top_city = max(
                revenue_by_city,
                key=revenue_by_city.get
            )

            file.write(f"Top City: {top_city}\n")
if __name__ == "__main__":
    main()