from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cashier = MoneyMachine()
maker = CoffeeMaker()
menu =Menu()

while True:
    drink = input('What would you like to drink' +' ' + menu.get_items() + ':')
    order = menu.find_drink(drink)
    available = maker.is_resource_sufficient(order)
    if not available:

        if drink == 'report':
            maker.report()
            cashier.report()
        elif drink == 'off':
            exit()
        else:
            print('Drink not in the menu')
            
    else:
        payment = cashier.make_payment(order.cost)
        available= False
                
        if payment:
            maker.make_coffee(order)
        else:
            print('payment not proceed')
