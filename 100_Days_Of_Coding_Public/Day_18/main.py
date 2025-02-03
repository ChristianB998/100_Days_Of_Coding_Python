import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("turtle")
tim.color("black")
# for i in range(4):
#     """Draw square"""
#     tim.forward(100)
#     tim.right(90)

# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

def random_color():
     r = random.randint(0, 255)
     g = random.randint(0, 255)
     b = random.randint(0, 255)
     return (r, g, b)

Screen().colormode(255)
# Draw body's with +1 more sides with each round
# counter = 3
# for _ in range(10):
#     tim.color(random_color())
#     for i in range(counter):
#         tim.forward(100)
#         tim.right(360 / counter)
#     counter += 1

# Random walk
tim.pensize(10)
tim.forward(100)
tim.speed(10)
count = 0

while count < 50:
    count += 1
    tim.color(random_color())
    distance = random.randint(15, 150)
    random_num = random.randint(1, 3)
    if random_num == 1:
        tim.forward(distance)
    elif random_num == 2:
        tim.right(90)
        tim.forward(distance)
    elif random_num == 3:
        tim.left(90)
        tim.forward(distance)

## other solution for random walk
# direction = [0 , 90, 180, 270]
# for _ in range(200
#   tim.forward(30)
#   tim.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()