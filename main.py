from machine import MENU, resources


# Initialize machine on startup
off = False
money = 0.0


# Prompt user espresso/latte/cappuccino
def prompt():
    return input("What would you like? (espresso/latte/cappuccino): ")


def check_input(input):
    print("hold")


while not off:

    user_input = prompt()

    if user_input == "off":
        off = True
    elif user_input == "report":
        for key in resources:
            print(f"{key}: {resources[key]}")
        print(f"Money: ${money}")
