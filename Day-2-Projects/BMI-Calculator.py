#Adding the variables for height and weight to obtain user input:
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#To be able to use the ** operator, the height variable needs to become a float. 
height_calc = (float(height) ** 2)

#Converting weight from a str to a float
weight_type = float(weight)

#Equation with int type so a whole number is the output
BMI = int(weight_type/height_calc)

print(BMI)