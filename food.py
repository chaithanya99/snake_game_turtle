from turtle import *
from random import randint
class Food:
    def __init__(self):
        self.f=Turtle()
        self.f.shape("circle")
        self.f.color("blue")
        self.f.turtlesize(0.5)
        self.new_food()
    def new_food(self):
        x=randint(-260,260)
        y=randint(-260,260)
        self.f.penup()
        self.f.goto(x,y)