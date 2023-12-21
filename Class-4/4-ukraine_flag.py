from turtle import *

# Background Color Set (Yellow for Ukrainian flag)
bgcolor("yellow")

# Blue Color Rectangle
penup()
goto(-682, 0)
pendown()
color("blue")  # Set pen color to blue
begin_fill()
for i in range(2):
    forward(1360)
    right(90)
    forward(342)
    right(90)
end_fill()

hideturtle()
exitonclick()
