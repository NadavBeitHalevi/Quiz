from quiz_brain import QuizBrain
from quiz_service import QuizService
from quiz_ui import QuizInterface

q_brain = QuizBrain(q_sevice=QuizService())
QuizInterface(quiz_brain=q_brain)
