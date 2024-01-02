from machine import MENU, resources

# Initialize machine on startup
off = False
money = 0.00


# Prompt user espresso/latte/cappuccino, also used for report and off commands
def prompt():
    return input("What would you like? (espresso/latte/cappuccino): ")


def check_input(input):

    req_water = MENU[input]['ingredients']['water']
    req_coffee = MENU[input]['ingredients']['coffee']
    if 'milk' in MENU[input]['ingredients']:
        req_milk = MENU[input]['ingredients']['milk']

    if req_water > resources['water']:
        print("Not enough water. Make another selection.")
    elif req_coffee > resources['coffee']:
        print("Not enough coffee. Make another selection.")
    elif 'milk' in MENU[input]['ingredients'] and req_milk > resources['milk']:
        print("Not enough milk. Make another selection")
    else:
        resources['water'] -= req_water
        resources['coffee'] -= req_coffee
        if 'milk' in MENU[input]['ingredients']:
            resources['milk'] -= req_milk
    # refund money if no enough resources


def get_coins(quarters, dimes, nickels, pennies):
    print("placeholder")
    # todo logic to collect coins and make sure enough money inserted, refund if too much


while not off:

    user_input = prompt()

    if user_input == "off":
        off = True
    elif user_input == "report":
        for key in resources:
            print(f"{key}: {resources[key]}")
        print(f"Money: ${money:.2f}")
    elif user_input == "espresso":
        check_input("espresso")
    elif user_input == "latte":
        check_input("latte")
    elif user_input == "cappuccino":
        check_input("cappuccino")
    else:
        print("Invalid request. Try again.")
