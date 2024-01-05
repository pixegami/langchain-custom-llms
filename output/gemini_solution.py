# Convert the data into a Python variable called 'items'
items = [
    ("Groceries", 35.20),
    ("Transport", 45.00),
    ("Entertainment", 15.99),
    ("Eating Out", 4.50),
    ("Utilities", 60.00),
    ("Shopping", 85.00),
    ("Groceries", 70.30),
    ("Entertainment", 25.00),
    ("Entertainment", 9.99),
    ("Eating Out", 18.40),
    ("Transport", 50.00),
]

# Create a dictionary to store the sum of expenses for each category
category_totals = {}

# Iterate over the items and add the amount to the corresponding category
for category, amount in items:
    category_totals[category] = category_totals.get(category, 0) + amount

# Print the results
for category, total in category_totals.items():
    print(f"{category}: ${total:.2f}")
