
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""

import turtle
import random
colors = [
    # Reds
    "red", "orangered", "tomato", "indianred", "crimson", "firebrick", "darkred", "salmon", "darksalmon",
    "lightcoral", "rosybrown", "brown", "mistyrose", "lightpink", "pink", "hotpink", "deeppink", "palevioletred",
    "mediumvioletred",

    # Oranges
    "orange", "darkorange", "coral", "lightsalmon", "sandybrown", "peachpuff", "bisque", "navajowhite",
    "moccasin", "wheat", "burlywood", "tan", "chocolate", "peru", "sienna", "saddlebrown",

    # Yellows
    "yellow", "gold", "lightgoldenrodyellow", "lemonchiffon", "lightyellow", "khaki", "palegoldenrod",
    "darkkhaki", "beige", "cornsilk", "blanchedalmond", "antiquewhite", "papayawhip", "oldlace",

    # Greens
    "green", "lime", "limegreen", "springgreen", "mediumspringgreen", "lawngreen", "greenyellow", "chartreuse",
    "lightgreen", "palegreen", "darkgreen", "forestgreen", "seagreen", "mediumseagreen", "darkseagreen",
    "olive", "olivedrab", "yellowgreen", "darkolivegreen", "honeydew", "mintcream",

    # Blues
    "blue", "mediumblue", "darkblue", "navy", "royalblue", "dodgerblue", "deepskyblue", "skyblue",
    "lightskyblue", "powderblue", "lightblue", "steelblue", "cadetblue", "cornflowerblue", "mediumslateblue",
    "slateblue", "darkslateblue", "lightsteelblue",

    # Indigos and Violets
    "indigo", "purple", "darkviolet", "blueviolet", "darkorchid", "darkmagenta", "mediumorchid", "orchid",
    "violet", "plum", "thistle", "lavender", "mediumpurple", "mediumvioletred", "magenta", "fuchsia",

    # Others (Whites, Grays, Blacks)
    "white", "whitesmoke", "snow", "gainsboro", "lightgray", "silver", "darkgray", "gray", "dimgray",
    "slategray", "darkslategray", "black", "aliceblue", "ghostwhite", "azure", "lavenderblush", "seashell",
    "floralwhite", "ivory", "mintcream", "linen"
]
turtle.setup(width=600, height=600)
tina = turtle.Turtle()

... # Your code here


def make_shape(sides, color):
    tina.pencolor(color)
    angle = 360/sides

    for i in range(sides):
        tina.left(angle)
        tina.forward(100)

def go_to_no_trail(x, y):
    tina.penup()
    tina.goto(x,y)
    tina.pendown()

for i in range(4):
    for j in range(4):
        go_to_no_trail((i*150)-200,(j*150)-250)
        make_shape(4, colors[random.randint(0, len(colors)-1)])

turtle.exitonclick()