'''
Title: Password Generator - Easy Way
Description: A password generator that takes a random sample of letters, symbols & numbers and adds it to a password variable. 
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

#EASY PASSWORD V1
#random values from letters, numbers, symbol lists. 
random_letters = random.sample(letters, user_letters)
random_symbols = random.sample(symbols, user_symbols)
random_numbers = random.sample(numbers, user_numbers)

easy_password = ''.join(random_letters) + ''.join(random_symbols) + ''.join(random_numbers)

#Used this to test and make sure that the right letters,symbols, passowrds are in the easy_password
print(random_letters)
print(random_symbols)
print(random_numbers)

#Print the Easy Password
print(easy_password)