'''
TITLE: Silent Auction
DESCRIPTION: A program that takes bidders names and prices and stores it,
       in a dictionary to see who the highest bidder is. 
USED: defining functions, lists, dictionaries, importing 
'''

import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program.\n")

#To hold the bidders and bids. 
bidder_list = {}


def highest_bidder(bidder_record):
  highest_bid = 0 
  winner = ""
  
  #for loop to see who bid the highest bid
  for bidder in bidder_record:
    bid_amount = bidder_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a ${highest_bid} bid.")

#Loop to continue entering info on bidder and bid, until someone types "no"
while True:
  name = input("What is your name?\n")
  bid = int(input("What is your bid?\n"))
  bidder_list[name] = bid
  more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n")

  #If no more bids, it calls the highest_bidder function to see who won.
  if more_bids == "no":
    highest_bidder(bidder_record=bidder_list)
    break

  #If there are more bids then it clears the console,
  #So that no one knows who bid and bid price. 
  elif more_bids == "yes":
    os.system('clear')