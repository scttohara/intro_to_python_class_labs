"""
Contains test functions for deal_and_test
"""


def is_high_card(hand):
    """

    :param hand: list of dictionaries
    :return: boolean
    """
    check_matching_faces = True
    exactly_one_pair_dict = {}
    for value in hand:

        if value['face'] not in exactly_one_pair_dict.keys():
            exactly_one_pair_dict[value['face']] = 1

        else:
            exactly_one_pair_dict[value['face']] += 1
            check_matching_faces = False

    return not is_flush(hand) and not is_straight(hand) and not is_straight_flush(hand) and check_matching_faces


def is_pair(hand):
    """

    :param hand: list of dictionaries
    :return: boolean
    """
    exactly_one_pair_dict = {}
    for value in hand:

        if value['value'] not in exactly_one_pair_dict.keys():
            exactly_one_pair_dict[value['value']] = 1
        else:
            exactly_one_pair_dict[value['value']] += 1

    #  below code checks for exactly one pair
    check_pair = False
    check_3_of_a_kind = False
    check_4_of_a_kind = False
    for values in exactly_one_pair_dict.values():
        if values == 2 and not check_pair and not check_3_of_a_kind and not check_4_of_a_kind:
            check_pair = True

        elif values == 2 and check_pair:
            check_pair = False

        if values == 3:
            check_pair = False
            check_3_of_a_kind = True

        if values == 4:
            check_pair = False
            check_4_of_a_kind = True

    return check_pair


def is_2_pair(hand):
    """

    :param hand: list of dictionaries
    :return: boolean
    """
    two_pair_dict = {}
    for value in hand:

        if value['value'] not in two_pair_dict.keys():
            two_pair_dict[value['value']] = 1
        else:
            two_pair_dict[value['value']] += 1

    #  below code checks for exactly two pair
    check_pair = False
    check_two_pair = False

    for values in two_pair_dict.values():
        if values == 2 and not check_pair:
            check_pair = True

        elif values == 2 and check_pair:
            check_two_pair = True

    return check_pair and check_two_pair


def is_3_of_a_kind(hand):
    """

    :param hand: list of dictionaries
    :return: boolean
    """
    three_of_a_kind_dict = {}
    for value in hand:

        if value['value'] not in three_of_a_kind_dict.keys():
            three_of_a_kind_dict[value['value']] = 1
        else:
            three_of_a_kind_dict[value['value']] += 1

    #  below code checks for exactly two pair
    check_for_3_of_a_kind = False
    check_for_pair = False

    for values in three_of_a_kind_dict.values():
        if values == 3:
            check_for_3_of_a_kind = True
        elif values == 2:
            check_for_pair = True

    return check_for_3_of_a_kind and not check_for_pair


def is_4_of_a_kind(hand):
    """

    :param hand: list of dictionaries
    :return: boolean
    """
    four_of_a_kind_dict = {}
    for value in hand:

        if value['value'] not in four_of_a_kind_dict.keys():
            four_of_a_kind_dict[value['value']] = 1
        else:
            four_of_a_kind_dict[value['value']] += 1

    #  below code checks for exactly two pair
    check_for_4_of_a_kind = False

    for values in four_of_a_kind_dict.values():
        if values == 4:
            check_for_4_of_a_kind = True

    return check_for_4_of_a_kind


def is_full_house(hand):
    """

    :param hand: list of dictionaries
    :return: boolean
    """
    full_house_pair_dict = {}
    for value in hand:

        if value['value'] not in full_house_pair_dict.keys():
            full_house_pair_dict[value['value']] = 1
        else:
            full_house_pair_dict[value['value']] += 1

    #  below code checks for exactly two pair
    check_for_full_house_1 = False
    check_for_full_house_2 = False

    for values in full_house_pair_dict.values():
        if values == 3:
            check_for_full_house_1 = True
        elif values == 2:
            check_for_full_house_2 = True

    return check_for_full_house_1 and check_for_full_house_2


def is_flush(hand):
    """

    :param hand: list of dictionaries
    :return: boolean
    """
    check_flush = False
    if hand[0]['suit'] == hand[1]['suit'] == hand[2]['suit'] == hand[3]['suit'] == hand[4]['suit']:
        check_flush = True

    #  Below check for straight flush

    return check_flush and not is_straight_flush(hand)


def is_straight(hand):
    """

    :param hand: list of dictionaries
    :return: boolean
    """
    sorted_hand = []
    for card in hand:
        sorted_hand.append(card['value'])

    #  puts list in ascending order
    sorted_hand.sort()

    return sorted_hand[0] == (sorted_hand[1] - 1) == (sorted_hand[2] - 2) == (sorted_hand[3] - 3) == (sorted_hand[4] - 4) and not is_straight_flush(hand)


def is_straight_flush(hand):
    """
    Uses is_flush and is_straight to check for a straight flush
    :param hand: list of dictionaries
    :return: boolean
    """
    check_flush = False
    if hand[0]['suit'] == hand[1]['suit'] == hand[2]['suit'] == hand[3]['suit'] == hand[4]['suit']:
        check_flush = True

    sorted_hand = []
    for card in hand:
        sorted_hand.append(card['value'])

    #  puts list in ascending order
    sorted_hand.sort()

    return check_flush and sorted_hand[0] == (sorted_hand[1] - 1) == (sorted_hand[2] - 2) == (sorted_hand[3] - 3) == (sorted_hand[4] - 4)
