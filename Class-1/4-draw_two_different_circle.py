from turtle import *

# Black ring
penup()
goto(200, 0)
pendown()
pencolor("black")
color('skyblue')
begin_fill()
circle(80)
end_fill()

# Blue Ring
penup()
goto(-200, 0)
pendown()
pencolor("red")
color('magenta')
begin_fill()
circle(80)
end_fill()

hideturtle()
exitonclick()