'''
Title: Band Name Generator
Description: Created a band name generator which combines user input of city and pet names.
Utilized: print(), input(), variables, concatenation using the + operator. 
'''


#Created a greeting the program.
print("Welcome to the band name generator!")
print("Follow the prompts below to create a band name.\n")

#Ask the user for the city that they grew up in.
city = input("What city did you grow up in?\n")

#Ask the user for the name of a pet.
pet = input("What was the name of your favorite pet?\n")

#Combine the name of their city and pet and show them their band name.
name = (city + " " + pet)

#Make sure the input cursor shows on a new line:
print("Your band name can be " + name + "!")
