from menu import Menu
# from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def run_coffee_machine():
    menu = Menu()
    # menu_item = MenuItem()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    def input_response():
        """Returns the user response for the choice of drink"""
        resp = input(f"What would you like? {menu.get_items()}: ")
        if resp not in ['espresso', 'latte', 'cappuccino', 'report', 'off']:
            resp = input(f"What would you like? {menu.get_items()}: ")
        return resp

    def handle_drink(a_drink):
        """Gets the money made from each transaction and updates the resources """
        if coffee_maker.is_resource_sufficient(a_drink) and money_machine.make_payment(a_drink.cost):
            coffee_maker.make_coffee(a_drink)

# start of the routine
    response = input_response()
    while response:
        if response == 'off':
            return
        elif response == 'report':
            coffee_maker.report()
            response = input_response()
        else:
            drink = menu.find_drink(response)
            handle_drink(drink)
            response = input_response()


run_coffee_machine()

# def run_coffee_machine():
#     money = 0
#
#     def input_response():
#         """Returns the user response for the choice of drink"""
#         resp = input("What would you like? (espresso/latte/cappuccino): ").lower()
#         if resp not in ['espresso', 'latte', 'cappuccino', 'report', 'off']:
#             resp = input("What would you like? (espresso/latte/cappuccino): ").lower()
#         return resp
#
#     def handle_drink(drink):
#         """ Returns the money made from each transaction """
#
#         print("Please insert coins.")
#         quarters = float(input("how many quarters?: "))
#         dimes = float(input("how many dimes?: "))
#         nickels = float(input("how many nickels: "))
#         pennies = float(input("how many pennies?: "))
#         total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
#         if total < MENU[drink]['cost']:
#             print("Sorry that's not enough money. Money refunded.")
#             return 0
#         elif resources['water'] < MENU[drink]['ingredients']['water']:
#             print("Sorry we have run out of water. Money refunded")
#             return 0
#         elif resources['coffee'] < MENU[drink]['ingredients']['coffee']:
#             print("Sorry we have run out of coffee. Money refunded")
#             return 0
#         elif drink != 'espresso' and resources['milk'] < MENU[drink]['ingredients']['milk']:
#             print("Sorry we have run out of milk. Money refunded")
#             return 0
#         # elif drink not in ['espresso', 'latte', 'cappuccino']:
#         #     print("Please enter one of: 'espresso', 'latte', 'cappuccino'")
#         else:
#             resources['coffee'] -= MENU[drink]['ingredients']['coffee']
#             resources['water'] -= MENU[drink]['ingredients']['water']
#             if drink != 'espresso':
#                 resources['milk'] -= MENU[drink]['ingredients']['milk']
#
#             if total > MENU[drink]['cost']:
#                 print("Here is ${0:.2f} in change.\nHere is your {1:s} ☕️. Enjoy!".format(total - MENU[drink]['cost'],
#                                                                                           drink))
#             else:
#                 print("Here is your {0:s} ☕️. Enjoy!".format(drink))
#             return MENU[drink]['cost']
#
#     def report():
#         print(f"Water: {resources['water']}")
#         print(f"Coffee: {resources['coffee']}")
#         print(f"Milk: {resources['milk']}")
#         print(f"Money ${money}")
#
#     # start of the routine
#     response = input_response()
#     while response:
#         if response == 'off':
#             return
#         elif response == 'report':
#             report()
#             response = input_response()
#         else:
#             money += handle_drink(response)
#             response = input_response()
