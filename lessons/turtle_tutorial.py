"""Turtle tutorial."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.color("blue", "yellow")
leo.speed(50)
leo.hideturtle()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()
bob.color(25, 120, 150)

bob.speed(50)
side_length: int = 300
i: int = 0
while (i < 100):
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(121)
    i += 1
leo.end_fill()

done()