from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    cars = []
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
      
    
    def create_cars(self, x):
        new_car = CarManager()
        y = random.randint(-250, 250)
        new_car.shape("square")
        new_car.shapesize(1, 2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(x, y)
        self.cars.append(new_car)

    def on_start(self):
        for i in range(15):
            x = random.randint(-250, 250)
            self.create_cars(x)
        

    def general_move(self, level):
        for car in self.cars:
            if car.xcor() <= -340:
                self.cars.remove(car)
            car.goto(car.xcor()-(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * level), car.ycor())
