'''
TITLE: OOP Coffee Machine ~ (Object Oriented Programming)
DESCRIPTION: Concise program reflecting the same functions as Day23-Day24 Coffee Machine

Note: Type "report" to see how much resources and profit. Type "off" to turn off the machine. 
'''

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

#While loop that ask user for coffee choices.
while machine_on:
  
  #Ak users what type of coffee they want.
  choice = input(f"What would you like to drink? {menu.get_items()}: ")
  
  #Shows the resources and profit
  if choice == "report":
    coffee_maker.report()
    money_machine.report()

  #Turns machine off
  elif choice == "off":
    machine_on = False

  #Finds the drink and its resources. Asks user for payment. Sees if payment is > cost.
  #Makes coffee. 
  else:
    drink = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink):
      money_machine.make_payment(drink.cost)
      coffee_maker.make_coffee(drink)