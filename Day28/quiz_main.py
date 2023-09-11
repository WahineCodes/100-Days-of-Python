'''
TITLE: Quiz with OOP
DESCRIPTION: The following program uses Object Oriented Programing to 
       display a general knowledge quiz with 15 questions. 
'''
#Calls the classes from the other files to be used in the quiz_main
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

    if quiz.question_number == len(quiz.question_list):
        print("You've completed the quiz.")
        print(f"Your final score was {quiz.score}/{quiz.question_number}")
        False