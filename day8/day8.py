# Functions with inputs
def greet(name):
    print(f"Hello {name}")


greet("Mathew")


# Parameter - name of data
# Argument - value of data

# Positional vs. Keyword arguments
def greet_with(name, location):
    print(f"Hello {name}. What is weather like in {location}?")


greet_with("Mathew", "Cracow")

# Positional argument - order of passing arguments has meaning
# Keyword argument - call function with assigning arguments to parameters
greet_with(location="Warsaw", name="Mathew")

# Ex1
from math import ceil


def paint_calc(height, width, cover):
    print(f"You'll need {ceil(height * width / cover)} cans of paint.")


test_h = int(input())  # Height of wall (m)
test_w = int(input())  # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
