# '''List Comprehension'''
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [n for n in names if len(n) < 5]
# long_names = [n.upper() for n in names if len(n) > 5],

import random
import pandas


# '''Dictionary Comprehension'''
# student_scores = {student:random.randint(1,100) for student in names}
# # print(student_scores)

# #Loop through a dictionary to use in next dictionary
# #looks through the dictionary and adds based on condition
# #items() gets all the items in a dictionary
# passed_students = {student:score for (student,score) in student_scores.item() if score>60}

'''How to iterate over a Pandas DataFrame'''
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]

}

#loops through and prints key
# for (key, value) in student_dict.items():
#     print(key)

#Pandas dataframe
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Pandas has a built-in loop function that can go through each of the rows. 
#Loop through pandas dataframe

'''Example 1'''
# for (index, row) in student_data_frame.iterrows():
#     print(row.score)

'''Example 2'''
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)