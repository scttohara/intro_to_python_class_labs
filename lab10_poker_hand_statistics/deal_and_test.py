"""
module to create a shuffle a deck of cards.
"""

import random
import card_tests
import time
import csv


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


def get_number_of_poker_hands_to_test():
    """
    uses try/exception block to protect program.

    :return: int: The number of iterations to run the program
    """
    number_is_valid = False
    hands_to_test = 0
    while not number_is_valid:
        try:
            hands_to_test = int(input("How many poker hands should we test?\n"))
            number_is_valid = True

        except ValueError:
            print("That is not a number, try again")

    return hands_to_test


def main():
    times_to_test = get_number_of_poker_hands_to_test()

    file_to_open = input('name a file to write the results to:\n')
    file_to_open = file_to_open + '.csv'

    deck = build_deck()
    #  shuffle(deck)

    straight_flush_count = 0
    high_card_count = 0
    full_house_count = 0
    pair_count = 0
    two_pair_count = 0
    three_of_a_kind_count = 0
    four_of_a_kind_count = 0
    flush_count = 0
    straight_count = 0
    count = 0

    while count < times_to_test:

        shuffle(deck)
        hand = deal_hand(deck)

        #  Nested if statements to reduce the number of functions that run to test the poker hand each iteration
        check_high_card = card_tests.is_high_card(hand)
        if check_high_card:
            high_card_count += 1
        elif not check_high_card:
            check_pair = card_tests.is_pair(hand)
            if check_pair:
                pair_count += 1
            elif not check_pair:
                check_2_pair = card_tests.is_2_pair(hand)
                if check_2_pair:
                    two_pair_count += 1
                elif not check_2_pair:
                    check_3_of_a_kind = card_tests.is_3_of_a_kind(hand)
                    if check_3_of_a_kind:
                        three_of_a_kind_count += 1
                    elif not check_3_of_a_kind:
                        check_straight = card_tests.is_straight(hand)
                        if check_straight:
                            straight_count += 1
                        elif not check_straight:
                            check_flush = card_tests.is_flush(hand)
                            if check_flush:
                                flush_count += 1
                            elif not check_flush:
                                check_full_house = card_tests.is_full_house(hand)
                                if check_full_house:
                                    full_house_count += 1
                                elif not check_full_house:
                                    check_4_of_a_kind = card_tests.is_4_of_a_kind(hand)
                                    if check_4_of_a_kind:
                                        four_of_a_kind_count += 1
                                    elif not check_4_of_a_kind:
                                        check_straight_flush = card_tests.is_straight_flush(hand)
                                        if check_straight_flush:
                                            straight_flush_count += 1

        count += 1

    total_poker_hands = 2598960

    prob_of_hand_appearing = {'straight_flush': 40 / total_poker_hands, 'high_card': 1302540 / total_poker_hands,
                              'full_house': 3744 / total_poker_hands, 'pair': 1098240 / total_poker_hands,
                              'two_pair': 123552 / total_poker_hands, 'three_of_a_kind': 54912 / total_poker_hands,
                              'four_of_a_kind': 624 / total_poker_hands, 'flush': 5108 / total_poker_hands,
                              'straight': 10200 / total_poker_hands}

    count_of_hand_appearing = {'straight_flush': straight_flush_count, 'high_card': high_card_count,
                               'full_house': full_house_count, 'pair': pair_count,
                               'two_pair': two_pair_count, 'three_of_a_kind': three_of_a_kind_count,
                               'four_of_a_kind': four_of_a_kind_count, 'flush': flush_count,
                               'straight': straight_count}

    #  try catch for opening and writing to file
    try:
        csv_file = open(file_to_open, 'w', newline='\n')
        file_headings = ['hand', 'occurrences', 'percent', 'expected', 'difference']
        csv_writer = csv.DictWriter(csv_file, fieldnames=file_headings)
        csv_writer.writeheader()

        print('\n{:20}{:26}{:26}{:30}{:34}'.format('hand', '\toccurrences', 'percent', 'expected', 'difference'))

        for key in prob_of_hand_appearing:
            print('{:20}{:15}{:21}{:27}{:32}'.format(key, count_of_hand_appearing[key],
                                                     round(count_of_hand_appearing[key] / times_to_test, 6),
                                                     round(prob_of_hand_appearing[key], 6),
                                                     round(((count_of_hand_appearing[key] / times_to_test) -
                                                            prob_of_hand_appearing[key]), 6)))

            line_to_write = {
                'hand': key, 'occurrences': count_of_hand_appearing[key],
                'percent': round(count_of_hand_appearing[key] / times_to_test, 6),
                'expected': round(prob_of_hand_appearing[key], 6),
                'difference': round(((count_of_hand_appearing[key] / times_to_test) - prob_of_hand_appearing[key]), 6),
            }

            csv_writer.writerow(line_to_write)

        csv_file.close()

    except PermissionError:
        print('Cannot open file for writing')
        print('File might be open in another program.')


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    print('\n\n--- {} seconds ---'.format(end_time))
