class QuizController:

    def __init__(self, q_list):     #constructor
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):   #method
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def ask_question(self):          #method
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):    #method
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
