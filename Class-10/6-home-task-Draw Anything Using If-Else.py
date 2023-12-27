from turtle import *

# Page setup
penup()
goto(-150, 100)
pendown()

# Get user input for the color and shape
user_color = input("Enter the color you want to use: ")
shape = input("Enter the shape you want to draw ('circle', 'square', etc.): ")

# Set up the Turtle screen
speed(2)
color(user_color)

# Draw the requested shape
if shape == 'circle':
    # Get user input for the radius of the circle
    radius = int(input("Enter the radius of the circle: "))
    circle(radius)
elif shape == 'square':
    # Get user input for the side length of the square
    side_length = int(input("Enter the side length of the square: "))
    for _ in range(4):
        forward(side_length)
        right(90)
else:
    print(f"Sorry, I don't know how to draw a '{shape}'. Try 'circle' or 'square'.")

# Keep the window open
hideturtle()
exitonclick()
