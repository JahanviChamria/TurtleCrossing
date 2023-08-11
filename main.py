import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

t=Player()
cm=CarManager()
sc=Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=t.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cm.create()
    cm.move()

    for car in cm.allcars:
        if t.distance(car)<20:
            sc.fin()
            game_is_on=False

    if t.finish():
        t.start()
        cm.levelup()
        sc.lv()


screen.exitonclick()