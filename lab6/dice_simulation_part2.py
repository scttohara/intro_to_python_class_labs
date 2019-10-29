"""
picks a number between 2 and 12 a given number of times. At the end the number of times each
number was picked is output in a table format
"""

import random


def main():
    get_number_of_iterations_from_user()


def get_number_of_iterations_from_user():
    """
    prompts user for number of iterations to do.

    :return: nothing
    """

    picks = int(input("Please enter the number of times I should pick a random number\n"))

    pick_numbers(picks)


def pick_numbers(picks):
    """
    Randomly picks a given number of times. and then send the rolls completed and the rolls_count_dict.
    picks_count_dict holds the number of times each given number occurred.

    :param picks: int
    :return: nothing
    """

    picks_done = 1

    #  holds a given number between 2 and 12 and the number of times it occurred
    picks_count_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

    while picks_done <= picks:

        #  randomly picks a number between 2 and 12 inclusive.
        pick = random.randint(2, 12)

        # increases the count of the occurrence of a number by 1 when it occurs
        picks_count_dict[pick] += 1

        #  increases count of picks completed
        picks_done += 1

    #  one is subtracted because the picks_done count starts at 1
    print_output_in_table_format(picks_done-1, picks_count_dict)


def print_output_in_table_format(picks_done, picks_count_dict):
    """
    prints output information in formatted table.

    :param picks_done: int
    :param picks_count_dict: dictionary
    :return: nothing
    """

    print("total iteration(s): " + str(picks_done))

    print("\nnumber   picks   percent")

    rows_printed = 2
    while rows_printed <= 12:

        #  formats the output of the table
        print('{:6}{:8}{:10}'.format(rows_printed, picks_count_dict[rows_printed],
                                     round(picks_count_dict[rows_printed] / picks_done, 2)))

        rows_printed += 1


if __name__ == '__main__':
    main()
