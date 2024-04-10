from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(choice):
    for ingredient in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}. :(")
            return False
    return True


def process_coins():
    """Returns total amount of money from inserted coins."""
    print("Please insert coins.")
    quarters = float(input("Insert quarters: "))
    dimes = float(input("Insert dimes: "))
    nickles = float(input("Insert nickles: "))
    pennies = float(input("Insert pennies: "))
    return 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies


def check_cost(choice, money):
    """Takes user's coffee choice and inserted amount of money as parameter. Compares money against cost of chosen
    drink. Returns 'False' if user does not have enough money. Otherwise, it returns change and adds cost of the
    drink to machine's resources checking if there was already any drink bought. """

    cost = MENU[choice]["cost"]

    if cost > money:
        print("Sorry, not enough money. Coins refunded.")
        return False
    elif cost < money:
        print(f"Here is your ${round(money - cost, 2)} in change.")

    return True


def make_coffee(choice):
    coffee = MENU[choice]

    for ingredient in coffee["ingredients"]:
        resources[ingredient] -= coffee["ingredients"][ingredient]

    if "money" not in resources:
        resources["money"] = coffee["cost"]
    else:
        resources["money"] += coffee["cost"]


def coffee_machine():
    flag = True
    while flag:
        prompt = input("What would you like? (espresso/latte/cappuccino): ")
        if prompt == "off":
            flag = False
        elif prompt != "espresso" and prompt != "latte" and prompt != "cappuccino" and prompt != "report":
            print("No such an option. Try again.")
        elif prompt == "report":
            for resource in resources:
                print(f"{resource}: {resources[resource]}")
        else:
            if check_resources(prompt):
                credit = process_coins()
                if check_cost(prompt, credit):
                    make_coffee(prompt)
                print(f"Here is your {prompt}. Enjoy!")

    print("Turning off the machine...")


coffee_machine()
