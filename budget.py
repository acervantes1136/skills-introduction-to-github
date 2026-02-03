"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float).
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""

# User Enters Monthly Income
monthly_income = float(input("Enter Monthly Income (no commas): $"))

# User Monthly Expenses
expenses = []
expense_names = ["Savings", "Gas", "Credit Card(s)", "Groceries", "Other"]

for name in expense_names:
    amount = float(input(f"Enter amount for {name} expenses (no commas): $"))
    expenses.append(amount)

# Total Expenses and Remaining Balance
total_expenses = sum(expenses)
remaining_balance = monthly_income - total_expenses

# Percentage of Income Spent
percentage_spent = (total_expenses / monthly_income) * 100

# Output
print("\n   Monthly Income Summary   ")
print(f"Total Monthly Income: ${monthly_income:,.2f}")
print(f"Total Monthly Expenses: ${total_expenses:,.2f}")
print(f"Remaining Balance: ${remaining_balance:,.2f}")
print(f"Percentage of Income Spent: {percentage_spent:.2f}%")
