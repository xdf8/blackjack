import random


def select_card_remove_from_deck(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card


def get_user_action():
    user_action = input("Do you want to hit [h] or stand [s]?: ")
    while user_action != "h" and user_action != "s":
        user_action = input("Please select a valid option [h, s]: ")
    return user_action


def get_score(cards: list) -> int:
    score = 0
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
    for card in cards:
        card_value = card.split()[0]
        score += card_values[card_value]
    # ace can count as 1 or 11
    contains_ace = any([True if "A" in card else False for card in cards])
    if score > 21 and contains_ace:
        score -= 10
    return score
