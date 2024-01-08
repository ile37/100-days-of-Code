from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle(pos=(-380,0))
right_paddle = Paddle(pos=(370,0))
baddles = [left_paddle, right_paddle]

ball = Ball()

scoreboard = Scoreboard()

screen.listen()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_on = True

while game_on:

    screen.update()
    time.sleep(0.012)

    ball.move()

    # Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Collision with baddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 350 or ball.distance(left_paddle) < 50 and ball.xcor() < -360:
        ball.baddle_bounce()

    # Out of bounds
    if ball.xcor() > 410:
        ball.reset()
        scoreboard.left_score += 1
        scoreboard.update_score()

    if ball.xcor() < -410:
        ball.reset()
        scoreboard.right_score += 1
        scoreboard.update_score()


screen.exitonclick()