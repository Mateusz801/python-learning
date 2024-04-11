from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pendown()

# Challenge 1 - square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# Challenge 2 - dashed line
# for _ in range(50):
#     timmy.forward(5)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.pendown()

# Challenge 3 - more geometry
for i in range(3, 11):
    r = randint(0, 256)
    g = randint(0, 256)
    b = randint(0, 256)
    tup = (r, g, b)
    timmy.color(tup)
    for _ in range(i):
        timmy.forward(100)
        timmy.right(360 / i)

# Challenge 4 - random walk

screen.exitonclick()
