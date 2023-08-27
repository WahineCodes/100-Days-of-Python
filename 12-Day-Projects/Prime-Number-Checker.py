'''
TITLE: Prime Number Checker
DESCRIPTION: Checks to see if a number is prime. Prime numbers are numbers that are greater than 1, 
      and are divisible by itself and one. 
USED: Defining a function with parameters and arguments,calling a function, if/elif conditional statements. 

'''

#Defining a function called prime_checker with one paramenter called number.
def prime_checker(number):
    prime_num = True 

    #Checks to see if the number is > 1
    if number == 1:
        print("It's not a prime number.") 

    #Checks to see if the number is cleanly divisible by another number
    #If so then it is not prime
    for i in range (2, number):
        if number % i == 0:
            prime_num = False

    #Prints if a number is prime or not. 
    if prime_num == True and number > 1:
        print("It's a prime number.")
    elif prime_num == False:
        print("It's not a prime number.")
            

#User input where n = number
n = int(input("Check this number: "))
prime_checker(number=n)
