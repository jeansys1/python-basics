# Monthly Budget
# Project 1 of my "Python Basics" series: variables
#
# The program asks for the month's income and expenses,
# then prints a summary: money left, budget per day,
# projection over a year and recommended savings.

# ----- Constants -----
# Written in capital letters because their value never changes.
CURRENCY = "€"
SAVINGS_RATE = 0.20  # 50/30/20 rule: save 20% of your income
DAYS_PER_MONTH = 30
MONTHS_PER_YEAR = 12

# ----- Input -----
print("========== MONTHLY BUDGET ==========")
print("(amounts with a comma or a dot)")
print()

name = input("Your name: ").strip().title()
month = input("Month: ")

# input() always returns text, so we convert it to a number with float().
# replace(",", ".") turns a comma into a dot, because Python expects a dot.
salary = float(input("Net salary: ").replace(",", "."))
other_income = float(input("Other income: ").replace(",", "."))

rent = float(input("Rent: ").replace(",", "."))
groceries = float(input("Groceries: ").replace(",", "."))
transport = float(input("Transport: ").replace(",", "."))
subscriptions = float(input("Subscriptions: ").replace(",", "."))
leisure = float(input("Leisure: ").replace(",", "."))

# ----- Calculations -----
# round(number, 2) keeps 2 digits after the decimal point.
income = round(salary + other_income, 2)
expenses = round(rent + groceries + transport + subscriptions + leisure, 2)
money_left = round(income - expenses, 2)

budget_per_day = round(money_left / DAYS_PER_MONTH, 2)
yearly_projection = round(money_left * MONTHS_PER_YEAR, 2)
recommended_savings = round(income * SAVINGS_RATE, 2)

# Share of each expense in the income, as a percentage
rent_share = round(rent / income * 100, 1)
groceries_share = round(groceries / income * 100, 1)
transport_share = round(transport / income * 100, 1)
subscriptions_share = round(subscriptions / income * 100, 1)
leisure_share = round(leisure / income * 100, 1)
expenses_share = round(expenses / income * 100, 1)

balanced_budget = money_left >= 0  # a comparison gives True or False (bool)

# ----- Summary -----
print()
print("====================================")
print(f"{name}'s budget for {month}")
print("====================================")

print("INCOME")
print(f"  Net salary: {salary} {CURRENCY}")
print(f"  Other income: {other_income} {CURRENCY}")
print(f"  Total: {income} {CURRENCY}")
print("------------------------------------")

print("EXPENSES")
print(f"  Rent: {rent} {CURRENCY} ({rent_share}% of income)")
print(f"  Groceries: {groceries} {CURRENCY} ({groceries_share}% of income)")
print(f"  Transport: {transport} {CURRENCY} ({transport_share}% of income)")
print(f"  Subscriptions: {subscriptions} {CURRENCY} ({subscriptions_share}% of income)")
print(f"  Leisure: {leisure} {CURRENCY} ({leisure_share}% of income)")
print(f"  Total: {expenses} {CURRENCY} ({expenses_share}% of income)")
print("------------------------------------")

print("SUMMARY")
print(f"  Money left: {money_left} {CURRENCY}")
print(f"  Per day: {budget_per_day} {CURRENCY}")
print(f"  Over 12 months: {yearly_projection} {CURRENCY}")
print(f"  Recommended savings (20%): {recommended_savings} {CURRENCY}")
print(f"  Balanced budget: {balanced_budget}")
print("====================================")
