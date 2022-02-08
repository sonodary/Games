from turtle import Screen
import turtle
from PingPong_Game.paddle import Paddle
from PingPong_Game.ball import Ball
from PingPong_Game.scoreboard import Scoreboard
import time


def pingpong():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Ping Pong")
    screen.tracer(0)

    paddle_left = Paddle(-350)
    paddle_right = Paddle(350)
    ball = Ball()
    scoreboard = Scoreboard()

    # Reset the position of the paddles
    def paddle_reset():
        paddle_left.goto(-350, 0)
        paddle_right.goto(350, 0)

    #How to play
    screen.listen()
    screen.onkeypress(paddle_right.up, "Up")
    screen.onkeypress(paddle_right.down, "Down")
    screen.onkeypress(paddle_left.up, "q")
    screen.onkeypress(paddle_left.down, "a")

    while True:
        time.sleep(ball.ball_speed)
        turtle.TurtleScreen._RUNNING = True
        screen.update()
        ball.move()
        # Detect collision with walls
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.collision_wall()
        # Detect collision with paddle
        if ball.distance(paddle_right) < 50 and ball.xcor() > 330:
            ball.collision_right_paddle()
        elif ball.distance(paddle_left) < 50 and ball.xcor() < -330:
            ball.collision_left_paddle()
        # Detect scoring
        if ball.xcor() > 380:
            ball.reset_position()
            paddle_reset()
            scoreboard.increase_left()
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.increase_right()
            paddle_reset()
        # If the either player scores 7 points
        if scoreboard.left_score == 7 or scoreboard.right_score == 7:
            scoreboard.gameover()
            break

    screen.exitonclick()
