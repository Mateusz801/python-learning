# Loops:
# For loop:
# for item in list:
# do sth

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# Range in for
# Range is helpful for generating range of numbers <a, b)
# It is also possible to specify a step
suma = 0
for number in range(1, 101):
    suma += number
print(suma)

# Ex1 - sum even from given range
target = int(input())

total = 0
for number in range(0, target + 1, 2):
    total += number

print(total)

# Ex2 - FizzBuzz
for number in range(1, 101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
