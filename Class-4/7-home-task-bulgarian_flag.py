from turtle import *

# Background Color Set (White for Bulgarian flag)
bgcolor("white")

# Green Color Rectangle
penup()
goto(-682, 135)
pendown()
color("green")  # Set pen color to green
begin_fill()
for i in range(2):
    forward(1360)
    right(90)
    forward(240)
    right(90)
end_fill()

# Red Color Rectangle
penup()
goto(-682, -105)
pendown()
color("red")  # Set pen color to Red
begin_fill()
for i in range(2):
    forward(1360)
    right(90)
    forward(240)
    right(90)
end_fill()

hideturtle()
exitonclick()
