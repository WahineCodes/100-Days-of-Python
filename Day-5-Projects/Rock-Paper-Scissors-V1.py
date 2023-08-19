'''
Title: Rock, Paper, Scissors Version 1
Description: Play a game of Rock, Paper, Scissors against the computer. 
             Rock wins against Scissors, Paper wins against Rock, and Scissors wins against paper. 
Utilized: random module, if/elif/else conditional statements
'''

#Visuals
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

#Rock wins against scissors
#Paper wins against Rock
#Scissors wins against paper


user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

computer_choice = random.randint(0,2)

#Conditions to Win
if user_input == 0 and computer_choice == 2:
    print(f"{rock}\nComputer Chooses:\n{scissors}\nYOU WIN")
elif user_input == 1 and computer_choice == 0:
    print(f"{paper}\nComputer Chooses:\n{rock}\nYou WIN")
elif user_input == 2 and computer_choice == 1:
    print(f"{scissors}\nComputer Chooses:\n{paper}\nYou WIN")

#Conditions to Tie
elif user_input == 0 and computer_choice == 0:
    print(f"{rock}\nComputer Chooses:\n{rock}\nITS A TIE")
elif user_input == 1 and computer_choice == 1:
    print(f"{paper}\nComputer Chooses:\n{paper}\nITS A TIE")
elif user_input == 2 and computer_choice == 2:
    print(f"{scissors}\nComputer Chooses:\n{scissors}\nITS A TIE")

#Conditions to Lose  
elif user_input == 0 and computer_choice == 1:
    print(f"{rock}\nComputer Chooses:\n{paper}\nYOU LOSE")
elif user_input == 1 and computer_choice == 2:
    print(f"{paper}\nComputer Chooses:\n{scissors}\nYOU LOSE")
elif user_input == 2 and computer_choice == 0:
    print(f"{scissors}\nComputer Chooses:\n{rock}\nYOU LOSE")

else:
    print("You typed the wrong number!")