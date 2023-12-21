from turtle import *

# Circle Position Setup
penup()
goto(0,-200)
pendown()

# Set all color
bgcolor("green")
pencolor("red")
fillcolor("red")

# Circle Draw
begin_fill()
circle(200)
end_fill()

hideturtle()
exitonclick()