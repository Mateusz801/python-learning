# Local scope - exists within functions
# Global scope - accessible within entire file
# Namespace - sth is valid inside scope (function, variable etc.). When you give name to sth you have to know, where it
# is

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# In Python there is no block scope.
game_lvl = 3
enemies = ["Skeleton", "Zombie", "Alien"]


def create_enemy():
    if game_lvl < 5:
        new_enemy = enemies[0]

# That doesn't work because within the function there is additional local scope. "new_enemy" variable is available
# anywhere in the function. To print it, print has to be indented.
# If one creates variable in if, while, for loop it doesn't count as creating a separate local scope.
# print(new_enemy)
    print(new_enemy)


# Modifying Global Scope - put word "global" before name of a variable
# It is better though to return f.e. increased number of enemies

# Global constants - sth you will never change, f.e. PI number. They are spelled in uppercase, with "_" instead of space

