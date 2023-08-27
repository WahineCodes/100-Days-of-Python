zero = (r''' 
+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')


one = ('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========\n''')

two = ('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========\n''')

three = ('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========\n''')

four = ('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========\n''')

five = ('''
  +---+
  |   |
  O   |
      |
      |
      |
=========\n''')

six = (
'''  +---+
  |   |
      |
      |
      |
      |
=========\n''')

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                 


import random

print(logo)
print("Theme: Animals")
print("Rules")
print(" * Guess the word and win. Guess the wrong letter and lose a life")
print(" * If you guess the correct letters there are no penalties.") 
print(" * If run out of lives, you lose\n")

word_list = ["aardvark", "camel", "zebra", "monkey", "elephant", "sloth", "dog", "cat", 
             "gorilla", "python", "lion", "cheetah", "hippo", "rhino", "panda", "meerkat",
            "penguin", "giraffe"]

#Randomly selects a word
word = random.choice(word_list)

#Assign the random word to chosen_word variable
chosen_word = list(word)

#Count how many letters are in chosen_word
count = len(chosen_word)

#For each letter in the chosen_word, add a "_" to the variable display. 
display = []
for blank_space in range(count):
  display.append("_")

#User has 6 lives
user_lives = 6

#Condition to end the game
end_game = False

while not end_game:
  guess = str(input("Guess a letter: ").lower())

  if guess in display:
    print(f"You've already guessed {guess}\n")

  #Looks at all the positions in chosen_word
  for position in range(count):
    letter = chosen_word[position]
    #Replaces a blank in display with the letter
    if letter == guess:
      display[position] = letter

  #User loses a life for wrong guesses
  if guess not in chosen_word:
    user_lives -= 1
    print(f"The letter is not in the word. You lose one live.\nYou now have {user_lives} lives left.\n")

  #Hangman art according to number of lives. 
  if user_lives == 6:
    print(display)
    print(six)
  
  elif user_lives == 5:
    print(display)
    print(five)

  elif user_lives == 4:
    print(display)
    print(four)

  elif user_lives == 3:
    print(display)
    print(three)

  elif user_lives == 2:
    print(display)
    print(two)

  elif user_lives == 1:
    print(display)
    print(one)
  

  #Condition to win the game: no '_' in display. 
  if "_" not in display:
    end_game = True
    print("YOU WIN")

  #Condition to lose the game: 0 lives. 
  elif user_lives == 0:
    end_game = True
    print("YOU LOSE")
    print(zero)