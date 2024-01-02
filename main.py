from machine import MENU, resources

# Initialize machine on startup
off = False
money = 0.00


# Prompt user espresso/latte/cappuccino, also used for report and off commands
def prompt():
    return input("What would you like? (espresso/latte/cappuccino): ")


def check_input(input, money):

    req_water = MENU[input]['ingredients']['water']
    req_coffee = MENU[input]['ingredients']['coffee']
    if 'milk' in MENU[input]['ingredients']:
        req_milk = MENU[input]['ingredients']['milk']
    req_money = float(MENU[input]['cost'])

    if money >= req_money:

        if req_water > resources['water']:
            print("Not enough water. Make another selection.")
        elif req_coffee > resources['coffee']:
            print("Not enough coffee. Make another selection.")
        elif 'milk' in MENU[input]['ingredients'] and req_milk > resources['milk']:
            print("Not enough milk. Make another selection")
        else:
            # Remove machine resources per order
            resources['water'] -= req_water
            resources['coffee'] -= req_coffee

            if 'milk' in MENU[input]['ingredients']:
                resources['milk'] -= req_milk

            # Refund surplus money to customer, add required amount to resources
            if money > req_money:
                print(f"Here is ${money - req_money:.2f} in change.")

            resources['money'] += float(req_money)
            print(f"Enjoy your {input}!")
    else:
        print("Sorry that's not enough money. Money refunded")


def get_coins():

    quarters = float(input("How many quarters: "))
    dimes = float(input("How many dimes: "))
    nickels = float(input("How many nickels: "))
    pennies = float(input("How many pennies: "))

    return (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)


while not off:

    user_input = prompt()

    if user_input == "off":
        off = True
    elif user_input == "report":
        print()
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']:.2f}")
        print()
    elif user_input == "espresso":
        user_money = get_coins()
        check_input("espresso", user_money)
    elif user_input == "latte":
        user_money = get_coins()
        check_input("latte", user_money)
    elif user_input == "cappuccino":
        user_money = get_coins()
        check_input("cappuccino", user_money)
    else:
        print("Invalid request. Try again.")
