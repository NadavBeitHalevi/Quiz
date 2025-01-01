import html

from quiz_service import QuizService
from quiz_util import QuizUtil


class QuizBrain:
    def __init__(self, q_sevice: QuizService):
        self.question_number = 0
        self.score = 0
        self.quiz_service = q_sevice
        self.current_question = None
        response = self.quiz_service.get_questions(num_of_questions="10")
        
        self.question_list = QuizUtil.quiz_transform(question_data=response)
        print(f"numer of questions: {len(self.question_list)}")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        current_question_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {current_question_text}"
        # user_answer = input(f"Q.{self.question_number}: {current_question_text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer) -> bool:
        correct_answer = self.current_question.answer
        answer = user_answer.lower() == correct_answer.lower()
        if answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}" + "\n")
        return answer

    def get_score(self) -> int:
        return self.score
