inventory = 0
failed_entries = 0
deliveries_processed = 0


def get_valid_input():
    stock = input("Enter stock quantity (or type 'quit' to exit): ")

    if stock.lower() == "quit":
        return "quit"

    if not stock.isdigit():
        print("Error: Invalid input. Please enter a whole number.")
        return None

    stock = int(stock)

    if stock < 0:
        print("Error: Negative numbers are not allowed.")
        return None

    return stock


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print("\n--- Final Report ---")
    print("Total Units Processed:", total_units)
    print("Total Deliveries Processed:", deliveries_processed)
    print("Number of Failed/Rejected Entries:", failed_attempts)


while True:
    stock = get_valid_input()

    if stock == "quit":
        break

    if stock is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, stock)

    tax = calculate_tax(stock)
    print("Tax for this delivery:", tax)

    deliveries_processed += 1

    if inventory > 500:
        print("ALERT: Overstock! Inventory exceeds 500 units.")
        break


generate_report(inventory, failed_entries)