from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.penup()
        self.goto(STARTING_POSITION)


    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def restart(self):
        self.goto(STARTING_POSITION)
        self.level += 1

    
