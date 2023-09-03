'''
TITLE: Black Jack Game ~ Capstone Project
DESCRIPTION: The goal is to get cards equivalent to 21. If you go over you lose and the computer wins.
      If you tie with the dealer you win.  
USED: Summary of everything I've learned in the past days. 
'''

#Modules that allow me to use random and clear()
import random
import os

#Randomly get cards from the list. 
#11 represents the Ace and can be a 11 or a 1. 
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Calculates the score of the cards
def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
    
  #If the user is over 21 but has a 11, the 11 becomes a 1
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Condition that compares users score to computers score
def compare(user_score, computer_score):
  
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose"


  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif user_score == 0:
    return "Win with a Blackjack"
  elif user_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "Opponent went over. You win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"
  
def play_game():

  logo = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           
'''
  
  print(logo)

  #Variables to hold user and computer's cards
  user_cards = []
  computer_cards = []
  is_game_over = False

  #Deals the user and computer 2 cards each
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #While loop that allows the user to continue to choose cards. 
  #In order to try to reach 21. 
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  #Rule: If the computer has less than 17 score then it automatically needs another card. 
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

#If user wants to play another game of Blackjack the console/terminal will clear the past game. 
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system('clear')
  play_game()

