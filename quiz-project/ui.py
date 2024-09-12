from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 14, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_label = Label(bg=THEME_COLOR, text="Score: 0", font=FONT)
        self.score_label.grid(row=0, column=0, columnspan=2)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="QUESTION", fill="black", font=FONT,
                                                     width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image,
                                  highlightthickness=0, command=self.answer_true)
        self.false_button = Button(image=false_image,
                                   highlightthickness=0, command=self.answer_false)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz Finished!")

    def answer_true(self):
        if self.quiz.still_has_questions():
            if self.quiz.check_answer("True"):
                self.give_feedback(True)
                self.score_label.config(text=f"Score: {self.quiz.score}")
            else:
                self.give_feedback(False)
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz Finished!")

    def answer_false(self):
        if self.quiz.still_has_questions():
            if self.quiz.check_answer("False"):
                self.give_feedback(True)
                self.score_label.config(text=f"Score: {self.quiz.score}")
            else:
                self.give_feedback(False)
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz Finished!")

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)