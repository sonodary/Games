from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body = []
        # Create snakes and put to the initial position
        for position in STARTING_POSITION:
            self.add_one(position)
        self.head = self.body[0]

    def add_one(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.body.append(new_turtle)

    def move(self):
        for pos in range(len(self.body) - 1, 0, -1):
            new_x = self.body[pos - 1].xcor()
            new_y = self.body[pos - 1].ycor()
            self.body[pos].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def grow(self):
        self.add_one(self.body[-1].position())

    def reposition(self):
        for snake in self.body:
            snake.goto(1000, 1000)
        self.body.clear()
        # Create snakes and put to the initial position
        for position in STARTING_POSITION:
            self.add_one(position)
        self.head = self.body[0]