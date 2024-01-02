from machine import MENU, resources

# Initialize machine on startup
off = False
money = 0.00


# Prompt user espresso/latte/cappuccino, also used for report and off commands
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
        print(f"Money: ${money:.2f}")
    elif user_input == "espresso":
        check_input("espresso")
    elif user_input == "latte":
        check_input("latte")
    elif user_input == "cappuccino":
        check_input("cappuccino")
    else:
        print("Invalid request. Try again.")
