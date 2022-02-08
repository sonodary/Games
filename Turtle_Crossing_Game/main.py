import time
import turtle
from turtle import Screen
from Turtle_Crossing_Game.player import Player
from Turtle_Crossing_Game.car_manager import CarManager
from Turtle_Crossing_Game.scoreboard import Scoreboard

def turtlegame():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    player = Player()
    scoreboard = Scoreboard()
    cars = CarManager()

    screen.listen()
    screen.onkeypress(player.move, "Up")


    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        turtle.TurtleScreen._RUNNING = True
        screen.update()
        cars.generate()
        cars.move()
        if player.finish():
            player.go_to_start()
            scoreboard.increase()
            cars.level_up()
        for car in cars.cars:
            if ((23 > (car.ycor() - player.ycor()) > 0) or (0 < (player.ycor() - car.ycor()) < 15)) and (abs(car.xcor() - player.xcor()) < 40):
                scoreboard.gameover()
                game_is_on = False

    screen.exitonclick()