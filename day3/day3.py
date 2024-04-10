

# Indentation error - wrong indentation
# Comparison Operators: >; <; <=; >=; ==; !=
# if height = 120 will give SYNTAX ERROR

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
if height > 120:
    payment = 0
    print("You can ride")
    age = int(input("What is your age? "))
    if age < 12:
        payment = 5
    elif age < 18:
        payment = 7
    else:
        payment = 12

    if input("Do you want a photo? ") == "yes":
        payment += 3

    print(f"The total bill is {payment}")
else:
    print("You're too short.")


year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year!")
        else:
            print("Not a leap year :(")
    else:
        print("Leap year!")
else:
    print("No a leap year :(")


# Logical operators - and; or; not
# Love calculator
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")
names = name1 + name2
names.lower()
true = names.count("t") + names.count("r") + names.count("u") + names.count("e")
love = names.count("l") + names.count("o") + names.count("v") + names.count("e")
score = int(str(true) + str(love))

print(f"Your score is: {score}")
if score < 10 or score > 90:
    print("You are not meant to be together.")
elif 40 <= score <= 50:
    print("You're meant to be together.")
else:
    print("Only time can tell.")
