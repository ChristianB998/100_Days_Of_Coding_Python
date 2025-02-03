from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("black")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


Screen().colormode(255)

tim.degrees(360)

degree = 5

# def draw_circle1():
#     for _ in range(360):
#         tim.forward(1)
#         tim.left(1)
for i in range(int(360/degree)):
    tim.color(random_color())
    tim.speed(10)
    tim.left(degree)
    tim.circle(100)
    #draw_circle1()


screen = Screen()
screen.exitonclick()