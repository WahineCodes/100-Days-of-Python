'''
Title: Tip Calculator
Description: Created a tip calculator that accounts for the total of the bill, the % of tip, and
             how many people will split the bill. 
Utilized: f-string, float(), int(), input(), operators (*, +, /), round(), .format()
'''

#Example: If the bill was $150.00, split between 5 people, with 12% tip, the output would be 33.60

#Obtain user inputs re: total bill, amount of people to split, percentage of tip.
#Changes the variables from a str to float or int types. 
bill_total = float(input("How much was your bill?\n"))
people = float(input("How many people will split the bill?\n"))
tip = int(input("How much tip did you want to give?\n"))

#Makes the tip a decimal. 
percent_tip = tip/100

#Calculates amount of tip
find_tip = bill_total * percent_tip

#Calculates amount each person will give. 
bill_per_person = (bill_total + find_tip) / people

#Using the round() function to output 2 decimal place. 
#However due to a formatting issue only 1 decimal place is outputted.
bill = round(bill_per_person, 2)

#To fix the formatting issue used the following format() function.
#Now any output will have 2 decimal places. 
bill = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: {bill}")