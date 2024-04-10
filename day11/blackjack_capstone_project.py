from random import choice
from art import logo


def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)


def score(hand):
    return sum(hand)


def ace(hand):
    if 11 in hand and score(hand) > 21:
        hand[hand.index(11)] = 1


def compare_scores(p_score, d_score):
    if p_score > 21:
        print("You went over. You lose.")
    elif d_score == p_score:
        print("Draw.")
    elif d_score > 21:
        print("You won!")
    elif p_score > d_score:
        print("You won!")
    elif p_score < d_score:
        print("You lose.")


def game():
    print(logo)
    player_hand = []
    dealer_hand = []
    for _ in range(2):
        player_hand.append(draw_card())
        dealer_hand.append(draw_card())

    print(f"Your cards: {player_hand}, current score: {score(player_hand)}")
    print(f"Dealer's first card: {dealer_hand[0]}")

    if score(player_hand) == 21:
        print("Blackjack! You won!")
    elif score(dealer_hand) == 21:
        print("Dealer got blackjack, you lose.")
    else:
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            player_hand.append(draw_card())

        if sum(dealer_hand) < 17:
            dealer_hand.append(draw_card())

        ace(player_hand)
        ace(dealer_hand)

        player_score = sum(player_hand)
        dealer_score = sum(dealer_hand)

        print(f"Your final hand: {player_hand}, final score: {score(player_hand)}")
        print(f"Dealer's final hand: {dealer_hand}, final score: {score(dealer_hand)}")
        compare_scores(p_score=player_score, d_score=dealer_score)


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

while play == 'y':
    game()
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
