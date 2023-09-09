from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        
    def score(self, level):
        self.clear()
        self.write(f"Level:{level}", False, "center", font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", font = FONT)
    
