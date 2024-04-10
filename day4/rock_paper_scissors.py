import random as rand

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hands = [rock, paper, scissors]

choice = int(input("What do you choose? 0 - rock, 1 - paper, 2 - scissors "))
comp_choice = rand.randint(0, 2)


if choice >= 3 or choice < 0:
    print("Invalid number, you've lost!")
else:
    user_won = (choice == 0 and comp_choice) == 2 or (choice == 1 and comp_choice == 0) or (choice == 2 and comp_choice == 1)
    print(f"Your choice: {hands[choice]}\n")
    print(f"Computer's choice: {hands[comp_choice]}\n")
    if choice == comp_choice:
        print("Draw!")
    elif user_won:
        print("You've won!")
    elif not user_won:
        print("You've lost!")
