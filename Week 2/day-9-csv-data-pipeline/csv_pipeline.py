import csv


DATA_FOLDER = "data"

def load_csv(file_path):
    data = []

    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    return data

def load_orders():
    orders = load_csv(f"{DATA_FOLDER}/orders_raw.csv")
    print(f"Loaded {len(orders)} raw orders")
    return orders

def load_customers():
    customers = load_csv(f"{DATA_FOLDER}/customers_raw.csv")
    print(f"Loaded {len(customers)} customers.")
    return customers


def load_products():
    products = load_csv(f"{DATA_FOLDER}/products_raw.csv")
    print(f"Loaded {len(products)} products.")
    return products

def build_lookup_table(rows, key_field):
    lookup = {}

    for row in rows:
        lookup[row[key_field]] = row

    return lookup

def normalize_status(status):
    status = status.strip().lower()
    if status in ["completed","complete","done"]:
        return "completed"
    elif status == "pending":
        return "pending"
    elif status in ["cancelled","canceled"]:
        return "cancelled"
    return "unknown"

def normalize_city(city):
    city= city.strip().lower()
    if city == "prishtina":
        return "Prishtina"
    elif city == "vushtrri":
        return "Vushtrri"
    elif city == "mitrovica":
        return "Mitrovica"
    elif city == "peja":
        return "Peja"
    elif city == "prizren":
        return "Prizren"
    elif city == "ferizaj":
        return "Ferizaj"
    return city.title()

def normalize_channel(channel):
    channel = channel.strip().lower()

    if channel in ["online","web"]:
        return "online"
    elif channel == "store":
        return "store"
    elif channel == "":
        return "unknown"
    return "unknown"

def is_positive_integer(value):
    try:
        return int(value) > 0
    except (ValueError, TypeError):
        return False

def validate_order(order, customers_lookup, products_lookup):

    if not order["order_id"]:
        return False, "missing_order_id"

    if not order["customer_id"]:
        return False, "missing_customer_id"

    if order["customer_id"] not in customers_lookup:
        return False, "invalid_customer_id"

    if not order["product_id"]:
        return False, "missing_product_id"

    if order["product_id"] not in products_lookup:
        return False, "invalid_product_id"

    if not order["order_date"]:
        return False, "missing_order_date"

    quantity = order["quantity"]

    if quantity == "":
        return False, "missing_quantity"

    try:
        quantity = int(quantity)
    except ValueError:
        return False, "invalid_quantity"

    if quantity <= 0:
        return False, "negative_quantity"

    if not order["status"]:
        return False, "missing_status"

    status = normalize_status(order["status"])

    if status == "unknown":
        return False, "invalid_status"

    channel = normalize_channel(order["channel"])

    if channel not in ["online", "store", "unknown"]:
        return False, "invalid_channel"

    return True, "valid"
def calculate_total_amount(order):
    return int(order["quantity"]) * float(order["price"])

def enrich_order(order, customers_lookup, products_lookup):

    customer = customers_lookup[order["customer_id"]]
    product = products_lookup[order["product_id"]]

    enriched_order = {
        "order_id": order["order_id"],
        "customer_id": order["customer_id"],
        "customer_name": customer["customer_name"],
        "city": normalize_city(customer["city"]),
        "product_id": order["product_id"],
        "product_name": product["product_name"],
        "category": product["category"],
        "quantity": int(order["quantity"]),
        "price": float(product["price"]),
        "total_amount": calculate_total_amount({
            "quantity": order["quantity"],
            "price": product["price"]
        }),
        "status": normalize_status(order["status"]),
        "channel": normalize_channel(order["channel"]),
        "order_date": order["order_date"]
    }

    return enriched_order

def write_csv(file_path, rows, fieldnames):

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)

def create_data_quality_report(raw_orders, clean_orders, invalid_orders):

    with open("output/data_quality_report.txt", "w") as file:

        file.write("Data Quality Report - Day 9\n\n")

        file.write(f"Total raw orders: {len(raw_orders)}\n")
        file.write(f"Valid orders: {len(clean_orders)}\n")
        file.write(f"Invalid orders: {len(invalid_orders)}\n\n")

        file.write("Invalid records by reason:\n")

        reasons = {}

        for order in invalid_orders:
            reason = order["reason"]

            if reason not in reasons:
                reasons[reason] = 0

            reasons[reason] += 1

        for reason, count in reasons.items():
            file.write(f"{reason}: {count}\n")

        file.write("\nBronze input files checked:\n")
        file.write("- orders_raw.csv\n")
        file.write("- customers_raw.csv\n")
        file.write("- products_raw.csv\n")

        file.write("\nSilver output files created:\n")
        file.write("- orders_clean.csv\n")

        file.write("\nMain data quality problems found:\n")
        file.write("- Missing quantities\n")
        file.write("- Invalid customer/product IDs\n")
        file.write("- Incorrect status values\n")
        file.write("- Missing dates\n")

def count_by_field(rows, field_name):
    counts = {}

    for row in rows:
        value = row[field_name]

        if value not in counts:
            counts[value] = 0

        counts[value] += 1

    return counts

def sum_by_field(rows, group_field, amount_field):

    totals = {}

    for row in rows:
        group = row[group_field]
        amount = float(row[amount_field])

        if group not in totals:
            totals[group] = 0

        totals[group] += amount

    return totals

def get_completed_orders(rows):

    completed = []

    for row in rows:
        if row["status"] == "completed":
            completed.append(row)

    return completed

def get_top_n_by_field(rows, field_name, n):

    totals = {}

    for row in rows:

        name = row[field_name]

        amount = float(row["total_amount"])

        if name not in totals:
            totals[name] = 0

        totals[name] += amount


    sorted_values = sorted(
        totals.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_values[:n]

def create_business_summary(clean_orders):

    completed_orders = get_completed_orders(clean_orders)

    completed_revenue = sum(
        float(order["total_amount"])
        for order in completed_orders
    )


    with open("output/business_summary.txt", "w") as file:

        file.write("Business Summary - Day 9\n\n")

        file.write(
            f"Completed revenue: {completed_revenue}\n\n"
        )


        file.write("Orders by status:\n")

        for key, value in count_by_field(clean_orders, "status").items():
            file.write(f"{key}: {value}\n")


        file.write("\nOrders by city:\n")

        for key, value in count_by_field(clean_orders, "city").items():
            file.write(f"{key}: {value}\n")

        


        file.write("\nRevenue by category:\n")

        revenue_category = sum_by_field(
            completed_orders,
            "category",
            "total_amount"
        )

        for key, value in revenue_category.items():
            file.write(f"{key}: {value}\n")


        file.write("\nRevenue by channel:\n")

        revenue_channel = sum_by_field(
            completed_orders,
            "channel",
            "total_amount"
        )

        for key, value in revenue_channel.items():
            file.write(f"{key}: {value}\n")


        file.write("\nTop 3 customers by completed revenue:\n")

        for customer, revenue in get_top_n_by_field(
            completed_orders,
            "customer_name",
            3
        ):
            file.write(f"{customer}: {revenue}\n")


        file.write("\nTop 3 products by completed revenue:\n")

        for product, revenue in get_top_n_by_field(
            completed_orders,
            "product_name",
            3
        ):
            file.write(f"{product}: {revenue}\n")


        most_value = max(
            completed_orders,
            key=lambda x: float(x["total_amount"])
        )

        file.write("\nMost valuable completed order:\n")
        file.write(
            f"Order {most_value['order_id']} - {most_value['total_amount']}\n"
        )


        file.write(
            "\nOrders that should not count as revenue:\n"
        )

        file.write(
            "- Pending orders\n"
            "- Cancelled orders\n"
        )


        file.write(
            "\nBusiness recommendation:\n"
        )

        file.write(
            "Focus on completed sales and investigate cancelled orders.\n"
        )


        file.write(
            "\nWhy this Gold output can be trusted:\n"
        )

        file.write(
            "Only validated and cleaned orders were used for calculations.\n"
        )
def main():

    # Load raw data (Bronze)
    orders = load_orders()
    customers = load_customers()
    products = load_products()


    # Build lookup tables
    customers_lookup = build_lookup_table(customers, "customer_id")
    products_lookup = build_lookup_table(products, "product_id")


    clean_orders = []
    invalid_orders = []


    # Validate orders
    for order in orders:

        valid, reason = validate_order(
            order,
            customers_lookup,
            products_lookup
        )

        if valid:
            enriched_order = enrich_order(
                order,
                customers_lookup,
                products_lookup
            )

            clean_orders.append(enriched_order)

        else:
            order["reason"] = reason
            invalid_orders.append(order)


    clean_fields = [
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


    invalid_fields = [
        "order_id",
        "customer_id",
        "product_id",
        "order_date",
        "quantity",
        "status",
        "channel",
        "reason"
    ]


    # Write Silver files
    write_csv(
        "output/orders_clean.csv",
        clean_orders,
        clean_fields
    )


    write_csv(
        "output/invalid_orders.csv",
        invalid_orders,
        invalid_fields
    )


    # Create reports
    create_data_quality_report(
        orders,
        clean_orders,
        invalid_orders
    )


    create_business_summary(
        clean_orders
    )


    print("Pipeline completed successfully!")
    print(f"Clean orders: {len(clean_orders)}")
    print(f"Invalid orders: {len(invalid_orders)}")


if __name__ == "__main__":
    main()