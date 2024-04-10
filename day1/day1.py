print("Here we go again :)")
print("print('what to print')\n")

print("Hello world!\nHello world!")  # \n makes a new line in print

# Concatenate:
print("Hello " + "Mateusz!\n\n")

# Input from the user:
# input("What is your name? ")

# input() function will be executed first
print("Hello " + input("What is your name? "))

# Number of letters in given word:
print(len(input("Enter your word: ")))

# Variables:
name = input("Promptus maximus: ")
print(name)

# Variables can be changed and used in functions:
name = "Angela"
print(name)
length = len(name)
print(length)

# Putting number as a first character will result in syntax error
# NameError occurs when one tries to call variable that not exists
