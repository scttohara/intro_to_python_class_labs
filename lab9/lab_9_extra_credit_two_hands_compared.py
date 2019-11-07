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
    hand_1 = []
    hand_2 = []

    for count in range(0, 10):
        if count == 0 or count % 2 == 0:
            hand_1.append(deck[count])
            #  print(count)
        else:
            hand_2.append(deck[count])

    return hand_1, hand_2


def main():
    deck = build_deck()
    shuffle(deck)

    hand_1, hand_2 = deal_hand(deck)

    print("\nHands dealt:\nHand 1:")
    for card in hand_1:
        print("{} of {}".format(card['face'], card['suit']))

    print("\nHand 2:")
    for card_2 in hand_2:
        print("{} of {}".format(card_2['face'], card_2['suit']))

    print("\nAnalysis:\n\nHands Contain:")

    #  Below passes Hand 1 to the given functions to find what it is
    check_high_card = card_tests.is_high_card(hand_1)
    check_pair = card_tests.is_pair(hand_1)
    check_2_pair = card_tests.is_2_pair(hand_1)
    check_3_of_a_kind = card_tests.is_3_of_a_kind(hand_1)
    check_4_of_a_kind = card_tests.is_4_of_a_kind(hand_1)
    check_full_house = card_tests.is_full_house(hand_1)
    check_flush = card_tests.is_flush(hand_1)
    check_straight = card_tests.is_straight(hand_1)
    check_straight_flush = card_tests.is_straight_flush(hand_1)

    #  Below passes Hand 2 to the given functions to find what it is
    check_high_card_hand_2 = card_tests.is_high_card(hand_2)
    check_pair_hand_2 = card_tests.is_pair(hand_2)
    check_2_pair_hand_2 = card_tests.is_2_pair(hand_2)
    check_3_of_a_kind_hand_2 = card_tests.is_3_of_a_kind(hand_2)
    check_4_of_a_kind_hand_2 = card_tests.is_4_of_a_kind(hand_2)
    check_full_house_hand_2 = card_tests.is_full_house(hand_2)
    check_flush_hand_2 = card_tests.is_flush(hand_2)
    check_straight_hand_2 = card_tests.is_straight(hand_2)
    check_straight_flush_hand_2 = card_tests.is_straight_flush(hand_2)

    check_hand_1 = 0

    if check_straight_flush:
        print("Hand 1: Straight flush")
        check_hand_1 = 1

    elif check_high_card:
        print("Hand 1: High card")
        check_hand_1 = 9

    elif check_full_house:
        print("Hand 1: Full house")
        check_hand_1 = 3

    elif check_pair:
        print("Hand 1: A pair")
        check_hand_1 = 8

    elif check_2_pair:
        print("Hand 1: Two pair")
        check_hand_1 = 7

    elif check_3_of_a_kind:
        print("Hand 1: 3 of a kind")
        check_hand_1 = 6

    elif check_4_of_a_kind:
        print("Hand 1: 4 of a kind")
        check_hand_1 = 2

    elif check_flush:
        print("Hand 1: A flush")
        check_hand_1 = 4

    elif check_straight:
        print("Hand 1: A straight")
        check_hand_1 = 5

    check_hand_2 = 0

    if check_straight_flush_hand_2:
        print("Hand 2: Straight flush")
        check_hand_2 = 1

    elif check_high_card_hand_2:
        print("Hand 2: High card")
        check_hand_2 = 9

    elif check_full_house_hand_2:
        print("Hand 2: Full house")
        check_hand_2 = 3

    elif check_pair_hand_2:
        print("Hand 2: A pair")
        check_hand_2 = 8

    elif check_2_pair_hand_2:
        print("Hand 2: Two pair")
        check_hand_2 = 7

    elif check_3_of_a_kind_hand_2:
        print("Hand 2: 3 of a kind")
        check_hand_2 = 6

    elif check_4_of_a_kind_hand_2:
        print("Hand 2: 4 of a kind")
        check_hand_2 = 2

    elif check_flush_hand_2:
        print("Hand 2: A flush")
        check_hand_2 = 4

    elif check_straight_hand_2:
        print("Hand 2: A straight")
        check_hand_2 = 5

    print("\nWINNER IS:")
    #  Checks who wins
    if check_hand_1 < check_hand_2:
        print("Hand 1!!!!!")

    elif check_hand_1 > check_hand_2:
        print("Hand 2!!!!!")

    elif check_hand_1 == check_hand_2:
        print("NOOO IT'S A DRAW")


if __name__ == '__main__':
    main()
