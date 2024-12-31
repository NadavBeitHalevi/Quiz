from typing import Dict, List
import requests

from question_model import Question

class QuizService:
    def __init__(self):
        self.parameters = {
            "type": "boolean"
        }
        self.base_url = "https://opentdb.com/api.php"

    def get_questions(self, num_of_questions: str) -> List[Dict[str, str]]:
        self.parameters["amount"] = num_of_questions
        response = requests.get(self.base_url, params=self.parameters)
        response.raise_for_status()
        question_data = response.json()["results"]
        return question_data
    
    def quiz_transform(self, question_data: List[Dict[str, str]]) -> List[Question]:
        question_bank = []
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)
        return question_bank
