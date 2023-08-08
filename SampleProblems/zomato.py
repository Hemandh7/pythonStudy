dish_menu = {}
order_records = {}
order_counter = 1

def add_dish_to_menu(dish_id, dish_name, dish_price, dish_availability):
    dish_menu[dish_id] = {"name": dish_name, "price": dish_price, "availability": dish_availability}

def remove_dish_from_menu(dish_id):
    if dish_id in dish_menu:
        del dish_menu[dish_id]

def update_dish_availability(dish_id, new_availability):
    if dish_id in dish_menu:
        dish_menu[dish_id]["availability"] = new_availability

def place_new_order(customer_name, chosen_dish_ids):
    valid_dish_ids = []
    for dish_id in chosen_dish_ids:
        if dish_id in dish_menu and dish_menu[dish_id]["availability"] == "yes":
            valid_dish_ids.append(dish_id)

    if not valid_dish_ids:
        print("No valid dishes found. Order not placed.")
        return

    global order_counter
    order_id = order_counter
    order_counter += 1
    order_records[order_id] = {"customer_name": customer_name, "chosen_dish_ids": valid_dish_ids, "status": "received"}

def update_order_status(order_id, new_status):
    if order_id in order_records:
        order_records[order_id]["status"] = new_status

def list_orders_by_status(status_filter=None):
    for order_id, order in order_records.items():
        if status_filter is None or order["status"] == status_filter:
            print(f"Order ID: {order_id}, Customer: {order['customer_name']}, Status: {order['status']}")

def save_data_to_files():
    with open("menu.txt", "w") as menu_file:
        for dish_id, dish in dish_menu.items():
            menu_file.write(f"{dish_id},{dish['name']},{dish['price']},{dish['availability']}\n")

    with open("orders.txt", "w") as orders_file:
        for order_id, order in order_records.items():
            chosen_dish_ids = ",".join(order["chosen_dish_ids"])
            orders_file.write(f"{order_id},{order['customer_name']},{chosen_dish_ids},{order['status']}\n")

def load_data_from_files():
    try:
        with open("menu.txt", "r") as menu_file:
            for line in menu_file:
                dish_id, dish_name, dish_price, dish_availability = line.strip().split(',')
                add_dish_to_menu(dish_id, dish_name, float(dish_price), dish_availability)

        with open("orders.txt", "r") as orders_file:
            for line in orders_file:
                order_id, customer_name, chosen_dish_ids, status = line.strip().split(',')
                chosen_dish_ids = chosen_dish_ids.split(',')
                order_records[int(order_id)] = {"customer_name": customer_name, "chosen_dish_ids": chosen_dish_ids, "status": status}
    except FileNotFoundError:
        pass

def calculate_total_price(chosen_dish_ids):
    total_price = 0
    for dish_id in chosen_dish_ids:
        if dish_id in dish_menu:
            total_price += dish_menu[dish_id]["price"]
    return total_price
    

def main():
    load_data_from_files()

    while True:
        print("\nZesty Zomato - Main Menu")
        print("1. Add Dish to Menu")
        print("2. Remove Dish from Menu")
        print("3. Update Dish Availability")
        print("4. Place New Order")
        print("5. Update Order Status")
        print("6. List Orders")
        print("7. List Orders by Status")
        print("8. Calculate Total Price")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            dish_id = input("Enter Dish ID: ")
            dish_name = input("Enter Dish Name: ")
            dish_price = float(input("Enter Dish Price: "))
            dish_availability = input("Is the Dish Available (yes/no): ")
            add_dish_to_menu(dish_id, dish_name, dish_price, dish_availability)
        elif choice == "2":
            dish_id = input("Enter Dish ID to remove: ")
            remove_dish_from_menu(dish_id)
        elif choice == "3":
            dish_id = input("Enter Dish ID to update availability: ")
            new_availability = input("Is the Dish Available (yes/no): ")
            update_dish_availability(dish_id, new_availability)
        elif choice == "4":
            customer_name = input("Enter Customer Name: ")
            chosen_dish_ids = input("Enter Dish IDs (comma-separated): ").split(',')
            place_new_order(customer_name, chosen_dish_ids)
        elif choice == "5":
            order_id = int(input("Enter Order ID to update status: "))
            new_status = input("Enter New Status: ")
            update_order_status(order_id, new_status)
        elif choice == "6":
            list_orders_by_status()
        elif choice == "7":
            status_filter = input("Enter Status to filter: ")
            list_orders_by_status(status_filter)
        elif choice == "8":
            chosen_dish_ids = input("Enter Dish IDs for calculating total price (comma-separated): ").split(',')
            total_price = calculate_total_price(chosen_dish_ids)
            print(f"Total Price: {total_price}")
        elif choice == "9":
            save_data_to_files()
            print("Exiting Zesty Zomato. Have a tasty day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
