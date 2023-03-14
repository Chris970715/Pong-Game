from turtle import Turtle
import time
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1


    def move(self):
        x_p = (self.xcor() + self.x_move)
        y_p = (self.ycor() + self.y_move)
        self.goto(x_p,y_p)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.bounce_x()
        self.ball_speed = 0.1

