import colorgram
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("circle")
Screen().colormode(255)

# extract colors from an image

# colors = colorgram.extract("hirst_spot_painting.jpg", 25)
#
# color = []
# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# for i in range(25):
#     first_color = colors[i]
#     r = first_color.rgb.r
#     g = first_color.rgb.g
#     b = first_color.rgb.b
#     rgb_color = (r, g, b)
#     #hsl = first_color.hsl # e.g. (230, 255, 203)
#     color.append(rgb_color)
#
# print(color)

# current color list from the extraction -> deleted the white colors per hand
color_list =  [(236, 35, 108), (221, 231, 237), (145, 28, 66), (239, 75, 35), (7, 148, 95), (220, 171, 45), (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91), (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35), (239, 162, 193), (145, 27, 25), (243, 167, 156), (163, 211, 178), (26, 187, 225)]
tim.speed(0)
tim.setheading(225)
tim.penup() # draw dots we don't need the lines or pen down in this case
tim.hideturtle() # we also don't need a turtle
tim.forward(350) # sets the beginning in the left corner with the setheading(225) from before
tim.setheading(0)
def hirst_(number_of_dots):
    for i in range(1, number_of_dots+1):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
        if i %10 ==0: # if it is tenth counter we go to the new line
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

hirst_(100)

screen = Screen()
screen.exitonclick()