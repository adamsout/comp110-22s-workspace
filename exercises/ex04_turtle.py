"""EX04 - Turtle Art: I will try and draw a starry landscape in the mountains hills."""

__author__ = "730392844"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """Draws the entire picture."""
    bob: Turtle = Turtle()
    grass(bob, -400, -90)
    sky(bob, -400, -90)
    mountains(bob)
    stars(bob)
    moon(bob, 100, 305)
    c_moon(bob, 125, 305)
    done()


def grass(turt: Turtle, x: float, y: float) -> None:
    """Draws the grass of the mountain range."""
    turt.speed(100)
    turt.hideturtle()
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.begin_fill()
    turt.color(25, 75, 50)
    i: int = 0
    while (i < 4):
        turt.forward(900)
        turt.right(90)
        i += 1
    turt.end_fill()


def sky(turt: Turtle, x: float, y: float) -> None:
    """Draws the sky behind the mountain range."""
    turt.speed(100)
    turt.hideturtle()
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.begin_fill()
    turt.color("dark blue")
    i: int = 0
    while (i < 4):
        turt.forward(900)
        turt.left(90)
        i += 1
    turt.end_fill()


def hills(turt: Turtle, x: float, y: float) -> None:
    """Will draw the mountains of the landscape."""
    turt.speed(100)
    turt.hideturtle()
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.begin_fill()
    turt.color("black", "black")
    i: int = 0
    while (i < 3):
        turt.forward(300)
        turt.left(120)
        i += 1
    turt.end_fill()


def mountains(bob: Turtle) -> None:
    """Will call hills in main."""
    hills(bob, -450, -100)
    hills(bob, -350, -140)
    hills(bob, -275, -80)
    hills(bob, -150, -100)
    hills(bob, -50, -120)
    hills(bob, 30, -160)
    hills(bob, 100, -115)
    hills(bob, 175, -140)


def star(turt: Turtle, x: float, y: float) -> None:
    """Draws the stars in the sky."""
    turt.speed(100)
    turt.hideturtle()
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.begin_fill()
    turt.color("yellow", "yellow")
    i: int = 0
    while (i < 18):
        turt.forward(20)
        turt.right(170)
        i += 1
    turt.end_fill()


def stars(bob: Turtle) -> None:
    """Calling all the stars to main."""
    star(bob, -300, 200)
    star(bob, -75, 300)
    star(bob, -275, 250)
    star(bob, -145, 278)
    star(bob, 200, 200)
    star(bob, 267, 378)
    star(bob, 300, 190)
    star(bob, -100, 200)
    star(bob, 250, 300)


def moon(turt: Turtle, x: float, y: float) -> None:
    """Will draw a picture of the moon."""
    turt.speed(100)
    turt.hideturtle()
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.begin_fill()
    turt.color("white", "white")
    turt.begin_fill()
    turt.circle(75)
    turt.end_fill()


def c_moon(turt: Turtle, x: float, y: float) -> None:
    """Will draw another circle to make the mmon look crescent."""
    turt.speed(100)
    turt.hideturtle()
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.begin_fill()
    turt.color("dark blue", "dark blue")
    turt.begin_fill()
    turt.circle(75)
    turt.end_fill()


if __name__ == "__main__":
    main()