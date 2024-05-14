
from turtle import Turtle, Screen
import random

tim = Turtle()
print(tim)
tim.shape("turtle")
tim.color("Coral")


my_screen = Screen()
my_screen.colormode(255)


def get_color():
    c1 = random.randint(1, 256)
    c2 = random.randint(1, 256)
    c3 = random.randint(1, 256)
    return c1, c2, c3


sides = 3
while sides < 11:
    degree = 360/sides
    tim.pencolor(get_color())
    for i in range(sides):
        tim.forward(100)
        tim.right(degree)
    sides += 1

my_screen.exitonclick()




