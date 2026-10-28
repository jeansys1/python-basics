# Monthly Budget

[Version française](README.fr.md)

A command-line personal budget calculator. You enter your income and expenses for the month, and the program prints a summary: money left, budget per day, projection over a year and recommended savings.

Project 1 of my **Python Basics** series, about **variables**.

## Features

- Enter your salary, other income and 5 expenses (rent, groceries, transport, subscriptions, leisure)
- Amounts can be typed with a comma (`320,10`) or a dot (`320.10`)
- Share of each expense in your income, as a percentage
- Money left, budget per day and projection over 12 months
- Recommended savings based on the 50/30/20 rule (20% of income)

## Example

```text
====================================
Jean's budget for November
====================================
INCOME
  Net salary: 2100.0 €
  Other income: 150.0 €
  Total: 2250.0 €
------------------------------------
EXPENSES
  Rent: 750.0 € (33.3% of income)
  Groceries: 320.1 € (14.2% of income)
  Transport: 75.2 € (3.3% of income)
  Subscriptions: 45.0 € (2.0% of income)
  Leisure: 180.0 € (8.0% of income)
  Total: 1370.3 € (60.9% of income)
------------------------------------
SUMMARY
  Money left: 879.7 €
  Per day: 29.32 €
  Over 12 months: 10556.4 €
  Recommended savings (20%): 450.0 €
  Balanced budget: True
====================================
```

## How to run

You only need Python 3, nothing to install.

```bash
git clone https://github.com/jeansys1/python-basics.git
cd python-basics/1-variables
python3 monthly_budget.py
```

## What I learned

- Creating variables with clear names (`money_left`, `budget_per_day`, etc.)
- The basic types: `str` (the name), `float` (the amounts), `int` (the constants `DAYS_PER_MONTH` and `MONTHS_PER_YEAR`) and `bool` (`balanced_budget`)
- Converting user input with `float()`, because `input()` always returns text
- Doing calculations with `+`, `-`, `*`, `/` and rounding with `round()`
- Using constants, written in capital letters
- Using string methods: `strip()`, `title()`, `replace()`
- Printing results with f-strings

## Ideas for improvement

This project only uses variables. The next projects in the series will teach me how to improve it:

- **Functions**: avoid repeating the same lines for each expense
- **Conditionals**: show a warning when the budget is in the red
- **Loops**: enter as many expenses as you want
- **Exceptions**: ask again when the input is not a number

## Python Basics series

1. **Variables: Monthly Budget** (this project)
2. Functions: [Trip Cost](../2-functions)
3. Conditionals: [Shipping Cost](../3-conditionals)
4. Loops: [Python Quiz](../4-loops)
5. Exceptions: coming soon
