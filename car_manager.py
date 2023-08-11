from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.allcars=[]
        self.cspeed=STARTING_MOVE_DISTANCE

    def create(self):
        chance=random.randint(1, 6)
        if chance==1:
            car=Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            ry=random.randint(-250, 250)
            car.color(random.choice(COLORS))
            car.goto(300, ry)
            self.allcars.append(car)

    def move(self):
        for car in self.allcars:
            car.backward(self.cspeed)

    def levelup(self):
        self.cspeed+=MOVE_INCREMENT
