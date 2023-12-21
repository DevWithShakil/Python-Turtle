from turtle import *

# Background Color Set (Maroon for Latvian flag)
bgcolor("maroon")

# white Color Rectangle
penup()
goto(-682, 50)
pendown()
color("white")  # Set pen color to white
begin_fill()
for i in range(2):
    forward(1360)
    right(90)
    forward(100)
    right(90)
end_fill()

hideturtle()
exitonclick()
