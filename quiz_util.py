from typing import Dict, List
from question_model import Question


class QuizUtil():
    @staticmethod
    def quiz_transform(question_data: List[Dict[str, str]]) -> List[Question]:
        return [Question(question["question"], question["correct_answer"]) for question in question_data]