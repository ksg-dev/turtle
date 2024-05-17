import color
from turtle import Turtle, Screen


t = Turtle()
my_screen = Screen()
my_screen.colormode(255)
t.speed(0)


t.color(color.get_color())
t.circle(100)
t.right(5)

while t.heading() > 0:
    t.color(color.get_color())
    t.circle(100)
    t.right(5)
    print(t.heading())


my_screen.exitonclick()
