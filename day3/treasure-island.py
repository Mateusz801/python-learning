print('''Welcome to Treasure Island.
Your mission is to find the treasure.''')
direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'.").lower()

if direction == "left":
    lake = input("You're at a lake. Would you like to wait for a boat or swim?\n").lower()
    if lake == "wait":
        door = input("You arrive at the island. There is a house with 3 doors: red, yellow and blue.\nWhich colour do "
                     "you choose? ").lower()
        if door == "yellow":
            print("You won!")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game over")
