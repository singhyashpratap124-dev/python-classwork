# Inventorty Management System using Python lists

# Nested list containing product details
inventory = [
    [101, "Keyboard", 12, 850.00]
    [102, "Mouse", 4, 450.00]
    [103, "Monitor", 7, 12500.00]
    [104, "Webcam", 3, 1800.00]
    [105, "Headphones", 15, 1200.00]
]

# Read the low-stock limit
stock_limit = int(input("Enter the low-stock limi: "))

low_stock_products = []
total_inventory_value = 0

print("\nInventory Details")
print("-" * 70)
print("ID\tProduct\t\tQuantity\tUnit Price\tStock Value")
print("-" * 70)

# Process every product in the inventory
for product in inventory:
    product_id = product[0]
    product_name = product[1]
    quantity = product[2]
    unit_price = product[3]

    # Calculate the value of the current product
    stock_value = quantity * unit_price
    total_inventory_value = total_inventory_value + stock_value

    print(
        product_id, "\t",
        product_name, "\t\t",
        quantity, "\t\t",
        unit_price, "\t\t",
        stock_vzlue
    )

    # Identify products below the stock limit
    if quantity < stock_limit:
        low_stock    
                        