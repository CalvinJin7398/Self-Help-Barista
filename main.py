from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
Cashier = MoneyMachine()
Maker = CoffeeMaker()

is_on = True
while is_on is True:
    options = menu.get_items()
    choice = input(f"What would you like? {options}:")
    if choice == "off":
        is_on = False
    if choice == "report":
        Maker.report()
        Cashier.report()
    else:
        drink = menu.find_drink(choice)
        if Maker.is_resource_sufficient(drink) and Cashier.make_payment(drink.cost):
                Maker.make_coffee(drink)
