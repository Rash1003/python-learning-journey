print("===== Expense Tracker =====")
print("1. Add Expense")
print("2. View Expenses")
print("3. Total Spending")
print("4. Highest Expense")
print("5. Search Category")
print("6. Exit")

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

print("\nExpenses:")
for expense in expenses:
    print(f"{expense['category']} : ₹{expense['amount']}")

    