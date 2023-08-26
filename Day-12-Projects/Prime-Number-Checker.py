'''
TITLE: IS IT A PRIME NUMBER?
DESCRIPTION: Created a program to check if a number is a prime number.
USED: Defining a function with parameters and arguments, modulo (%)

Conditions to be prime:
- Must be greater than 1
- Must be divisible ONLY by itself and 1. 
'''

n = int(input("Check this number: "))

def prime_checker(number):
  prime_num = True
  if number == 1:
    print("It's not a prime number.")

  for i in range(2, number):
    if number % i == 0:
      prime_num = False

  if prime_num == True and number > 1:
    print("It's a prime number.")
  elif prime_num == False:
    print("It's not a prime number.")

prime_checker(number=n)