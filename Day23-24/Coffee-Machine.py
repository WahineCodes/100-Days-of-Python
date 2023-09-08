'''
TITLE: Coffee Machine
DESCRIPTION: You're a coffee shop and order a coffee. 
  - The program will let the userchoose a coffee
  - Input the necessary coins
  - Receive a coffee if enough money is inputted
  - Receive a refund if insufficient amoutn of coins were inserted
  - User can order as many times as the resources allow. 
  - Press report to see the resource amount and profit. 
  - Type off to turn off the machine once resources are used. 
'''

from menuresources import MENU
from menuresources import resources
from menuresources import latte
from menuresources import logo

print(logo)

#Shows the Amount for Each Resource. (ex. Water - 300 at start)
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
profit = 0

#1 Ask User - What Drink they want:
def chosen_drink():
  global water
  global milk
  global coffee
  global profit

  user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
  print("    ")

  #Report shows the quantity of resources left
  if user_choice == "report":
    print(f"water: {water}ml\nmilk: {milk}ml\ncoffee: {coffee}g\nprofit: ${profit}")
    print("    ")
    drink_ingredients(type = chosen_drink())

  #Ends the while loop in the code below
  elif user_choice == "off":
    print("Coffee machine has turned off")
    return 

  #Returns the users choice in the functions below
  elif user_choice == "espresso":
    return "espresso"
  elif user_choice == "latte":
    return "latte"
  elif user_choice == "cappuccino":
    return "cappuccino"

def add_resource(type):
  global water
  global milk
  global coffee

  #Separate variables to express the quantity of water, milk, coffee it takes to make each drink
  water_chosen_drink2 = (MENU[type]["ingredients"]["water"])
  milk_chosen_drink2 = (MENU[type]["ingredients"]["milk"])
  coffee_chosen_drink2 = (MENU[type]["ingredients"]["coffee"])

  #The drink_ingredient(type) function below subtracts the ingredients whenever a user orders a drink.
  #However, this function adds the ingredients back if the user is refunded their money. 
  if type == "espresso":
    water = water + water_chosen_drink2
    coffee = coffee + coffee_chosen_drink2
      
  elif type == "latte" or type == "cappuccino":
    water = water + water_chosen_drink2
    milk = milk + milk_chosen_drink2
    coffee = coffee + coffee_chosen_drink2

#Ask user to enter coins & Computer checks to see if enough money inputted
def check_money(type):   
  global profit
  
  print("Please insert coins.")
  quarters_user = float(input("  * How many quarters?: "))
  dimes_user = float(input("  * How many dimes?: "))
  nickles_user = float(input("  * How many nickles?: "))
  pennies_user = float(input("  * How many pennies?: "))
  
  sum_of_money = float((quarters_user * .25) + (dimes_user * .10) + (nickles_user * .05) + (pennies_user * .01))
  cost_drink = (MENU[type]["cost"])
  change = round(sum_of_money - cost_drink, 2)

  #If the user does not have enough money, the money is refunded.
  if sum_of_money < cost_drink: 
    print("  ")
    print("Sorry that's not enough money. Money refunded.\n")

    #This is used to counter act the function in the drink_ingredients(type) function.
    #So that no resources are used if a drink is ordered, but user does not input enough money. 
    add_resource(type = chosen_drink())
    
  elif sum_of_money == cost_drink:
    if type == "espresso":
      money = money + 1.5
    elif type == "latte":
      money = money + 2.5
    elif type == "cappuccino":
      money = money + 3.0
    print("  ")
    print(f"\nThank you!\nYour change is: {change}\nHere is your {type} ☕️. Enjoy!\n {latte}") 
    
  elif sum_of_money >= cost_drink:
    if type == "espresso":
      profit += 1.5
    elif type == "latte":
      profit += 2.5
    elif type == "cappuccino":
      profit += 3.0
    print("  ")
    print(f"Thank you!\nYour change is: {change}\nHere is your {type} ☕️. Enjoy!\n {latte}")


def drink_ingredients(type):
  global water
  global milk
  global coffee
  global success
  
  more_drinks = True
  
  while more_drinks:   
    if type == "espresso":
      #The ammount of resources to make the drink
      water_chosen_drink = (MENU[type]["ingredients"]["water"])
      coffee_chosen_drink = (MENU[type]["ingredients"]["coffee"])


      #The comments from here on down were used as testers to make sure the program was correct.
      if water > water_chosen_drink and coffee > coffee_chosen_drink:
            #print("1 (espresso). Enough resources")
        
        #Will check money first before procedding with the drinks
        check_money(type)
        
        #Subtracs the amount of ingredients from resources. 
        water = water - water_chosen_drink
            #print(f"water: {water}") 
        coffee = coffee - coffee_chosen_drink
            #print(f"coffee: {coffee}")
        drink_ingredients(type = chosen_drink())

      elif water == water_chosen_drink and coffee > coffee_chosen_drink:
            #print("1 (espress). Enough resources")
        check_money(type)
        water = water - water_chosen_drink
            #print(f"water: {water}")
        coffee = coffee - coffee_chosen_drink
            #print(f"coffee: {coffee}")
      
        drink_ingredients(type = chosen_drink())

      elif water < water_chosen_drink or coffee < coffee_chosen_drink:
          print("Sorry not enough water")
          print("Please order another drink or type 'off' to turn off machine. \n") 
          drink_ingredients(type = chosen_drink())

  
    elif type == "latte" or type == "cappuccino":
      water_chosen_drink = (MENU[type]["ingredients"]["water"])
      milk_chosen_drink = (MENU[type]["ingredients"]["milk"])
      coffee_chosen_drink = (MENU[type]["ingredients"]["coffee"])

      if water >= water_chosen_drink and coffee >= coffee_chosen_drink or milk >= milk_chosen_drink:
            #print("2 (latte/cap). Enough resources")
        check_money(type)
        water = water - water_chosen_drink
            #print(f"water: {water}")
        milk = milk - milk_chosen_drink
            #print(f"milk: {milk}")
        coffee = coffee - coffee_chosen_drink
            #print(f"coffee: {coffee}")
        drink_ingredients(type = chosen_drink())
      
      elif water < water_chosen_drink or coffee < coffee_chosen_drink or milk < milk_chosen_drink:
          print("Sorry not enough water")
          print("Please order another drink or type 'off' to turn off machine. \n") 
          drink_ingredients(type = chosen_drink())


    else:
      play_again = False

drink_ingredients(type = chosen_drink())