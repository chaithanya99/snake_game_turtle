from turtle import *
import turtle
import time
start_pos=[(0,0),(-20,0),(-40,0)]

class Snake:

    def __init__(self):
        self.all_tur=[]
        self.create_snake()
        self.head=self.all_tur[0]

    def create_snake(self):
        for i in start_pos:
            t = Turtle()
            t.penup()
            t.shape("square")
            t.color("white")
            t.goto(i)
            self.all_tur.append(t)

    def add_length(self):
        t = Turtle()
        t.penup()
        t.shape("square")
        t.color("white")
        t.goto(self.all_tur[len(self.all_tur)-1].pos())
        self.all_tur.append(t)
    def move(self):
        for i in range(len(self.all_tur) - 1, 0, -1):
            x = self.all_tur[i - 1].xcor()
            y = self.all_tur[i - 1].ycor()
            self.all_tur[i].goto(x, y)

        self.all_tur[0].fd(20)


    def move_up(self):
        print("move up")
        self.all_tur[0].setheading(90)
    def move_left(self):
        print("move left")
        self.all_tur[0].setheading(180)
    def move_down(self):
        print("move down")
        self.all_tur[0].setheading(270)
    def move_right(self):
        print("move right")
        self.all_tur[0].setheading(0)
    def get_head(self):
        return self.all_tur[0]