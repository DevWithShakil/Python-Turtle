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

# Orange Ring
penup()
goto(0, 0)
pendown()
pencolor("red")
color('orange')
begin_fill()
circle(80)
end_fill()

# Magenta Ring
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