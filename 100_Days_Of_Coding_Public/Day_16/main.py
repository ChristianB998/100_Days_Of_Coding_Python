import coffee_maker
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine_is_online = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()



while coffee_machine_is_online:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")

    if choice == "off":
        coffee_machine_is_online = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)