import os


def find_winnder(bids):
    highest_bid = 0
    bidder = ""
    for person in participants:
        bid = participants[person]
        if bid > highest_bid:
            highest_bid = bid
            bidder = person

    print(f"The winner is {bidder} with a bid of ${highest_bid}.")


print("Logos maximos")
print("Welcome to the secret auction program!")
participants = {}

auction = True

while auction:
    name = input("What is your name?")
    bid = int(input("What is your bid? $"))
    participants[name] = bid

    should_continue = input("Is there more participants? 'yes' or 'no'").lower()

    if should_continue == "no":
        auction = False
        find_winnder(participants)
    else:
        os.system('cls')

