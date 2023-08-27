'''
Title: Love Score
Description: Takes both people's names and checks for the number of times the letters t, r, u, e, l, o, v, e appear. 
             It then sums up the count for t, r, u, e, as the fist number in the love score. 
             Next it susm the count of l, o, v, e as the second number in the love score. 
             Based on the score it outputs messages.     
Utilized: Nested conditions, += operator, f-strings, if/elif/else conditional statements
'''

#Prompt for user input.
#.lower() is used so that any name becomes lowercase. 
print("Welcome to the Love Calculator!")
name1 = (input("What is your name? \n")).lower()
name2 = (input("What is their name? \n")).lower()

#counts how many times the letters t, r, u, e are found within name1 and name2
t = int(name1.count("t")) + int(name2.count("t"))
r = int(name1.count("r")) + int(name2.count("r"))
u = int(name1.count("u")) + int(name2.count("u"))
e = int(name1.count("e")) + int(name2.count("e"))

#Adds together the t, r, u, e count for the first digit of the love score. 
sum_true = str(t + r + u + e)

#counts how many times the letters l, o, v, e are found within name1 and name2
l = int(name1.count("l")) + int(name2.count("l"))
o = int(name1.count("o")) + int(name2.count("o"))
v = int(name1.count("v")) + int(name2.count("v"))
e = int(name1.count("e")) + int(name2.count("e"))

#Adds together the l, o, v, e for the second digit of the love score. 
sum_love = str(l + o + v + e)

#Uses concat of strings to combine the true and love number sums to make a two digit number. 
#Next, it turns the score back into an integer for the loop. 
love_score = int(sum_true + sum_love)

if love_score < 10 or love_score >= 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
