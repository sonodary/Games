from turtle import Turtle
WIDTH = 5
LENGTH = 1

class Paddle(Turtle):
    def __init__(self, starting_xcor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=LENGTH, stretch_wid=WIDTH)
        self.color("white")
        self.penup()
        self.starting_xcor = starting_xcor
        self.goto(starting_xcor, 0)

    def up(self):
        self.goto(self.starting_xcor, self.ycor() + 40)

    def down(self):
        self.goto(self.starting_xcor, self.ycor() - 40)

