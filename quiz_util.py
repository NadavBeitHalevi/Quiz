from typing import Dict, List
from question_model import Question


class QuizUtil:

    @staticmethod
    def quiz_transform(question_data: List[Dict[str, str]]) -> List[Question]:
        question_bank = []
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)
        return question_bank