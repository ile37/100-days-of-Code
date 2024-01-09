import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()

    car_manager.move()

    if len(car_manager.moving_cars) < 20 and random.randint(1, 6) == 1:
        car_manager.add_moving_cars()

    # Collision detection with cars
    for car in car_manager.moving_cars:
        if car.distance(player) < 15:
            scoreboard.game_over()
            game_is_on = False
    
    # Detect successful crossing
    if player.is_at_finish_line():
        car_manager.speed_increase()
        player.reset()
        scoreboard.increase_score()

    

screen.exitonclick()