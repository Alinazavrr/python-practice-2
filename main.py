# A1 - Multi-Item Shopping (while loop)
customer_name = input("Enter customer name: ")
subtotal = 0.0
item_count = 0

while True:
    product_name = input("Enter product name (or 'done' to finish): ")
    if product_name.lower() == "done":
        break

    price = float(input("Enter price: "))
    subtotal += price
    item_count += 1

print(f"Customer : {customer_name.upper()}")
print(f"Items : {item_count}")
print(f"Subtotal : {subtotal} KZT")

# A2 - Tiered Discount (if/elif/else)
print("-" * 30)

if subtotal < 3000:
    discount_tier = "No discount"
    discount_rate = 0.0
elif subtotal < 7000:
    discount_tier = "5% discount"
    discount_rate = 0.05
else:
    discount_tier = "15% discount"
    discount_rate = 0.15

discount = subtotal * discount_rate
total = subtotal - discount

print(f"Discount tier : {discount_tier}")
print(f"Discount : {discount} KZT")
print(f"Total : {total} KZT")

# A3 - Name Analysis (strings)
print(f"Name uppercase : {customer_name.upper()}")
print(f"Name lowercase : {customer_name.lower()}")
print(f"Name length : {len(customer_name)}")

if len(customer_name) > 5:
    print("Long name")
else:
    print("Short name")
