'''
Title: Rock, Paper, Scissors Version 2
Description: Play a game of Rock, Paper, Scissors against the computer. 
             Rock wins against Scissors, Paper wins against Rock, and Scissors wins against paper. 
Utilized: random module, if/elif/else conditional statements
'''

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

user_choice = (input("Welcome to Rock, Paper, Scissors.\nIn this game you will be competing against the computer.\nChoose Rock, Paper, or Scissors:\n")).lower()

#Randomize the numbers with range (0,3) for computer choice.
random_number = random.randint(0,2)
print(random_number)

#Game Visualization

print(user_choice)
print("You Chose:")
if user_choice == "rock":
  print(rock)
elif user_choice == "paper":
  print(paper)
else:
  print(scissors)


#Computer's choice
print("Computer chose:\n")
if random_number == 0:
  print(rock)
elif random_number == 1:
  print(paper)
else:
  print(scissors)


#Conditions:
if user_choice == "rock" and random_number == 0:
  print("It's a tie")
elif user_choice == "rock" and random_number == 1:
  print("You lose.")
elif user_choice == "rock" and random_number == 2:
  print("You win")
if user_choice == "paper" and random_number == 0:
  print("You win")
elif user_choice == "paper" and random_number == 1:
  print("It's a tie.")
elif user_choice == "paper" and random_number == 2:
  print("You lose")
if user_choice == "scissors" and random_number == 0:
  print("You lose")
elif user_choice == "scissors" and random_number == 1:
  print("You win.")
elif user_choice == "scissors" and random_number == 2:
  print("It's a tie")