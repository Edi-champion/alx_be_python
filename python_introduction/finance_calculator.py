#!/usr/bin/python3


month_income = float(input("Enter your monthly income: "))
month_expenses = float(input("Enter your total monthly expenses: "))

#Calculate monthly Savings

month_sav = month_income - month_expenses

#Project ANNUAL savings
in_rate = 0.05

pject_saviings = (month_sav*12 +(month_sav*12*in_rate))

#Display results

print (f"Your monthly savings are ${round(month_sav}:,.0f}")
print(f"Projected savings after one year, with interest, is:${round(pject_saviings):,.0f}")

