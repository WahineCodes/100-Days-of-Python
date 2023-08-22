'''
Title: Password Generator - Hard Way - V2 - with for loops
Description: A password generator that takes a random sample of letters, symbols & numbers.
             It then randomly reorders the letters, symbols, numbers to random order to create a unique password. 
Practiced Using: random.sample(), "".join()
'''
import random

#List of random letters, symbols, and numbers. 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #0-51
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] #0-8
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] #0-9

#User input prompts:
print("Welcome to the PyPassword Generator!")
user_letters= int(input("How many letters would you like in your password?\n")) 
user_symbols = int(input(f"How many symbols would you like?\n"))
user_numbers = int(input(f"How many numbers would you like?\n"))

#HARD PASSWORD Version 2 - for loop

password_list = []

#For loops take random letters/symbols/numbers from lists and adds them to the password_list.
for char in range(1, user_letters + 1):
  password_list.append(random.choice(letters))

for sum in range(1, user_symbols + 1):
  password_list += random.choice(symbols)

for num in range(1, user_numbers + 1):
  password_list += random.choice(numbers)

#Shows initial list
print(password_list)

#How to reorder a list
random.shuffle(password_list)
print(password_list)

#Transform a list to a string
hard_password = ""
for char in password_list:
  hard_password += char

print(hard_password)