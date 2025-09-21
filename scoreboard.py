from os import write
from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-280,250)
        self.score = 1
        self.show()

    def add_score(self):
        self.score+=1
        self.clear()
        self.show()

    def show(self):
        self.write(arg=f"Level: {self.score}" , align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER !!" , align="center", font=FONT)
