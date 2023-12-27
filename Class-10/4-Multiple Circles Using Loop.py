from turtle import *
penup()
goto(-200,0)
pendown()
# Draw multiple circles using a loop
for i in range(5):
    circle(50)  # You can customize the radius as needed
    penup()
    forward(100)  # Move forward for the next circle
    pendown()

# Keep the window open
hideturtle()
exitonclick()
