from turtle import *

#page setup
penup()
goto(-250, -50)
pendown()

width = int(input("Enter a width of rectangle: "))
height = int(input("Enter a height of rectangle: "))

for i in range(2):
    forward(width)
    left(90)
    forward(height)
    left(90)

hideturtle()
exitonclick()