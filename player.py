import turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.starting_position = STARTING_POSITION
        self.penup()
        self.color("white")
        self.shape('turtle')
        self.seth(90)
        self.goto(STARTING_POSITION)

    def level_up(self):
        self.teleport(0,-280)

    def move(self):
        self.forward(MOVE_DISTANCE)