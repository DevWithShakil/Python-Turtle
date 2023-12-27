from turtle import *
penup()
goto(-250, 50)
pendown()

# Draw a star using a loop
for _ in range(5):
        forward(500)
        right(144)

# Keep the window open
hideturtle()
exitonclick()
