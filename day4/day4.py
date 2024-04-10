# Randomisation
# Computers are deterministic, Python uses Mersenne Twister to generate pseudorandom numbers
# Modules can be used after importing one and can be created by programmer

import random
import my_module

# Random whole number:
random_integer = random.randint(1, 10)
print(random_integer)
print(my_module)

# To get random float other from <0,1), multiply function
random_float = random.random()
print(random_float)
random_float_bigger = 5 * random.random()

# Ex1
ex1 = random.randint(0, 1)
if ex1 == 0:
    print("Heads")
else:
    print("Tails")

# Data structure: for storing things that have relationship. They may be organized
# Lists: list = [item1, item2]
states_of_america = ["Delaware", "Pennsylvania"]

# Access item of the list:
# When it comes to starting with 0, think about that as an offset of a list
print(states_of_america[0])

# One can access list from behind using negative indexes
print(states_of_america[-1])

# Changing contents of a list:
states_of_america[1] = "Pencilvenia"
print(states_of_america[1])

# Adding an item:
states_of_america.append("MateoLando")
print(states_of_america)

# Adding multiple items:
states_of_america.extend(["ZygmuntoLand", "CracowLand"])
print(states_of_america)

# Ex2 - random item from a list
names = "Mateusz, Angelica, Zuzanna, Anna, Tomek, Jurek, Marek"
names = names.split(", ")

rand_name = random.randint(0, len(names) - 1)
print(names[rand_name])

# Trying to access index from beyond range will result in IndexError

# Nested list - a list within a list
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# Ex3
line1 = ["⬜", "⬜", "⬜"]
line2 = ["⬜", "⬜", "⬜"]
line3 = ["⬜", "⬜", "⬜"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?

vertical = position[0].upper()
horizontal = int(position[1]) - 1

# if vertical == "A":
#     vertical = 0
# elif vertical == "B":
#     vertical = 1
# elif vertical == "C":
#     vertical = 2

abc = ["A", "B", "C"]
vertical = abc.index(vertical)

map[horizontal][vertical] = "X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
