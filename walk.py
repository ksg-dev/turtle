from turtle import Turtle, Screen
import random

tes = Turtle()
my_screen = Screen()
#tes.shape("turtle")
my_screen.colormode(255)

# Correct pen settings to use on final run
tes.speed(10)
tes.shape("circle")
tes.pensize(10)
tes.shapesize(0.1, 0.1)


def get_color():
    c1 = random.randint(1, 255)
    c2 = random.randint(1, 255)
    c3 = random.randint(1, 255)
    return c1, c2, c3


directions = [0, 90, 180, 270]


for _ in range(200):
    direction = random.choice(directions)
    tes.pencolor(get_color())
    tes.setheading(direction)
    tes.forward(50)


my_screen.exitonclick()
