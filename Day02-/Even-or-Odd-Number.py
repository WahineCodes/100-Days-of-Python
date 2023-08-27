'''
Title: Even or Odd Number
Description: Practicing the modulo operator and creating a loop with if statement. 
Utilized: modulo (%)
'''

#Asks user to type a number. 
number = int(input("Which number do you want to check? "))

#Determines if the number has a remainder or not. 
remainder = number % 2

#Creating an if loop.

#If the remainder is equal to 0 then the number is even.
#if the remainder is above 0 then it is an odd number. 
if remainder >=1:
    print("This is an odd number.")
else:
    print("This is an even number.")