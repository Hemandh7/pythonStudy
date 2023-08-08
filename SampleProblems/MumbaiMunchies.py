snacks = []
salesrecord = {}

def addsnack(snackid, name, price, availability):
    snacks.append({'id': snackid, 'name': name, 'price': price, 'availability': availability})

def removesnack(snackid):
    for snack in snacks:
        if snack['id'] == snackid:
            snacks.remove(snack)
            break

def updateavailability(snackid, availability):
    for snack in snacks:
        if snack['id'] == snackid:
            snack['availability'] = availability
            break

def makesale(snackid):
    for snack in snacks:
        if snack['id'] == snackid:
            if snack['availability'] == 'yes':
                if snackid in salesrecord:
                    salesrecord[snackid] += 1
                else:
                    salesrecord[snackid] = 1
                snack['availability'] = 'no'
                break
            else:
                print("Snack is unavailable.")
    else:
        print("Snack not found.")

def main():
    while True:
        print("\nCanteen Management System")
        print("1. Add Snack")
        print("2. Remove Snack")
        print("3. Update Availability")
        print("4. Make Sale")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            snackid = input("Enter Snack ID: ")
            name = input("Enter Snack Name: ")
            price = float(input("Enter Price: "))
            availability = input("Is the snack available? (yes/no): ")
            addsnack(snackid, name, price, availability)

        elif choice == "2":
            snackid = input("Enter Snack ID to remove: ")
            removesnack(snackid)

        elif choice == "3":
            snackid = input("Enter Snack ID to update availability: ")
            availability = input("Update availability (yes/no): ")
            updateavailability(snackid, availability)

        elif choice == "4":
            snackid = input("Enter Snack ID for sale: ")
            makesale(snackid)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
