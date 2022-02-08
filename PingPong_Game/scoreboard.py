from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 80, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGN, font=FONT)

    def increase_left(self):
        self.left_score += 1
        self.refresh_score()

    def increase_right(self):
        self.right_score += 1
        self.refresh_score()

    def gameover(self):
        if self.right_score == 7:
            self.goto(0, 0)
            self.write("Right win!", align=ALIGN, font=FONT)
        if self.left_score == 7:
            self.goto(0, 0)
            self.write("Left win!", align=ALIGN, font=FONT)