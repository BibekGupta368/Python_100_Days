from question_model import Question
from question_data import data_list
from quiz_controller import QuizController

question_bank = []
for question in data_list:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizController(question_bank)

while quiz.still_has_questions():
    quiz.ask_question()

print("You've sucessfully attempred all the question")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")
