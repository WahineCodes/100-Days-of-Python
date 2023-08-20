'''
Title: FizzBuzz
Description: From a range of numbers prints the numbers unless they are 
             divisible by 3 or 5 or both numbers. 
             If numbers are divisible by 3 it prints "Fizz."
             If numbers are divisible by 5 it prints "Buzz."
             If numbers are divisible by both 3 & 5 it prints "FizzBuzz."
Utilized: for loop, lists, modulo, if/elif/else fonditional statements. 
'''

#Created an empty list to input the numbers from the for loop below:
number_list = []

#Creates a range and stores number in number_list.
for number in range(1, 101):
  number_list.append(number)

#Used the modulo to identify if a number was divisible by 3 or 5.
#If modulo is equal to 0 then it was divisible by 3 or 5. 

#Conditions:
for i in number_list:
  #If the number is not divisible by 3 and 5 print the number.
  if ((i % 3) != 0) and ((i % 5) != 0):
    print(i)
  
  #if the number is divisible by 3 and 5 print "FizzBuss"
  elif ((i % 3) == 0) and ((i % 5) == 0):
    print("FizzBuzz")

  #If the number is divisible by 3 print "Fizz"
  elif (i % 3) == 0:
    print("Fizz")
  
  #If the number is divisible by 5 print "Buzz"
  elif (i % 5) == 0:
    print("Buzz")