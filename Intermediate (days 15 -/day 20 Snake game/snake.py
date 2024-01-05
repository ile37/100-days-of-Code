from turtle import Turtle

MOVE_DISTANCE = 20

class Snake():

    def __init__(self, start_size=3):
        self.snake = []
        self.create_snake(start_size)
        self.head = self.snake[0]

    def create_snake(self, start_size):
        for i in range(start_size):
            snake_block = Turtle("square")
            snake_block.penup()
            snake_block.color("White")
            if i != 0:
                snake_block.setpos(self.snake[i-1].xcor()-20, 0)
            self.snake.append(snake_block)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i-1].xcor()
            new_y = self.snake[i-1].ycor()
            self.snake[i].setpos(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)     

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)