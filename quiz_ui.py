from tkinter import Tk, Label, Canvas, PhotoImage, Button
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.geometry("350x500")
        # score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        # canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=25)
        # true button
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        self.true_button.config(command=self.true_pressed)
        # false button
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)
        self.false_button.config(command=self.false_pressed)
        # get first question
        self.get_next_question()
        # run window
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.itemconfig(self.question_text, text=self.quiz_brain.next_question())

    def true_pressed(self):
        print("true pressed")
        is_user_right = self.quiz_brain.check_answer("True")
        if is_user_right:
            self.update_score()
        self.provide_feedback(is_user_right)


    def false_pressed(self):
        print("False")
        is_user_right = self.quiz_brain.check_answer("False")
        if is_user_right:
            self.update_score()
        self.provide_feedback(is_user_right)

    def update_score(self):
        score = self.quiz_brain.get_score()
        self.score_label.config(text=f"Score: {score} / 10")

    def provide_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.reset_bg_color)
        if self.quiz_brain.still_has_questions():
            self.window.after(1000, self.get_next_question)
        else:
            self.game_ended()

    def reset_bg_color(self):
        self.canvas.config(bg="white")

    def get_next_question(self):
        q_text = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
    
    def game_ended(self):
        self.canvas.itemconfig(self.question_text,
                               text=f"You've reached the end of the quiz.\nYour score is: {self.quiz_brain.get_score()}/10")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
