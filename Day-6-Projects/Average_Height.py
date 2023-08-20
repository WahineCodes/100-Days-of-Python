'''
Title: Average Height
Description: User inputs a list of heights and the program finds the 
             average height. 
Utilized: for loops
'''
#Asks the user to add a list of heights. 
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#Created a variable.
sum_height = 0

#A for loop that cycles through the student heights.
#It thenn adds the height to the variable sum_height.
for height in student_heights:
    sum_height += int(height)

#Needed to add +1 to n, becuase lists start from 0. 
average = round((sum_height / (n+1)))

print(average)
