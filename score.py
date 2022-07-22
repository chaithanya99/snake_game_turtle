from turtle import *

class Score:
    def __init__(self):
        self.score=0
        self.turtle=Turtle()
        self.turtle.color("white")
        self.print_score()
        self.turtle.hideturtle()
    def print_score(self):
        self.turtle.clear()
        self.turtle.write("Score: " + str(self.score), align="center", font=("Arial", 24, "normal"))
    def print_game_over(self):
        self.turtle.clear()
        self.turtle.write("Gameover", align="center", font=("Arial", 24, "normal"))
