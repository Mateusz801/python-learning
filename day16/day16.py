# Object has attributes (variables associated with our object) and methods (functions that object can do)
from turtle import Turtle, Screen
from prettytable import PrettyTable

timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkSalmon")
timmy.forward(100)

screen = Screen()
print(screen.canvheight)
screen.exitonclick()


table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

