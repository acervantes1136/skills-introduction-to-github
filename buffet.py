"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator
DATE: 02/02/2026
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask user for their age (convert to int).
2. Use if/elif/else to determine price:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Print the final price formatted as currency (e.g., $16.95).
-----------------------------------------------------------------------
"""

# Ask user for their age
age = int(input("Enter age here: "))

# Buffet Totals
if age < 1:
    print(f"FREE ($0.00)")
elif age < 11:
    amount = 1.00
    payment = age * amount
    print(f"Total: ${payment:.2f}")
elif age < 64:
    print(f"Total: $16.95")
else:
    print(f"Total: $12.95")
