import turtle
from turtle import Screen
from Snake_Game.snake import Snake
from Snake_Game.food import Food
from Snake_Game.scoreborad import Scoreborad
import time
import random

def snakegame():
    screen = Screen()
    screen.setup(width = 600, height = 600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreborad()

    stop = False
    # Forward
    while True:
        screen.listen()
        screen.onkeypress(snake.up, "Up")
        screen.onkeypress(snake.down, "Down")
        screen.onkeypress(snake.right, "Right")
        screen.onkeypress(snake.left, "Left")
        turtle.TurtleScreen._RUNNING = True
        screen.update()
        time.sleep(0.1)
        snake.move()
        # Occasionally, the food become turtle and the player can get a bonus point
        if random.randint(0, 20) == 0:
            food.bonus()

        if food.shape() == "turtle":
            if random.randint(0, 10) == 0:
                food.back_to_normal()

        # Detect whether the snake eats the food
        if snake.head.distance(food) < 15:
            food.change_position()
            snake.grow()
            if food.shape() == "circle":
                scoreboard.refresh()
            else:
                scoreboard.refresh_bonus()

        # Detect whether the snake collides the wall
        if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
            scoreboard.gameover()
            time.sleep(3)
            user_request = screen.textinput(title="Question", prompt="Do you wanna play again? Yes or No?")
            if (user_request.lower() == "no"):
                stop = True
            else:
                stop = False
            scoreboard.reset()
            snake.reposition()

        # Detect collision with tail
        for part in snake.body[1:]:
            if snake.head.distance(part) < 5:
                scoreboard.gameover()
                time.sleep(3)
                user_request = screen.textinput(title="Question", prompt="Do you wanna play again? Yes or No?")
                if (user_request.lower() == "no"):
                    turtle.bye()
                else:
                    stop = False
                scoreboard.reset()
                snake.reposition()

        if stop:
            break




    screen.exitonclick()