# Trip Cost
# Project 2 of my "Python Basics" series: functions
#
# The program calculates the cost of a car trip, the cost per person,
# the travel time and the CO2 emitted.


def main():
    print("============ TRIP COST ============")
    print("(numbers with a comma or a dot)")
    print()

    # ----- Input -----
    start = input("From: ").strip().title()
    destination = input("To: ").strip().title()
    distance = ask_number("Distance (km): ")
    consumption = ask_number("Fuel consumption (L/100 km): ")
    fuel_price = ask_number("Fuel price (€/L): ")
    tolls = ask_number("Tolls (€): ")
    passengers = int(input("Number of people in the car: "))

    # ----- Calculations -----
    liters = calculate_liters(distance, consumption)
    fuel_cost = calculate_fuel_cost(liters, fuel_price)
    one_way_cost = fuel_cost + tolls
    round_trip_cost = one_way_cost * 2

    # The same per_person() function works for money and for CO2
    co2 = calculate_co2(liters)
    one_way_share = per_person(one_way_cost, passengers)
    round_trip_share = per_person(round_trip_cost, passengers)
    co2_share = per_person(co2, passengers)

    # Without a 2nd argument, calculate_duration() uses its default speed (90 km/h)
    road_duration = calculate_duration(distance)
    highway_duration = calculate_duration(distance, 110)

    # ----- Summary -----
    print()
    print("====================================")
    print(f"Trip from {start} to {destination}")
    print("====================================")
    print(f"  Distance: {distance} km")
    print(f"  Fuel used: {round(liters, 1)} L")
    print(f"  Time on roads (90 km/h): {format_duration(road_duration)}")
    print(f"  Time on highway (110 km/h): {format_duration(highway_duration)}")
    print("------------------------------------")
    print("COST")
    print(f"  Fuel: {round(fuel_cost, 2)} €")
    print(f"  Tolls: {tolls} €")
    print(f"  One way: {round(one_way_cost, 2)} €")
    print(f"  One way per person: {round(one_way_share, 2)} €")
    print(f"  Round trip: {round(round_trip_cost, 2)} €")
    print(f"  Round trip per person: {round(round_trip_share, 2)} €")
    print("------------------------------------")
    print("ENVIRONMENT")
    print(f"  CO2 emitted: {round(co2, 1)} kg")
    print(f"  CO2 per person: {round(co2_share, 1)} kg")
    print("====================================")


# Asks a question and returns the answer as a number.
# This avoids writing float(input(...).replace(",", ".")) for every input.
def ask_number(question):
    answer = input(question)
    return float(answer.replace(",", "."))


# Fuel consumption is given for 100 km
def calculate_liters(distance, consumption):
    return distance * consumption / 100


def calculate_fuel_cost(liters, fuel_price):
    return liters * fuel_price


# A petrol car emits about 2.3 kg of CO2 per liter of fuel
def calculate_co2(liters, kg_per_liter=2.3):
    return liters * kg_per_liter


def per_person(total, people):
    return total / people


# Returns the travel time in minutes (rounded)
def calculate_duration(distance, speed=90):
    return round(distance / speed * 60)


# Turns minutes into text, for example 310 -> "5 h 10 min"
def format_duration(minutes):
    hours = int(minutes / 60)
    minutes_left = minutes - hours * 60
    return f"{hours} h {minutes_left} min"


main()
