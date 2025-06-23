"""Question 6
● Title: Farm Inventory Management
● Question: Create a dictionary to store the inventory of a small farm. Keys should
be item names (e.g., 'Tractor', 'Plough', 'Seeds'), and values should be their
quantities. Write a function that takes the inventory dictionary and an item name
as input and returns the quantity of that item, or "Item not found" if it doesn't
exist."""
print("      Farm Inventory Management.       ")

# Dictionary for farm inventory
farm_inventory = {
    "Tractor": 10,
    "Plough": 50,
    "Seeds": 568
}

# Function to check quantity
def get_quantity(inventory, item_name):
    return inventory.get(item_name, "Item not found")

# User input
item = input("Enter the item name (e.g., Tractor, Plough, Seeds): ").strip().title()

# Display result
print(f"{item} quantity:", get_quantity(farm_inventory, item))