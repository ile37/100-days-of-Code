from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.setpos(-100, 190)
        self.write(self.left_score, align="center", font=("Courier", 60, "normal") )
        self.setpos(100, 190)
        self.write(self.right_score, align="center", font=("Courier", 60, "normal") )