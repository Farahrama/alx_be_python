monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your monthly expenses: ")
monthly_savings = float(monthly_income) - float(monthly_expenses)
projected_savings = int(monthly_savings) * 12 + (int(monthly_savings) * 12 * 0.05)

print(f"Your monthly savings are {monthly_savings}.")
print(f"Projected savings after one year, with interest, is: {projected_savings}.")