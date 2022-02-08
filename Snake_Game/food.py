from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("red")
        self.speed("fastest")
        self.goto(random.randint(-270, 270), random.randint(-270, 270))

    def change_position(self):
        self.goto(random.randint(-270, 270), random.randint(-270, 270))

    def bonus(self):
        self.shape("turtle")

    def back_to_normal(self):
        self.shape("circle")

