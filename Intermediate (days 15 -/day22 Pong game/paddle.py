from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("White")
        self.penup()
        self.setpos(pos)
        
    def up(self):
        self.goto(self.xcor(), self.ycor() + 30)
    
    def down(self):
        self.goto(self.xcor(), self.ycor() - 30)