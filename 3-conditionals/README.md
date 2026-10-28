# Shipping Cost

[Version française](README.fr.md)

A command-line shipping cost calculator, like on an online shop. You enter the package weight, the cart total, the destination and the express option, and the program prints the invoice with the estimated delivery time.

Project 3 of my **Python Basics** series, about **conditionals**.

## Shipping rules

- **Base price by destination**: France 4.99 €, Europe 9.99 €, World 19.99 €
- **Weight surcharge**: free up to 1 kg, +3 € up to 5 kg, +7 € up to 10 kg, +15 € above
- **Free shipping** from 50 € in France and from 100 € in Europe
- **Express option**: +5.90 € in France and Europe, +14.90 € for the rest of the world
- **Delivery time**: France 2 to 3 days (24 hours express), Europe 4 to 6 days (2 days express), World 7 to 14 days (4 days express)
- Packages over 30 kg are refused

If the cart is below the free shipping amount, the program tells you how much is missing.

## Example

```text
Package weight (kg): 12
Cart total (€): 80
Destination (France, Europe or World): europe
Express shipping? (yes/no): no

====================================
Shipping invoice
====================================
  Destination: Europe
  Package weight: 12.0 kg
  Shipping: Standard
  Estimated delivery: 4 to 6 days
------------------------------------
  Cart: 80.0 €
  Standard shipping: 24.99 €
------------------------------------
  TOTAL: 104.99 €
====================================
Tip: add 20.0 € to your cart to get free shipping.
```

## How to run

You need Python 3.10 or newer (for `match`), nothing to install.

```bash
git clone https://github.com/jeansys1/python-basics.git
cd python-basics/3-conditionals
python3 shipping_cost.py
```

## What I learned

- Making decisions with `if`, `elif` and `else`
- Comparing values with `<`, `<=`, `>`, `>=` and `==`
- Combining conditions with `and` and `or`
- Choosing between several values with `match` and `case`, and grouping cases with `|` (`case "france" | "europe"`)
- Writing functions that return `True` or `False`, like `is_valid_zone()` and `is_free_shipping()`
- Checking the input before calculating: package too heavy or unknown destination

## Ideas for improvement

- **Loops**: ask again until the destination is valid, or order several packages
- **Exceptions**: ask again when the input is not a number

## Python Basics series

1. Variables: [Monthly Budget](../1-variables)
2. Functions: [Trip Cost](../2-functions)
3. **Conditionals: Shipping Cost** (this project)
4. Loops: coming soon
5. Exceptions: coming soon
