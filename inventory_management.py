import json
import os

# File to store inventory data
INVENTORY_FILE = 'inventory.txt'

# Load inventory from file
def load_inventory():
    if not os.path.exists(INVENTORY_FILE):
        return {}
    with open(INVENTORY_FILE, 'r') as file:
        return json.load(file)

# Save inventory to file
def save_inventory(inventory):
    with open(INVENTORY_FILE, 'w') as file:
        json.dump(inventory, file)

# Add new item
def add_item(inventory):
    item_id = input("Enter item ID: ")
    name = input("Enter item name: ")
    quantity = int(input("Enter item quantity: "))
    price = float(input("Enter item price: "))
    inventory[item_id] = {"name": name, "quantity": quantity, "price": price}
    print("Item added successfully!")

# View all items
def view_items(inventory):
    if not inventory:
        print("No items in inventory.")
        return
    for item_id, details in inventory.items():
        print(f"ID: {item_id}, Name: {details['name']}, Quantity: {details['quantity']}, Price: ${details['price']}")

# Update item information
def update_item(inventory):
    item_id = input("Enter item ID to update: ")
    if item_id in inventory:
        name = input("Enter new item name: ")
        quantity = int(input("Enter new item quantity: "))
        price = float(input("Enter new item price: "))
        inventory[item_id] = {"name": name, "quantity": quantity, "price": price}
        print("Item updated successfully!")
    else:
        print("Item not found.")

# Delete item
def delete_item(inventory):
    item_id = input("Enter item ID to delete: ")
    if item_id in inventory:
        del inventory[item_id]
        print("Item deleted successfully!")
    else:
        print("Item not found.")

# Main function
def main():
    inventory = load_inventory()
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_item(inventory)
        elif choice == '2':
            view_items(inventory)
        elif choice == '3':
            update_item(inventory)
        elif choice == '4':
            delete_item(inventory)
        elif choice == '5':
            save_inventory(inventory)
            print("Inventory saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
