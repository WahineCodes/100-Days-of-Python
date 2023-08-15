#How many days, weeks, months do you have left if you lived until age 90. 

#To obtain users age and make it a int instead of a str
age = int(input("What is your current age? "))

#General data about days, weeks, months in a year
days_in_year = 365
weeks_in_year = 52
months_in_year = 12

#Calculating users current age and year data.
my_days = age * days_in_year
my_weeks = age * weeks_in_year
my_months = age * months_in_year

#Accounting for weeks, months, days at age 90 
age_90 = 90 * days_in_year
weeks_90 = 90 * weeks_in_year
months_90 = 90 * months_in_year

#multiplied by -1 to make it a positive number
days = (my_days - age_90) * -1
weeks = (my_weeks - weeks_90) * -1
months = (my_months - months_90)  * -1

#practiced using a f-string
print(f"You have {days} days, {weeks} weeks, and {months} months left")