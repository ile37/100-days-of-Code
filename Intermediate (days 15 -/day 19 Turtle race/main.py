from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False

user_bet = screen.textinput(title="Bets over here", prompt="Enter the color of the turtle you think is gonna win: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turts = []
for i, turt_color in enumerate(colors):
    new_turt = Turtle(shape="turtle")
    new_turt.color(turt_color)
    new_turt.penup()
    new_turt.goto(x=-230, y=(-100 + 40*i))
    turts.append(new_turt)


if user_bet:
    is_race_on = True

while is_race_on:

    for turt in turts:
        rand_distance = random.randint(0, 10)
        turt.forward(rand_distance)

        if turt.xcor() > 230:
            print(f"winner turtle color was {turt.color()[1]}")
            if user_bet == turt.color()[1]:
                print("You were correct")
            else:
                print("you were wrong")
            is_race_on = False
    
