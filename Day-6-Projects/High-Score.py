'''
Title: Highest Score
Description: Looks at the scores that the user inputs and finds the 
             highest score. 
Utilized: for loops
'''

#Asks user to input scores
student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

print(student_scores)

#Created an empty variable. 
highest_score = 0

#For loop that looks at the scores then adds the highest number to the variable highest_score. 
for score in student_scores:
    if score > highest_score:
        highest_score = score
        
print(f"The highest score in the class is: {highest_score}")
