'''
Title: BMI 2.0
Description: Created a bmi indicator for adults that lets you know your weight/height 
              status based on the CDC's guidlines on bmi.  
Practiced: if,elif,else statements

CDC BMI Guidelines:
- Below 18.5 = Underweight
- 18.5 - 24.9 = Healthy Weight
- 25.0 - 29.9 = Overweight
- 30.0 and Above - Obese
'''

#Asks users for height(m) and weight(kg).
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#BMI equation
bmi = round(weight / (height ** 2))

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese")
