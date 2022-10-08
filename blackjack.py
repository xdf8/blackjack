import random


def select_card_remove_from_deck(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card


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

user_action = input("Do you want to hit or stand? (h or s): ")
while user_action != "h" and user_action != "s":
    user_action = input("Please select a valid option (h or s): ")

# if user hits, add another card to their hand
if user_action == "h":
    player_cards.append(select_card_remove_from_deck(card_deck))
    print(f'Your cards are:\n {" ".join(str(x) for x in player_cards)}')
else:
    print("You stand, dealer's turn")


# if hit, select a card from the deck and add it to the player's hand
# if stand, end the
