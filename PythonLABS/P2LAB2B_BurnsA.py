#CTI 110
#P2LABS2B
#BurnsA
#10/17/24

#using lists and loops to draw

import turtle
t=turtle.Turtle()
#pensize and pencolor
t.pensize(7)
t.pencolor("yellow")

#simple loop
for length in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
    t.forward(length)
    t.left(90)

#more stuff pt2
t.pencolor("orange")
for length in [110, 120, 130, 140, 150, 160, 170, 180, 190, 200]:
    t.forward(length)
    t.left(90)

#pt3
t.pencolor("magenta")
for length in [210, 220, 230, 240, 250, 260, 270, 280, 290, 300]:
    t.forward(length)
    t.left(90)

#pt4
t.pencolor("purple")
for length in [310, 320, 330, 340, 350, 360, 370, 380, 390, 400]:
    t.forward(length)
    t.left(90)

#pt5
t.pencolor("lime")
for length in [410, 420, 430, 440, 450, 460, 470, 480, 490, 500]:
    t.forward(length)
    t.left(90)

#pt6
t.pencolor("green")
for length in [510, 520, 530, 540, 550, 560, 570, 580, 590, 600]:
    t.forward(length)
    t.left(90)

#pt7
t.pencolor("black")
for length in [610, 620, 630, 640, 650, 660, 670, 680, 690, 700]:
    t.forward(length)
    t.left(90)
