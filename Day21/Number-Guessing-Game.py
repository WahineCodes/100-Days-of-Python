import random

logo = '''                                                                      
┏┓         ┓            ┓     
┃┓┓┏┏┓┏┏  ╋┣┓┏┓  ┏┓┓┏┏┳┓┣┓┏┓┏┓
┗┛┗┻┗ ┛┛  ┗┛┗┗   ┛┗┗┻┛┗┗┗┛┗ ┛
'''

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")


def game():
  random_number = int(random.randint(1, 100))
  #Used the line below while testing my code, to ensure it was working.
  # print(f"The random Number: {random_number}\n")

  #Determines the ammount of attempts a user has
  def guess_attempts():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard'\n")
    if difficulty_level == "easy":
      return 10
    else:
      return 5

  #Variable to store attempt choice
  x = guess_attempts()

  guess_again = True
  
  while guess_again:
    #Ensures that the user can guess as many times as the program allows.
    user_guess = int(input("Make a guess: "))
    
    #Needed to put this as the first if statement for attempts. 
    if x == 0:
      print("You ran out of attempts. Game Over.")
      guess_again = False
    
    #If user guesses correct. Loop ends. Answer is printed.
    elif user_guess == random_number:
      print(f"You guessed correct! The answer was {random_number}")
      guess_again = False
    
    #When user guesses too high. Attempts decrease. Goes back to top of loop. 
    elif user_guess > random_number:
      print("Too High.\nGuess again.\n")
      x -= 1
      print(f"You have {x} attempts remaining to guess the number")  
      
    #When user guesses too high. Attempts decrease. Goes back to top of loop. 
    elif user_guess < random_number:
      print("Too Low.\nGuess again\n")
      x -= 1
      print(f"You have {x} attempts remaining to guess the number")  
      

#Calls the game function    
game()