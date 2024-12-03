#P4LAB1
#CTI 110
#BurnsA
#11/12/24

import turtle
#win=turtle.Screen()
t=turtle.Turtle()

#add some display options

t.pensize(15)
t.pencolor("light blue")
t.shape("turtle")
"""
#triangle
for side in range(3):
    t.forward(100)
    t.right(120)

#trip[py triamge
t.pencolor("blue")
t.pensize("5")
for side in range(30):
    t.forward(100)
    t.right(140)

#swuarre
t.pencolor("teal")
t.pensize("3")
t.forward(100)
for side in range(4):
    t.forward(100)
    t.right(90)
"""

#snowflake
t.pensize("5")
t.speed(0)
t.pencolor("white")
for flake in range(1000):
    color=("cornflowerblue")
    t.pencolor(color)
    t.forward(120)
    t.left(90)
    t.forward(20)
    t.back(20)
    t.right(180)
    t.forward(20)
    t.back(20)
    t.left(90)
    t.back(120)
    t.left(28)
