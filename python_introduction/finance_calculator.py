income = input("Enter you monthly income: ")
expenses = input("Enter your total monthly expenses: ")

savings = int(income) - int(expenses)

interest = 0.05

projected_savings = savings * 12 + (savings * interest * 12)

# Your monthly savings are $1000.
# Projected savings after one year, with interest, is: $12600.

print(f"Your monthly savings are ${savings}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")