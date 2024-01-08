import turtle
import time
import random

# Score and delay
score = 0
high_score = 0
delay = 0.06

# Set up the screen
wn = turtle.Screen()
wn.title('Snake Game by Arpit')
wn.bgcolor("green")
wn.setup(width=700, height=700)
wn.tracer(0)  # Turns off screen updates

# Outline of the playing field
pencil = turtle.Turtle()
pencil.speed(0)
pencil.shape('circle')
pencil.color('black')
pencil.penup()
pencil.hideturtle()
pencil.goto(310, 310)
pencil.pendown()
pencil.goto(-310, 310)
pencil.goto(-310, -310)
pencil.goto(310, -310)
pencil.goto(310, 310)
pencil.penup()

# Snake head
head = turtle.Turtle()
head.speed(0)  # 0 is the maximum animation speed of the turtle module
head.shape("circle")
head.color('black')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# Snake Food
food = turtle.Turtle()
food.speed(0)  # 0 is the maximum animation speed of the turtle module
food.shape("square")
food.color('red')
food.penup()
food.goto(0, 100)

# Contains information about snake body
segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('circle')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write('Score: 0 High Score: 0', align='center', font=('Courier', 24, 'normal'))

# Makes the window visible and runs everythings
wn.mainloop()
# Rest of the code (functions and game loop)...
