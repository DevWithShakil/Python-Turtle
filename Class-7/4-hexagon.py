from turtle import *

# page setup
penup()
goto(-50, 80)
pendown()

# iterating the loop 8 times
for i in range(8):
    forward(100)
    right(45)

hideturtle()
exitonclick()