'''
Title: Restaurant Bill Roulette
Description: User inputs the names of people at the table, and the program randomly selects
             one person to pay the bill. 
Utilized: random module, int(), len(), input(), .split()
'''

#Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#To count how many names are inputted:
count = 0
count_names = int(len(names))

#Need to subtract 1, because lists start at 0
count += (count_names - 1)

#Now I need to randomize the numbers of names in a list. 
#count is an integer type
random_number = random.randint(0, count)

#Choose the name in the list based on the random number.
person = names[random_number]

#Prompt:
print(f"{person} is going to buy the meal today!")