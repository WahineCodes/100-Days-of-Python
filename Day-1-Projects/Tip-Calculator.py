#Notes:
#The following creates a tip calculator that accounts for the total of the bill, 
#the percentage of tip, and how many people will split the bill.

#Example: If the bill was $150.00, split between 5 people, with 12% tip. Output = 33.60

#Obtaining user inputs re: total bill, amount of people to split, percentage of tip
bill_total = float(input("How much was your bill?\n"))
people = float(input("How many people will split the bill?\n"))
tip = int(input("How much tip did you want to give?\n"))

#Making tip into a decimal
percent_tip = tip/100

#Calculating how much tip to give
find_tip = bill_total * percent_tip

#Calculating how much tip to give per person. 
bill_per_person = (bill_total + find_tip) / people

#Using the round() to found to the 2 decimal place, however there is a formating issue
bill = round(bill_per_person, 2)

#To fix the formatting issue use the following to have 2 always have decimal places. 
bill = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: {bill}")