from turtle import *

# page setup
penup()
goto(-100, 0)
pendown()

# Draw simple way
# forward(200)
# left(120)
# forward(200)
# left(120)
# forward(200)

# Draw using loop
for i in range(3):
    forward(200)
    left(120)


hideturtle()
exitonclick()
