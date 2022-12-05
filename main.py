from turtle import Screen
from snake import *
import time
from food import Food
from scorboard import *

screen=Screen()
snake=Snake()
food=Food()
scoreboard=Scoreboard()

GAME_ON=True

#screen parameters

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)




screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



while GAME_ON:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        scoreboard.new_score()
    
    #detect colision with wall
    if snake.head.xcor()>295  or snake.head.xcor()<-295  or snake.head.ycor()>295  or snake.head.ycor()<-295:
        scoreboard.reset()
        snake.reset()
        
    #if head collide with any segment in tail:
    for segment in snake.square_list[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()


        

screen.exitonclick()