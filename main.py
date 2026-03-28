# Variant A — Shop Receipt
# Task A2 — Tiered Discount (if/elif/else)

subtotal = float(input("Enter subtotal: "))

if subtotal < 3000:
    discount_rate = 0
    discount_tier = "No discount"
elif subtotal < 7000:
    discount_rate = 0.05
    discount_tier = "5% discount"
else:
    discount_rate = 0.15
    discount_tier = "15% discount"

discount = subtotal * discount_rate
total = subtotal - discount

print("-" * 30)
print(f"Discount tier : {discount_tier}")
print(f"Discount : {discount} KZT")
print(f"Total : {total} KZT")
