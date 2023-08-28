'''
TITLE: Grading Program
DESCRIPTION: Looks at a python dictionary with keys=students and value=scores and based on their scores, 
             assigns the students a grade of outstanding, exceeds expectations, acceptable, or fail. 
USED: python dictionaries
'''

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
  scores = student_scores[student]
  if scores >= 91 and scores <= 100:
    student_grades[student] = "Outstanding"
  elif scores >= 81 and scores <= 90:
    student_grades[student] = "Exceeds Expectations"
  elif scores >= 71 and scores <= 80:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
 
print(student_grades)