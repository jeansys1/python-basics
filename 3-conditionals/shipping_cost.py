# Shipping Cost
# Project 3 of my "Python Basics" series: conditionals
#
# The program calculates the shipping cost of an order based on
# the package weight, the destination, the cart total and the express option.

# Constants (in capital letters because their value never changes)
MAX_WEIGHT = 30              # we don't ship packages over 30 kg
FREE_SHIPPING_FRANCE = 50    # free shipping in France from 50 €
FREE_SHIPPING_EUROPE = 100   # free shipping in Europe from 100 €


def main():
    print("=========== SHIPPING COST ===========")
    print("(numbers with a comma or a dot)")
    print()

    weight = ask_number("Package weight (kg): ")
    cart = ask_number("Cart total (€): ")
    zone = input("Destination (France, Europe or World): ").strip().lower()
    express = ask_yes_no("Express shipping? (yes/no): ")

    # Check the order before calculating anything
    print()
    if weight <= 0 or weight > MAX_WEIGHT:
        print(f"Sorry, we only ship packages from 0 to {MAX_WEIGHT} kg.")
    elif is_valid_zone(zone):
        print_invoice(weight, cart, zone, express)
    else:
        print("Sorry, unknown destination: choose France, Europe or World.")


def print_invoice(weight, cart, zone, express):
    # ----- Calculations -----
    free = is_free_shipping(cart, zone)
    if free:
        standard_cost = 0
    else:
        standard_cost = base_price(zone) + weight_surcharge(weight)

    if express:
        express_cost = express_surcharge(zone)
        mode = "Express"
    else:
        express_cost = 0
        mode = "Standard"

    total = cart + standard_cost + express_cost

    # ----- Invoice -----
    print("====================================")
    print("Shipping invoice")
    print("====================================")
    print(f"  Destination: {zone.title()}")
    print(f"  Package weight: {weight} kg")
    print(f"  Shipping: {mode}")
    print(f"  Estimated delivery: {delivery_time(zone, express)}")
    print("------------------------------------")
    print(f"  Cart: {cart} €")
    if free:
        print("  Standard shipping: free")
    else:
        print(f"  Standard shipping: {round(standard_cost, 2)} €")
    if express:
        print(f"  Express surcharge: {express_cost} €")
    print("------------------------------------")
    print(f"  TOTAL: {round(total, 2)} €")
    print("====================================")

    # A tip when the cart is below the free shipping amount
    if zone == "france" and cart < FREE_SHIPPING_FRANCE:
        print(f"Tip: add {round(FREE_SHIPPING_FRANCE - cart, 2)} € to your cart to get free shipping.")
    elif zone == "europe" and cart < FREE_SHIPPING_EUROPE:
        print(f"Tip: add {round(FREE_SHIPPING_EUROPE - cart, 2)} € to your cart to get free shipping.")


def ask_number(question):
    answer = input(question)
    return float(answer.replace(",", "."))


# Returns True if the person answers "yes" (or "y"), otherwise False
def ask_yes_no(question):
    answer = input(question).strip().lower()
    return answer == "yes" or answer == "y"


def is_valid_zone(zone):
    return zone == "france" or zone == "europe" or zone == "world"


def base_price(zone):
    match zone:
        case "france":
            return 4.99
        case "europe":
            return 9.99
        case "world":
            return 19.99


# The heavier the package, the higher the surcharge
def weight_surcharge(weight):
    if weight <= 1:
        return 0
    elif weight <= 5:
        return 3
    elif weight <= 10:
        return 7
    else:
        return 15


def express_surcharge(zone):
    match zone:
        case "france" | "europe":
            return 5.90
        case "world":
            return 14.90


def is_free_shipping(cart, zone):
    if zone == "france" and cart >= FREE_SHIPPING_FRANCE:
        return True
    elif zone == "europe" and cart >= FREE_SHIPPING_EUROPE:
        return True
    else:
        return False


def delivery_time(zone, express):
    if zone == "france" and express:
        return "24 hours"
    elif zone == "france":
        return "2 to 3 days"
    elif zone == "europe" and express:
        return "2 days"
    elif zone == "europe":
        return "4 to 6 days"
    elif express:
        return "4 days"
    else:
        return "7 to 14 days"


main()
