from turtle import Turtle
import random
import time
# THe smaller the faster
INITIAL_SPEED = 0.05

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        # The angle of the ball
        self.x_move = random.randint(4, 8)
        self.y_move = random.randint(4, 8)
        self.ball_speed = INITIAL_SPEED

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def collision_wall(self):
        self.y_move *= -1

    def reflect_to_left(self):
        if self.x_move < 4:
            self.x_move = - (self.x_move + random.randint(0, 2))
        else:
            self.x_move = - (self.x_move + random.randint(-2, 0))

    def reflect_to_right(self):
        if self.x_move > -4:
            self.x_move = - (self.x_move + random.randint(-2, 0))
        else:
            self.x_move = - (self.x_move + random.randint(0, 2))

    def change_angle(self):
        if self.x_move > 0:
            self.reflect_to_left()
        else:
            self.reflect_to_right()

    def collision_right_paddle(self):
        self.reflect_to_left()
        self.ball_speed /= 1.3
        self.move()

    def collision_left_paddle(self):
        self.reflect_to_right()
        self.ball_speed /= 1.03
        self.move()

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = INITIAL_SPEED
        time.sleep(1)
        self.change_angle()





