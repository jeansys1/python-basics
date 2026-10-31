# Trip Cost

[Version française](README.fr.md)

A command-line car trip calculator. You enter the distance, the car's fuel consumption, the fuel price, the tolls and the number of passengers, and the program prints the cost of the trip, the cost per person, the travel time and the CO2 emitted.

Handy to know how much everyone should pay when carpooling.

Project 2 of my **Python Basics** series, about **functions**.

## Features

- Fuel used and fuel cost
- Total cost one way and round trip, and cost per person
- Travel time on roads (90 km/h) and on the highway (110 km/h)
- CO2 emitted in total and per person
- Numbers can be typed with a comma (`6,5`) or a dot (`6.5`)

## Example

```text
====================================
Trip from Paris to Lyon
====================================
  Distance: 465.0 km
  Fuel used: 30.2 L
  Time on roads (90 km/h): 5 h 10 min
  Time on highway (110 km/h): 4 h 14 min
------------------------------------
COST
  Fuel: 55.92 €
  Tolls: 38.5 €
  One way: 94.42 €
  One way per person: 31.47 €
  Round trip: 188.83 €
  Round trip per person: 62.94 €
------------------------------------
ENVIRONMENT
  CO2 emitted: 69.5 kg
  CO2 per person: 23.2 kg
====================================
```

## How to run

You only need Python 3, nothing to install.

```bash
git clone https://github.com/jeansys1/python-basics.git
cd python-basics/2-functions
python3 trip_cost.py
```

## The functions

- `main()`: the main program, which asks for the information and prints the summary
- `ask_number(question)`: asks a question and returns the answer as a number
- `calculate_liters(distance, consumption)`: liters of fuel used
- `calculate_fuel_cost(liters, fuel_price)`: cost of the fuel
- `calculate_co2(liters, kg_per_liter=2.3)`: CO2 emitted
- `per_person(total, people)`: splits a total between the passengers
- `calculate_duration(distance, speed=90)`: travel time in minutes
- `format_duration(minutes)`: turns `310` into `"5 h 10 min"`

## What I learned

- Creating my own functions with `def`
- Giving parameters to a function and returning a result with `return`
- Giving a parameter a default value: `calculate_duration(distance)` uses 90 km/h, `calculate_duration(distance, 110)` uses 110 km/h
- Reusing the same function for different things: `per_person()` splits both the money and the CO2
- Avoiding repeated code: `ask_number()` replaces the same line four times
- Organizing a program with a `main()` function
- Converting minutes into hours with `int()`

## Ideas for improvement

- **Conditionals**: refuse a negative distance or 0 passengers
- **Loops**: add several stops to the trip
- **Exceptions**: ask again when the input is not a number

## Python Basics series

1. Variables: [Monthly Budget](../1-variables)
2. **Functions: Trip Cost** (this project)
3. Conditionals: [Shipping Cost](../3-conditionals)
4. Loops: [Python Quiz](../4-loops)
5. Exceptions: [Grade Book](../5-exceptions)
