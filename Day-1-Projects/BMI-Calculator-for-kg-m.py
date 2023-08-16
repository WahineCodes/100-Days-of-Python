'''
Title: BMI Calculator
Description: Created a BMI calculator for kg and meters. 
Utilized: print(), input(), variables, float(), int(), and ** operator. 
'''

#Adding the variables for height and weight to obtain user input:
height = input("Please enter your height in m: ")
weight = input("Please enter your weight in kg: ")

#Currently the height and weight variables are string types. 

#To be able to use the ** operator, the height variable needs to become a float. 
height_type = (float(height) ** 2)

#Converts the weight from a string to a float type. 
weight_type = float(weight)

#BMI equation that makes the output a integer. 
BMI = int(weight_type/height_type)

print(BMI)