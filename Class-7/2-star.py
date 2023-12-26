from turtle import *

goto(-150, 0)
bgcolor("black")
color("yellow")
speed(1)

begin_fill()
points = 1

while points < 5:
    forward(250)
    left(145)
    points = points + 1
end_fill()
hideturtle()
exitonclick()