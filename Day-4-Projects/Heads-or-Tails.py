'''
Title: Heads or Tails
Description: Randomly picks heads or tails. 
Utilized: random module, if/else statement
'''


import random

#prompt
print("Will it be Heads or Tails")

#variables:
heads = 1
tails = 2

#randomization:
random_number = random.randint(1, 2)

#Used this as a tester to make sure that the random number corresponded with the right variables
#print(random_number)

#Conditions for heads and tails. 
if random_number == 1:
    print("Heads")
else:
    print("Tails")
