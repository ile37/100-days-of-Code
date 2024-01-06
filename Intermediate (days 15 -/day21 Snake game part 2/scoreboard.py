from turtle import Turtle

ALIGNMENT = "center"
POSITION = (0, 250)
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setpos(POSITION)
        self.color("White")
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        

    def add_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.setpos(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

