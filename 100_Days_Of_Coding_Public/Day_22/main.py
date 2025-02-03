from turtle import Screen, Turtle
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0) # if we turn the tracer off we need to manual refresh it

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update() # update the paddle after tracer is turned off

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect missing paddle
    if ball.xcor() > 350:
        ball.bounce_reset()
        scoreboard.l_point()

    # Detect R paddle misses
    if ball.xcor() < -350:
        ball.bounce_reset()
        scoreboard.r_point()

screen.exitonclick()