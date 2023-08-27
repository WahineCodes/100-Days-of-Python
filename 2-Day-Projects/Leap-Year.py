'''
Title: Leap Year
Description: Determine if a specific year is a leap year or not. 
Practiced: nested conditions statements, if/elif/else statements. 


Notes: How to determine if a year is a leap year. 
- On every year that is evenly divisible by 4 
- EXCEPT every year that is evenly divisible by 100 
- UNLESS the year is also evenly divisible by 400
'''

#Ask's users to type a year they want to check. 
year = int(input("Which year do you want to check? "))

#Making equations to determine if a specific year has remainders.
#To follow the determining leap year factors listed above. 
div4 = year % 4

div100 = year % 100

div400 = year % 400

#Nested condition statements: 
if div4 == 0:
    if div100 == 0:
        if div400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    elif div100 > 0:
        print("Leap year.")
else:
    print("Not leap year.")
