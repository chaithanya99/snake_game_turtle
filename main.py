import turtle
from food import *
from turtle import *
from snake import *
import time
from score import *
turtle.tracer(0)
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake game")

snake=Snake()
food=Food()
score=Score()
game_on=True
screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")

while game_on:
    turtle.update()
    time.sleep(0.1)
    snake.move()
    snake_head=snake.get_head()
    if snake.head.distance(food.f)<15:
        food.new_food()
        score.score+=1
        score.print_score()
        snake.add_length()
    if snake_head.xcor()>290 or snake_head.xcor()<-290 or snake_head.ycor()>290 or snake_head.ycor()<-290 :
        print("game over")
        score.print_game_over()
        game_on=False
    for s in snake.all_tur:
        if s==snake_head:
            pass
        elif snake_head.distance(s)<10:
            score.print_game_over()
            game_on = False








screen.exitonclick()