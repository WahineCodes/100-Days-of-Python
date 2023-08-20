'''
Title: Sum of Even Numbers
Description: Sums all even numbers from 0 to 101. 
Utilized: for loops
'''

#Created an empty variable
even_numbers = 0

#Created a loop with a range between 0 to 101. 
#It takes a number every 2 steps and adds it to the list even_number. 

for number in range(0, 101, 2):
    even_numbers += number

print(even_numbers)
