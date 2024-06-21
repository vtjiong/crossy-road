import time
import turtle
import player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("turtle-cross")
screen.tracer(0)
screen.listen()
player = player.Player()
screen.onkey(fun=player.move, key="w")
car_manager = CarManager()
game_is_on = True
calculator = 0
scoreboard = Scoreboard()
while game_is_on:
    time.sleep(0.05)
    calculator += 1
    if calculator % 6 == 0:
        car_manager.create_car()
    screen.update()
    car_manager.move_cars()
    # Detect success
    if player.ycor() > 280:
        scoreboard.update()
        player.level_up()
        car_manager.speed_up()
    # Detect whether the turtle is colliding with the car
    if car_manager.check_collision(player):
        scoreboard.game_over()
        game_is_on = False
screen.exitonclick()