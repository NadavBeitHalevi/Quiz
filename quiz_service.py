from typing import Dict, List
import requests

from question_model import Question


class QuizService:
    def __init__(self, base_url: str = "https://opentdb.com/api.php", question_type: str = "boolean"):
        self.parameters = {
            "type": question_type,
            "category": "18",
        }
        self.base_url = base_url

    def get_questions(self, num_of_questions: int) -> List[Dict[str, str]]:
        self.parameters["amount"] = str(num_of_questions)
        response = requests.get(self.base_url, params=self.parameters)
        response.raise_for_status()
        question_data = response.json().get("results", [])
        return question_data
