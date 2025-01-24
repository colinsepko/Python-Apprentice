"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Background Image"


Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""

import turtle
import random
turtle.setup (width=600, height=600, startx=0, starty=0)

bozo = turtle.Turtle()
bozo.penup()
bozo.goto(0, -225)
bozo.pendown()

bozo.shape("triangle")
bozo.speed(100)

turtle_colors = [
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

index = random.randint(0, len(turtle_colors)-1)


for i in range(250):
    bozo.circle(i)
    index += (random.randint(0, 10) - 5)
    if index >= len(turtle_colors):
        index -= len(turtle_colors)
    elif index < 0:
        index += len(turtle_colors)
    bozo.pencolor(turtle_colors[index])

bozo.pencolor("black")

for i in range(75):
    bozo.circle(i**1.2)

turtle.exitonclick()
