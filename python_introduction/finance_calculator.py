income = input("Enter your monthly income: ")
expenses = input("Enter your total monthly expenses: ")

savings = float(income) - float(expenses)

interest = 0.05

projected_savings = savings * 12 + (savings * interest * 12)

print(f"Your monthly savings are ${int(savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
