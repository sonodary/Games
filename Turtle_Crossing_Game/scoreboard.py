from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "Center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-230, 270)
        self.level = 1
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def increase(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGN, font=FONT)
