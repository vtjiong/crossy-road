import turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10

    def create_car(self):
        new_car= turtle.Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.pu()
        new_car.shapesize(1, 2)
        new_car.goto(300, random.randint(-250, 250))
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
             car.backward(self.STARTING_MOVE_DISTANCE)

    def speed_up(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT

    def check_collision(self, player):
        for car in self.all_cars:
            if car.distance(player) < 20:  # Collision threshold
                return True
        return False

