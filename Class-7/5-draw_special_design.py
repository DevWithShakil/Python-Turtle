from turtle import *

# page setup
penup()
goto(-200, 0)
pendown()

bgcolor("white")

# Draw a special design
for i in range(36):
    forward(400)
    right(170)

hideturtle()
exitonclick()
