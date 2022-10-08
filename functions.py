import random


def select_card_remove_from_deck(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card


def get_user_action():
    user_action = input("Do you want to hit [h] or stand [h]?: ")
    while user_action != "h" and user_action != "s":
        user_action = input("Please select a valid option [h, s]: ")
    return user_action
