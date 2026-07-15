from order_data import orders


def validate_order(order):
    reasons = []

    if order["customer_name"] == "":
        reasons.append("Empty customer name")

    if order["quantity"] <= 0:
        reasons.append("Invalid quantity")

    if order["price"] <= 0:
        reasons.append("Invalid price")

    return reasons  


def split_valid_and_invalid_orders(orders):
    valid_orders = []
    invalid_orders = []

    for order in orders:
        reasons = validate_order(order)

        if len(reasons) == 0:
            valid_orders.append(order)
        else:
            invalid_orders.append({
                "order": order,
                "reasons": reasons
            })

    return valid_orders, invalid_orders

def write_invalid_records(invalid_orders):
    with open("output/invalid_records.txt", "w") as file:
        file.write("Invalid Records\n")
        file.write("================\n\n")

        for record in invalid_orders:
            order = record["order"]
            reasons = record["reasons"]

            file.write(f"Order ID: {order['order_id']}\n")
            file.write("Reasons:\n")

            for reason in reasons:
                file.write(f"- {reason}\n")

            file.write("\n")


def write_validation_report(valid_orders, invalid_orders):
    with open("output/validation_report.txt", "w") as file:
        file.write("Validation Report\n")
        file.write(f"Total records: {len(valid_orders) + len(invalid_orders)}\n")
        file.write(f"Valid records: {len(valid_orders)}\n")
        file.write(f"Invalid records: {len(invalid_orders)}\n")

def normalize_status(status):
    status = status.lower()

    if status == "complete":
        return "completed"
    return status

print(normalize_status("Completed"))
print(normalize_status("complete"))
print(normalize_status("completed\n"))

def normalize_city(city):
    if city == "Prishtine":
        return "Prishtina"
    return city.title()

print(normalize_city("Prishtine"))
print(normalize_city("vushtrri"))
print(normalize_city("mitrovica\n"))

def normalize_category(category):
    return category.title()
print(normalize_category("accessories"))
print(normalize_category("Electronics\n"))

def normalize_channel(channel):
    return channel.lower()

print(normalize_channel("Online"))
print(normalize_channel("STORE"))

def clean_order(order):
    cleaned_order = order.copy()
    
    cleaned_order["status"] = normalize_status(order["status"])
    cleaned_order["city"] = normalize_city(order["city"])
    cleaned_order["category"] = normalize_category(order["category"])
    cleaned_order["channel"] = normalize_channel(order["channel"])
    
    return cleaned_order    

def calculate_total_amount(order):
    return order["quantity"] * order["price"]

def get_completed_orders(clean_orders):
    completed_orders = []

    for order in clean_orders:
        if order["status"] == "completed":
            completed_orders.append(order)
    return completed_orders

def calculate_completed_revenue(clean_orders):
    revenue = 0

    completed_orders = get_completed_orders(clean_orders)

    for order in completed_orders:
        revenue += calculate_total_amount(order)
    return revenue

def count_non_revenue_orders(clean_orders):
    count = 0

    for order in clean_orders:
        if order["status"] in ["pending", "cancelled", "returned"]:
            count += 1

    return count    

def average_completed_order_value(clean_orders):
    completed_orders = get_completed_orders(clean_orders)

    if len(completed_orders) == 0:
        return 0
    revenue = calculate_completed_revenue(clean_orders)
    return revenue / len(completed_orders)

def get_highest_completed_order(clean_orders):
    completed_orders = get_completed_orders(clean_orders)

    if len(completed_orders) == 0:
        return None
    
    highest = completed_orders[0]

    for order in completed_orders:
        if calculate_total_amount(order) > calculate_total_amount(highest):
            highest = order
    return highest

def get_lowest_completed_order(clean_orders):
    completed_orders = get_completed_orders(clean_orders)

    if len(completed_orders) == 0:
        return None

    lowest = completed_orders[0]

    for order in completed_orders:
        if calculate_total_amount(order) < calculate_total_amount(lowest):
            lowest = order

    return lowest

def count_by_field(records, field_name):
    counts = {}

    for record in records:
        value = record[field_name]

        if value not in counts:
            counts[value] = 0

        counts[value] += 1

    return counts

def sum_revenue_by_field(records, field_name):
    revenue = {}

    completed_orders = get_completed_orders(records)

    for order in completed_orders:
        value = order[field_name]
        amount = calculate_total_amount(order)

        if value not in revenue:
            revenue[value] = 0

        revenue[value] += amount

    return revenue

def get_customers_with_multiple_orders(records):
    customer_counts = {}

    for order in records:
        customer = order["customer_name"]

        if customer not in customer_counts:
            customer_counts[customer] = 0

        customer_counts[customer] += 1

    multiple_orders = {}

    for customer, count in customer_counts.items():
        if count > 1:
            multiple_orders[customer] = count

    return multiple_orders

def get_products_ordered_more_than_once(records):
    product_counts = {}

    for order in records:
        product = order["product"]

        if product not in product_counts:
            product_counts[product] = 0

        product_counts[product] += 1


    repeated_products = {}

    for product, count in product_counts.items():
        if count > 1:
            repeated_products[product] = count

    return repeated_products

def get_top_orders_by_total_amount(records, limit):
    completed_orders = get_completed_orders(records)

    orders_with_total = []

    for order in completed_orders:
        new_order = order.copy()
        new_order["total_amount"] = calculate_total_amount(order)
        orders_with_total.append(new_order)

    sorted_orders = sorted(
        orders_with_total,
        key=lambda order: order["total_amount"],
        reverse=True
    )

    return sorted_orders[:limit]

def sort_dictionary(data, limit):
    sorted_data = sorted(
        data.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_data[:limit]

def write_business_report(clean_orders, valid_orders, invalid_orders):
    with open("output/business_report.txt", "w") as file:

        file.write("BUSINESS REPORT\n")
        file.write("====================\n\n")

        file.write(f"Raw records: {len(orders)}\n")
        file.write(f"Valid records: {len(valid_orders)}\n")
        file.write(f"Invalid records: {len(invalid_orders)}\n\n")


        file.write("Completed Revenue:\n")
        file.write(str(calculate_completed_revenue(clean_orders)))
        file.write("\n\n")


        file.write("Top 5 Orders:\n")

        top_orders = get_top_orders_by_total_amount(clean_orders,5)

        for order in top_orders:
            file.write(
                f"Order {order['order_id']} - "
                f"{order['product']} - "
                f"{calculate_total_amount(order)}\n"
            )


        file.write("\n\nTop Customers by Revenue:\n")

        customer_revenue = sum_revenue_by_field(
            clean_orders,
            "customer_name"
        )

        for customer,revenue in sort_dictionary(customer_revenue,3):
            file.write(f"{customer}: {revenue}\n")


        file.write("\n\nTop Products by Revenue:\n")

        product_revenue = sum_revenue_by_field(
            clean_orders,
            "product"
        )

        for product,revenue in sort_dictionary(product_revenue,3):
            file.write(f"{product}: {revenue}\n")


        file.write("\n\nTop Cities by Revenue:\n")

        city_revenue = sum_revenue_by_field(
            clean_orders,
            "city"
        )

        for city,revenue in sort_dictionary(city_revenue,3):
            file.write(f"{city}: {revenue}\n")


        file.write("\n\nCategories by Revenue:\n")

        category_revenue = sum_revenue_by_field(
            clean_orders,
            "category"
        )

        for category,revenue in sort_dictionary(
            category_revenue,
            len(category_revenue)
        ):
            file.write(f"{category}: {revenue}\n")


        file.write("\n\nChannels by Revenue:\n")

        channel_revenue = sum_revenue_by_field(
            clean_orders,
            "channel"
        )

        for channel,revenue in sort_dictionary(
            channel_revenue,
            len(channel_revenue)
        ):
            file.write(f"{channel}: {revenue}\n")


       
def main():

    print("Raw records:", len(orders))

    print("\nFirst 3 raw records:")
    for order in orders[:3]:    
        print(order)
    
    valid_orders, invalid_orders = split_valid_and_invalid_orders(orders)
    clean_orders = []
    for order in valid_orders:
        clean_orders.append(clean_order(order))

    print("Clean orders:", len(clean_orders))
    print(clean_orders[:3])



    print("\nOrders by status:")
    print(count_by_field(clean_orders, "status"))

    print("\nOrders by city:")
    print(count_by_field(clean_orders, "city"))

    print("\nRevenue by category:")
    print(sum_revenue_by_field(clean_orders, "category"))

    print("\nRevenue by customer:")
    print(sum_revenue_by_field(clean_orders, "customer_name"))

    print("\nCustomers with multiple orders:")
    print(get_customers_with_multiple_orders(clean_orders))

    print("\nRepeated products:")
    print(get_products_ordered_more_than_once(clean_orders))

    print("\nTop 5 Orders:")

    top_orders = get_top_orders_by_total_amount(clean_orders,5)

    for order in top_orders:
        print(
            order["order_id"],
            order["product"],
            order["total_amount"]
    )



    statuses = []
    cities = []
    categories = []
    channels = []

    for order in orders:
        if order["status"] not in statuses:
            statuses.append(order["status"])

        if order["city"] not in cities:
            cities.append(order["city"])

        if order["category"] not in categories:
            categories.append(order["category"])

        if order["channel"] not in channels:
            channels.append(order["channel"])

    print("\nUnique Statuses:", statuses)
    print("Unique Cities:", cities)
    print("Unique Categories:", categories)
    print("Unique Channels:", channels)

    
    completed_orders = get_completed_orders(clean_orders)
    print("Completed orders:",len(completed_orders))
    print("\nValid Orders:", len(valid_orders))
    print("Invalid Orders:", len(invalid_orders))
    
    completed_orders = get_completed_orders(clean_orders)

    print("Completed orders:", len(completed_orders))
    print("Completed revenue:", calculate_completed_revenue(clean_orders))
    print("Average order value:", average_completed_order_value(clean_orders))

    print("Highest order:", get_highest_completed_order(clean_orders))
    print("Lowest order:", get_lowest_completed_order(clean_orders))


    print("\nInvalid Records:")
    for record in invalid_orders:
        print(f"Order ID: {record['order']['order_id']}")
        print("Reasons:")
        for reason in record["reasons"]:
            print("-", reason)
        print()

    write_invalid_records(invalid_orders)
    write_validation_report(valid_orders, invalid_orders)
    write_business_report(
    clean_orders,
    valid_orders,
    invalid_orders
    )



if __name__ == "__main__":
    main()  