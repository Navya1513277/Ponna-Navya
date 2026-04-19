menu = {
    "Beverages": {
        "Coffee": 80,
        "Tea": 50,
        "Cold Coffee": 120
    },    
    "Juices & Milkshakes": {
        "Rose Milk": 120,
        "Badam Milk": 140,
        "Chocolate Milkshake": 150,
        "Fresh Fruit Mix": 90
    },
    "Snacks & Fast Food": {
        "Sandwich (Veg/Grilled)": 125,
        "Burger": 120,
        "French Fries": 80,
        "Pizza": 150,
        "Pasta": 180,
        "Puff (veg/Non-veg)": 60
    },    
    "Desserts": {
        "Ice Cream": 70,
        "Cake Slice": 90
    }
}

print("Welcome to our HELLO_CAFE")
print("--------HELLO_CAFE MENU-------")

# Display menu
for category, items in menu.items():
    print(f"\n...{category}...")
    for item, price in items.items():
        print(f"{item}: ₹{price}")

order_total = 0

# First item
order_item = input("\nEnter your item: ")
found = False

for category in menu:
    if order_item in menu[category]:
        order_total += menu[category][order_item]
        found = True
        break

if not found:
    print("You entered a wrong item ")
else:
    order = input("Do you want anything else (yes/no): ")
    if order.lower() == 'yes':
        order_item2 = input("Enter your second item: ")
        found2 = False

        for category in menu:
            if order_item2 in menu[category]:
                order_total += menu[category][order_item2]
                found2 = True
                break

        if not found2:
            print("Second item not found ")

    print(f"Your total order value is ₹{order_total}")