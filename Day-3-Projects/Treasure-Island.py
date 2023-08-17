'''
Title: Treasure Island
Description: A choose your adventure game in which users can pick certain paths to try to win the game. 
Utilized: Nested conditions, += operator, f-strings, if/elif/else conditional statements
'''

treasure = print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Game Over Prompts
right_fall = "Unfotunately you weren't watching where you were going and fell into a hole. You were unable to climb out and no other traveller was insight.\nGame Over."

swim_attack = "Unfotunately you didn't check the water and the creatures that lurked beneath. You were attacked by trout and was not able to find the treasure.\nGame Over."

door_red = "You have chosen the red door. You open the door but can't see anything insight, you step inside and fall into a floor of lava.\nGame Over."

door_blue = "You have chosen the blue door. You open the door but can't see anything insight, you step inside and have to run away from beasts.\nGame Over."

#Winner Prompt
win = "Congratulations you opened the correct door and found that behind the door was a hill with a castle. You climbed to the castle, went to the highest spire and found the hidden treasure."

#Choice 1 prompt:
left_right = (input("Would you like to begin this quest going 'left' or 'right'?\n")).lower()


if left_right == "right":
  print(right_fall)
elif left_right == "left":
  
  #Introduces whether user wants to swim or wait
  swim_wait = (input("You have now arrived at an unexpected lake. Would you like to 'swim' across the lake or 'wait' until help arrives?\n")).lower()
  if swim_wait == "swim":
    print(swim_attack)
  elif swim_wait == "wait":
    
    #Introduces the option for the three doors
    door = (input("It's a good thing you waited. A friendly captain arrives and allows you safe passage across the lake. Once you arrive on the land you follow a dirt   road. At the end of the road you are confronted with three doors. Do you want to enter the 'red', 'blue' or 'yellow' door?\n")).lower()
    if door == "blue":
      print(door_blue)
    elif door == "red":
      print(door_red)
    elif door == "yellow":
      print(win)
      print(treasure)
    elif door != "blue" or "red" or "yellow":
      print("Game Over")

  #Game over if anything other than swim or wait is typed. 
  elif swim_wait != "swim" or "wait":
    print("Game Over")

#Game over if anything other than right or left is typed. 
elif left_right != "right" or "left":
  print("Game Over")
else:
  print("Sorry you had bad luck and a magician sent you into a void. Game Over.")

