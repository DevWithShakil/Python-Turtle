from turtle import *

# Background Color Set (Yellow for Austrian flag)
bgcolor("red")

# white Color Rectangle
penup()
goto(-682, 100)
pendown()
color("white")  # Set pen color to white
begin_fill()
for i in range(2):
    forward(1360)
    right(90)
    forward(200)
    right(90)
end_fill()

hideturtle()
exitonclick()
