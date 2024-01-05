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

category_totals = {}

# Loop through items and add the amounts to the respective categories in category_totals
for item in items:
    category = item[0]
    amount = item[1]
    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount

# Print the results
for category, total in category_totals.items():
    print(category + ": $" + str(round(total, 2)))
