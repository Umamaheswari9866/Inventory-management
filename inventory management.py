
import json
inventory = {}
try:
    with open('inventory.json', 'r') as file:
        inventory = json.load(file)
except FileNotFoundError:
    pass
def authenticate(username, password):
    return username == 'maheswari' and password == 'ammu'
def create_item(name, quantity, price):
    if name in inventory:
        print("Item exists.")
    else:
        inventory[name] = {'quantity': quantity, 'price': price}
        save_inventory()

def read_item(name):
    if name in inventory:
        print(f"Name: {name}, Quantity: {inventory[name]['quantity']}, Price: {inventory[name]['price']}")
    else:
        print("Item not found.")

def update_item(name, quantity=None, price=None):
    if name in inventory:
        if quantity:
            inventory[name]['quantity'] = quantity
        if price:
            inventory[name]['price'] = price
        save_inventory()
    else:
        print("Item not found.")

def delete_item(name):
    if name in inventory:
        del inventory[name]
        save_inventory()
    else:
        print("Item not found.")

def save_inventory():
    with open('inventory.json', 'w') as file:
        json.dump(inventory, file)
def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if authenticate(username, password)==True:
        while True:
            print("\n1. Create item")
            print("2. Read item")
            print("3. Update item")
            print("4. Delete item")
            print("5. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                name = input("Enter item name: ")
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price: "))
                create_item(name, quantity, price)
            elif choice == '2':
                name = input("Enter item name: ")
                read_item(name)
            elif choice == '3':
                name = input("Enter item name: ")
                quantity = input("Enter new quantity: ")
                price = input("Enter new price: ")
                update_item(name, int(quantity) if quantity else None, float(price) if price else None)
            elif choice == '4':
                name = input("Enter item name: ")
                delete_item(name)
            elif choice == '5':
                print("exit")
                break;
            else:
                print("Invalid choice.")
    else:
        print("Invalid username or password")

if __name__ == "__main__":
    main()
