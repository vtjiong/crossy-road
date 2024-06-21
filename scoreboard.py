import turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=FONT)
