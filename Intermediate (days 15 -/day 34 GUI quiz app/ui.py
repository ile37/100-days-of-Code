from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Quiz_gui():
    def __init__(self, quiz_brain:QuizBrain):

        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Quizz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR, font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=self.true_img, highlightthickness=0, command=lambda: self.answer_button_clicked("True"))
        self.true_btn.grid(row=2, column=0)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=self.false_img, highlightthickness=0, command=lambda: self.answer_button_clicked("False"))
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        question_text = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.question, text=question_text)
        self.canvas.config(bg="white")

    def answer_button_clicked(self, user_answer):
        if self.quiz_brain.check_answer(user_answer):
            self.canvas.config(bg="green")
            self.score.config(text=f"Score: {self.quiz_brain.score}")
        else:
            self.canvas.config(bg="red")

        if self.quiz_brain.still_has_questions():
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the quiz.")
            self.canvas.config(bg="white")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")