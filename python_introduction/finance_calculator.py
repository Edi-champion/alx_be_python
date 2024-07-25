#!/usr/bin/python3


month_income = float(input("Enter your monthly income: "))
month_expenses = float(input("Enter your total monthly expenses: "))

#Calculate monthly Savings

month_sav = month_income - month_expenses

#Project ANNUAL savings

pject_saviings = ((month_sav*12)+ month_sav*12*0.05)

#Display results

print (f"Your monthly savings are ${month_sav}.")
print(f"Projected savings after one year, with interest, is:${pject_saviings}")


