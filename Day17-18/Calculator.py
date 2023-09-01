'''
TITLE: Calculator
DESCRIPTION: Can add, subtract, divide, and multiply numbers. 
USED: def functions, parameters, arguments, lists, dictionaries,
      f-strings. 
'''

#Since I use a mac I imported os to be able to clear the console. 
import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

#Functions of the different operator symbols
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add, 
  "-": subtract,
  "*": multiply,
  "/": divide,
}

#Function to do all the calculator 
def calculator():
  print(logo)

  #Users first input
  first_number = float(input("What's the first number?: "))

  #prints the different operations a user can choose from
  for symbol in operations:
    print(symbol)
  
  #Condition that will allow the while loop to run if true. 
  should_continue = True

  while should_continue:
    #Asks user for operator and second number for their calculations. 
    operation_symbol = input("Pick an operation from above: ")
    second_number = int(input("What's the next number?: "))

    #Pulls the operation symbol user chose. 
    calculation_function = operations[operation_symbol]

    #Shows the equation and answer
    answer = calculation_function(first_number, second_number)
    print(f"{first_number} {operation_symbol} {second_number} = {answer}")

    #Users decision to continue or start a new calculation independent of past equations. 
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      first_number = answer

    #Condition that stops the while loop.
    else: 
      should_continue = False
      os.system('clear')
      calculator()

#Calls the calculator function in order for it to run. 
calculator()