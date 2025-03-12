
""""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(0)                           # Make the turtle move as fast, but not too fast. 
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "magenta", "black", "grey", "silver"]

def draw_polygon(sides):

    angle = 360/sides # Calculate angle from number of sides
    
    for i in range(sides):               # Loop through the number of sides
        tina.forward(10)                              # Move tina forward by the forward distance
        tina.left(angle)                              # Turn tina left by the left turn

tina.hideturtle()
for i in range(3,100):
    index = i % len(colors)
    print(index)
    tina.color(colors[index])
    draw_polygon(i)

draw_polygon(...)                        # Draw a square

...                                      # Move tina to another spot on the screen

draw_polygon(...)                        # Draw a pentagon

...                                      # Move tina to another spot on the screen

draw_polygon(...)                        # Draw a hexagon
'''

turtle.exitonclick()                     # Close the window when we click on it
