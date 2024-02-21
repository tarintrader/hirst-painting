from turtle import Turtle, Screen
import random

color_list = [(197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53), (136, 162, 181),
              (131, 34, 22), (69, 39, 32), (53, 117, 86), (192, 95, 78), (146, 177, 149), (19, 91, 68), (165, 143, 157),
              (31, 59, 76), (111, 75, 81), (228, 176, 164), (128, 29, 33), (179, 204, 177), (71, 34, 36), (25, 82, 89),
              (89, 146, 127), (18, 69, 57), (41, 66, 90), (219, 178, 182), (175, 94, 98), (179, 192, 205),
              (104, 129, 152), (67, 64, 59), (112, 135, 140), (175, 196, 206)]

screen = Screen()
screen.colormode(255)
turtle = Turtle()
turtle.hideturtle()
turtle.penup()
turtle.speed('fastest')
y = -250
turtle.setposition(-250, y)

for _ in range (10):
    y += 50
    turtle.setposition(-250, y)
    for _ in range(10):
        turtle.dot(20, random.choice(color_list))
        turtle.forward(50)







screen.exitonclick()