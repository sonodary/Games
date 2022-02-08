COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

import random
from turtle import Turtle


class CarManager():
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def generate(self):
        if len(self.cars) < 30:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=3)
            car.goto(random.randint(310, 900), random.randint(-300, 300))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.goto(car.xcor() - self.speed, car.ycor())
            if car.xcor() < -335:
                self.cars.remove(car)

    def level_up(self):
        self.speed += MOVE_INCREMENT
