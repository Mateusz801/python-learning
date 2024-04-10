# Data types:
# Strings - creating with double quotes

# SUBSCRIPTING - "string"[position]
# It's getting character of specified position
h = "HELLO"[0]

# Integer
# Big integers may be specified with underscores, f.e.
big_int = 123_2421_2413

# Float
# When number has decimal places
PI = 3.14

# Boolean
t = True
f = False

# One can not concatenate strings with numbers in print() function
# Check the type -> type(variable)

# Conversion
# desired_type(variable)
num_char = len("blablabla")
new_num_char = str(num_char)

# Ex 1
two_digit = input("Input two digit number: ")
print(int(two_digit[0]) + int(two_digit[1]))

# Mathematics operations
# When dividing, one always gets 'float'

# BMI calculator
height = float(input("Enter your height [m]: "))
weight = int(input("Enter your weigth [kg]: "))

print(int(weight / height**2))

# Rounding a number to specific number of decimal places
print(round(8 / 3, 2))

# Floor divison gives integer
print(type(8 // 3))

# f-String - provides a way to concatenate strings and numbers
score = 0
print(f"Your score is {score}, your height is {height}")

# Ex 3
age = int(input("Enter your age: "))
weeks = (90 - age) * 52
print(f"You have {weeks} weeks left :)_(:")
