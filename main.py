import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
screen.listen()


player = Player()
screen.onkeypress(player.up, "Up")
carmanager = CarManager()
scoring = Scoreboard()


game_is_on = True
count = 0
carmanager.on_start()
while game_is_on:
    time.sleep(0.3)
    scoring.score(player.level + 1)
    screen.update()
    count = count + 1
    carmanager.general_move(player.level)
    if player.ycor() >= 280:
        player.restart()
    if count % 6 == 0:
        for i in range((player.level + 1) * 2):
            carmanager.create_cars(300)
    for car in carmanager.cars:
        if abs(car.xcor() - player.xcor()) < 25 and abs(car.ycor() - player.ycor()) < 10:
            game_is_on = False
            scoring.game_over()
            


screen.exitonclick()