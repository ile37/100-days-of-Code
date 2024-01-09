from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.moving_cars = []
        
    def move(self):
        for car in self.moving_cars:
            car.forward(STARTING_MOVE_DISTANCE)
            if car.xcor() < -350:
                car.setpos(350, 0)
                self.moving_cars.remove(car)
    
    def add_moving_cars(self):
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.setpos(350, random.randint(-250, 290))
            self.moving_cars.append(car)

    def speed_increase(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
