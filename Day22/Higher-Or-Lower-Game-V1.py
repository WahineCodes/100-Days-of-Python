'''
TITLE: Higher or Lower
DESCRIPTION: User will guess which person has a higher follower count on instagram. 
       As the user guesses right their score will increase. If they gues wrong the 
       game ends and their final score is revealed. 

       This version is a longer documentation of the game. 
'''

import random

import os

from art import logo 
from art import vs 

from game_data import data

print(logo)

score = 0

def pick_person():
  person = random.randint(0, len(data)-1)
  return person

for _ in range(1):
  person_a = (data[pick_person()])
  print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}")

  #VS
  print(vs)
  
  person_b = (data[pick_person()])
  print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}\n")

def switch(person_a, person_b):
  global score
  print(logo)
      
  person_a = person_b
  print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}")

  print(vs)
  
  person_b = (data[pick_person()])
  print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}\n")

  print(f"You're right! Current score: {score}")
      
  compare(person_a, person_b)

def compare(person_a, person_b):
  right_guess = True

  while right_guess:
    guess = input("Who has more followers? Type 'A' or 'B':  ").lower()
    global score
    
    if int(person_a['follower_count']) > int(person_b['follower_count']) and guess == "A":
      score += 1
      print(f"You're right! Current score: {score}")
      os.system('clear')
      switch(person_a, person_b)

    elif int(person_b['follower_count']) > int(person_a['follower_count']) and guess == "B":
      score += 1
      print(f"You're right! Current score: {score}")
      os.system('clear')
      switch(person_a, person_b)

    elif int(person_a['follower_count']) < int(person_b['follower_count']) and guess == "A":
      print(f"Sorry, that's wrong. Final score: {score}")
      right_guess = False

    elif int(person_b['follower_count']) < int(person_a['follower_count']) and guess == "B":
      print(f"Sorry, that's wrong. Final score: {score}")
      right_guess = False
    
    
    
compare(person_a, person_b)