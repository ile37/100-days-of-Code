from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:

    time.sleep(0.1)
    screen.update()

    snake.move()

    if snake.head.distance(food) < 20:
        food.eaten()
        snake.extend()
        scoreboard.add_score()

    # Wall collisions
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()

    # Tail collision
    for block in snake.snake[1:]:
        if snake.head.distance(block) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()