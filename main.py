import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("cyan")
screen.tracer(0)
player1 = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up",fun=player1.move)
game_is_on = True

score.show()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player1.is_win() == True:
        score.add_score()
        cars.chance.pop()
        cars.chance.pop()
        # if score.score <4:
        #     cars.chance.pop()
        #     cars.chance.pop()
        player1.reset_pos()
        cars.levelup()
    cars.create_car()
    cars.move()

    for car in cars.all_cars:
        if car.distance(player1) < 20 :
            score.game_over()
            game_is_on = False
screen.exitonclick()