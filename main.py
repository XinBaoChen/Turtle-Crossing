from calendar import c
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
#Classes
player = Player()
cars = CarManager()
scoreBoard = Scoreboard()


screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_back, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move_car()

    #Detect collisions with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreBoard.game_Over()

    #Detect successful crossing increase level of difficulty
    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()
        scoreBoard.increase_level()

screen.exitonclick()