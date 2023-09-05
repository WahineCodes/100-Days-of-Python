'''
TITLE: Higher or Lower
DESCRIPTION: User will guess which person has a higher follower count on instagram. 
       As the user guesses right their score will increase. If they gues wrong the 
       game ends and their final score is revealed. 

       This version represents a shorter documentation of the game. 
'''

import random
import os

from game_data import data
from art import logo 
from art import vs 


def descriptions(account):
  name = account['name']
  job = account['description']
  country = account['country']
  return f"{name}, a {job}, from {country}\n"


def compare(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def switch(person_a, person_b):
  global score
  print(logo)
      
  person_a = person_b
  print(f"Compare A: {descriptions(account = person_a)}")

  print(vs)
  
  person_b = random.choice(data)
  print(f"Against B: {descriptions(account = person_b)}")

  print(f"You're right! Current score: {score}")

  if person_a == person_b:
    person_b = random.choice(data)
  

def game():
  score = 0
  play = True
  person_b = random.choice(data)
  
  while play:
    person_a = person_b

    person_b = random.choice(data)

    if person_a == person_b:
      person_b = random.choice(data)
  
    print(logo)
    print(f"Compare A: {descriptions(account = person_a)}")
    print(vs)
    print(f"Against B: {descriptions(account = person_b)}")
    print(f"Current score: {score}\n")

    guess = input("Who has more followers? Type 'a' or 'b':  ").lower()

    a_followers = person_a['follower_count']
    b_followers = person_b['follower_count']
    is_correct = compare(guess, a_followers, b_followers)

    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}")
      os.system('clear')
    
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      play = False

game()