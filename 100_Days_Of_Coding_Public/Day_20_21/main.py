from turtle import Screen, Turtle

from score import Scoreboard
from snake import Snake
from food import Food

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snack Game")
screen.tracer(0)



snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extent()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -295 or snake.segments[0].ycor() > 295 or snake.segments[0].ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # detect collision with tail
    # if head collides with any segment in the tail:
        # trigger game_over
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()












screen.exitonclick()