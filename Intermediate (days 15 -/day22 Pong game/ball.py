from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.penup()
        self.x_move = 3
        self.y_move = -3


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= (-1)

    def baddle_bounce(self):
        self.x_move *= (-1)

    def reset(self):
        self.setpos(0,0)
        self.x_move *= (-1)
        

