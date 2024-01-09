from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self): 
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.setpos(STARTING_POSITION)

    def up(self):
        self.setpos(0, self.ycor() + MOVE_DISTANCE)


    def down(self):
        self.setpos(0, self.ycor() - MOVE_DISTANCE)

    def reset(self):
        self.setpos(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False