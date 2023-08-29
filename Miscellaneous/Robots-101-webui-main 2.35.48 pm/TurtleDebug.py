import turtle

class DebugTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.color('red')
        
        self.vel = 0
        self.angVel = 0