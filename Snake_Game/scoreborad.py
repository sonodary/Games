from turtle import Turtle
import os
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
current_directory = os.getcwd()

class Scoreborad(Turtle):


    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        with open(f"{current_directory}/Snake_Game/highScore.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.goto(0, 270)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.score += 1
        self.write_score()

    def refresh_bonus(self):
        self.score += 3
        self.write_score()

    def gameover(self):
        self.goto(0, 0)
        self.write(arg = "Game Over", move=False, align=ALIGNMENT, font=("Courier", 50, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(f"{current_directory}/Snake_Game/highScore.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.goto(0, 270)
        self.write_score()

