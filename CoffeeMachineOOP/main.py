from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}: ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        current_drink = menu.find_drink(choice)
        if current_drink:
            is_available = coffee_maker.is_resource_sufficient(current_drink)
            if is_available:
                is_process = money_machine.make_payment(current_drink.cost)
                if is_process:
                    coffee_maker.make_coffee(current_drink)
                    is_on = False





