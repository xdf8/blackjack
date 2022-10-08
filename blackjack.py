from functions import get_user_action
from functions import select_card_remove_from_deck

card_colors = ["♥️", "♦️", "♠️", "♣️"]
card_faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card_values = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}
card_deck = []

# generate all card combinations
for color in card_colors:
    for value in card_faces:
        card_deck.append(f"{value} of {color}")

player_cards = [
    select_card_remove_from_deck(card_deck),
    select_card_remove_from_deck(card_deck),
]
dealer_cards = [
    select_card_remove_from_deck(card_deck),
    select_card_remove_from_deck(card_deck),
]

print(f"Dealer has: {dealer_cards}")
print(f"Your cards are: {player_cards}")

user_action = get_user_action()

print(user_action)
# dealer must hit on 16 and stand on 17 or more
