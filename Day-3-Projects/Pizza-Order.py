'''
Title: Pizza Order
Description: Sums up the total bill of a pizza based on the user's choices. 
Utilized: Nested conditions, += operator, f-strings, if/elif/else conditional statements
'''

#Asks for user preference. 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

#Created the bill variable as a placeholder. 
#As the user selects pizza size bill will be replaced by the cost of the pizza they select. 
bill = 0


#Selection for the small pizza. 
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")

#Selection for the medium pizza.     
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is: ${bill}.")
    else:
        print(f"Your final bill is: ${bill}.")

#Selection for the large pizza.
else:
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is: ${bill}.")
    else:
        print(f"Your final bill is: ${bill}.")
