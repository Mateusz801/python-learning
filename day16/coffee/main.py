from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    coffe_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    while True:
        choice = input(f"What would you like? ({menu.get_items()}) ")
        if choice == "report":
            coffe_maker.report()
            money_machine.report()
        elif choice == "off":
            break
        else:
            order = menu.find_drink(choice)
            if coffe_maker.is_resource_sufficient(order):
                if money_machine.make_payment(order.cost):
                    coffe_maker.make_coffee(order)


coffee_machine()
