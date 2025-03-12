
"""
Turtles with a loop. 

This program has four identical lines of code to draw a square, 
but you know you can use a loop to make the program simpler. 

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

def shape(size, sides):
    for i in range(sides):
        tina.left(360/sides)
        tina.forward(size)

shape(100, 4)

size = 100
sides = 4
for i in range(sides):
        tina.left(360/sides)
        tina.forward(size)



turtle.exitonclick()                    # Close the window when we click on it
