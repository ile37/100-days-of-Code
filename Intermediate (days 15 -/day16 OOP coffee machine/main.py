from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()

while True:

    cmd = input("What would you like? (espresso/latte/cappuccino): ")
    if cmd == "off":
        break
    elif cmd == "report":
        coffee_maker.report()
    elif cmd == "espresso":
        coffee_maker.make_coffee(menu.find_drink("espresso"))
    elif cmd == "latte":
        coffee_maker.make_coffee(menu.find_drink("latte"))
    elif cmd == "cappuccino":
        coffee_maker.make_coffee(menu.find_drink("cappuccino"))
