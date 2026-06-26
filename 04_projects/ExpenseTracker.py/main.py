print("===== Expense Tracker =====")
print("1. Add Expense")
print("2. Total Spending")
print("3. Highest Expense")

expenses = []

while True:
    category = input("Enter category: ")
    amount = float(input("Enter amount: ₹"))

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    choice = input("Add another expense? (y/n): ")

    if choice.lower() == "n":
        break

print("\nYour Expenses:")
for expense in expenses:
    print(f"{expense['category']} : ₹{expense['amount']}")

print("\nExpenses:")

total = 0

for expense in expenses:
    print(f"{expense['category']} : ₹{expense['amount']}")
    total += expense["amount"]

print(f"\nTotal Spending: ₹{total}")


for expense in expenses:
    print(f"{expense['category']} : ₹{expense['amount']}")

if len(expenses) > 0:
    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print("\n===== Highest Expense =====")
    print(f"{highest['category']} : ₹{highest['amount']}")

