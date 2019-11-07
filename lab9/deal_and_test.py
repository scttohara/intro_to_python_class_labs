"""
module to create a shuffle a deck of cards.
"""

import random
import card_tests


def get_card_color_from_suit(suit):
    """
    Given a string representing a card suit
    return the color of the card (red or black).
    """
    if suit == 'Spades' or suit == 'Clubs':
        return 'black'
    else:
        return 'red'


def get_card_face_from_value(value):
    """
    Given an integer representing a card value
    return the card face (2 through A).
    """
    if value <= 10:
        return str(value)
    elif value == 11:
        return 'J'
    elif value == 12:
        return 'Q'
    elif value == 13:
        return 'K'
    else:
        return 'A'


def build_deck():
    """
    Create a list representing a deck of cards. Each
    item in the list is a dictionary representing a single card.
    """
    deck = []
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    values = range(2, 15)
    for suit in suits:
        for value in values:
            card = {'value': value, 'suit': suit, 'face': get_card_face_from_value(value),
                    'color': get_card_color_from_suit(suit)}
            deck.append(card)

    return deck


def shuffle(deck):
    """
    Implement the Fischer-Yates Shuffle to shuffle the cards.
    https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
    """
    for i in range(len(deck) - 1, 0, -1):
        j = random.randint(0, i)
        temp = deck[j]
        deck[j] = deck[i]
        deck[i] = temp


def deal_hand(deck):
    """
    Create a list representing a deck of cards. Each
    item in the list is a dictionary representing a single card.
    """
    hand = []

    for count in range(0, 5):
        hand.append(deck[count])

    return hand


def main():
    deck = build_deck()
    shuffle(deck)

    hand = deal_hand(deck)

    print("\nHand dealt:\n")
    for card in hand:
        print("{} of {}".format(card['face'], card['suit']))

    print("\nAnalysis:\n\nHand contains:")

    """hand = [{'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
            {'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
            {'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
            {'value': 4, 'suit': 'Clubs', 'face': '4', 'color': 'red'},
            {'value': 4, 'suit': 'Clubs', 'face': '4', 'color': 'red'}]
    """
    check_high_card = card_tests.is_high_card(hand)
    check_pair = card_tests.is_pair(hand)
    check_2_pair = card_tests.is_2_pair(hand)
    check_3_of_a_kind = card_tests.is_3_of_a_kind(hand)
    check_4_of_a_kind = card_tests.is_4_of_a_kind(hand)
    check_full_house = card_tests.is_full_house(hand)
    check_flush = card_tests.is_flush(hand)
    check_straight = card_tests.is_straight(hand)
    check_straight_flush = card_tests.is_straight_flush(hand)

    if check_straight_flush:
        print("Straight flush")

    elif check_high_card:
        print("High card")

    elif check_full_house:
        print("Full house")

    elif check_pair:
        print("A pair")

    elif check_2_pair:
        print("Two pair")

    elif check_3_of_a_kind:
        print("3 of a kind")

    elif check_4_of_a_kind:
        print("4 of a kind")

    elif check_flush:
        print("A flush")

    elif check_straight:
        print("A straight")


if __name__ == '__main__':
    main()
