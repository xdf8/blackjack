from time import sleep

from functions import get_score
from functions import get_user_action
from functions import select_card_remove_from_deck

card_colors = ["♥️", "♦️", "♠️", "♣️"]
card_faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card_deck = []

# generate all card combinations
for color in card_colors:
    for value in card_faces:
        card_deck.append(f"{value} of {color}")

# game relevant stuff
player_cards = [
    select_card_remove_from_deck(card_deck),
    select_card_remove_from_deck(card_deck),
]
dealer_cards = [
    select_card_remove_from_deck(card_deck),
    select_card_remove_from_deck(card_deck),
]

dealer_score = get_score(dealer_cards)
player_score = get_score(player_cards)

if dealer_score == 21:
    print(f"Dealer has: {dealer_cards}")
    print(f"Your cards are: {player_cards}")
    print("Dealer has blackjack!")
    exit()

print(f"Dealer has: {dealer_cards[0]} and [hidden]")
print(f"Your cards are: {player_cards}")
print(f"Your score is: {player_score}")

if player_score == 21:
    print("You have blackjack!")
    exit()

while user_action := get_user_action() == "h":
    player_cards.append(select_card_remove_from_deck(card_deck))
    player_score = get_score(player_cards)
    print(f"Your cards are: {player_cards}")
    print(f"Your score is: {player_score}")
    if player_score > 21:
        print("You went over 21, you lose!")
        exit()
    elif player_score == 21:
        print("You have blackjack!")
        exit()

# dealer must hit on 16 and stand on 17 or more
print("Dealers turn")
print(f"Dealer has: {dealer_cards}")
while dealer_score < 17:
    sleep(1)
    dealer_cards.append(select_card_remove_from_deck(card_deck))
    dealer_score = get_score(dealer_cards)
    print(f"Dealer has: {dealer_cards}")
    print(f"Dealer score is: {dealer_score}")
    sleep(1)
    if dealer_score > 21:
        print("Dealer went over 21, you win!")
        exit()
    elif dealer_score == 21:
        print("Dealer has blackjack, you lose!")
        exit()
    elif dealer_score >= 17:
        print("Dealer has 17 or more, dealer stands")
        print(f"Dealer score is: {dealer_score}")

sleep(1)

if dealer_score > 17:
    print(f"Dealer has a score of {dealer_score}, dealer stands")

if player_score > dealer_score:
    print("You win!")
elif player_score < dealer_score:
    print("Dealer wins!")
