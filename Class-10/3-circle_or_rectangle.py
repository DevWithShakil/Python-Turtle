from turtle import *

# Get user input to choose between circle and rectangle
shape = input("Enter 'circle' or 'rectangle': ")

if shape == 'circle':
    # Get user input for the radius of the circle
    radius = int(input("Enter the radius of the circle: "))
    
    # Draw the circle
    circle(radius)
elif shape == 'rectangle':
    # Get user input for the width and height of the rectangle
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))
    
    # Draw the rectangle
    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
else:
    print("Invalid shape entered. Please choose 'circle' or 'rectangle'.")

hideturtle()
exitonclick()