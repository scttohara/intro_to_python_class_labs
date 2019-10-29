"""
picks two dice a given number of times. At the end the number of times each
number was rolled is output in a table format
"""

import random


def main():
    get_number_of_iterations_from_user()


def get_number_of_iterations_from_user():
    """
    prompts user for number of iterations to do.

    :return: nothing
    """

    rolls = int(input("Please enter the number of times I should roll the dice\n"))

    roll_dice(rolls)


def roll_dice(rolls):
    """
    Rolls the dice a given number of times. and then send the rolls completed and the rolls_count_dictionary.
    rolls_count_dictionary holds the number of times each given number occurred.

    :param rolls: int
    :return: nothing
    """

    rolls_done = 1

    #  holds a given number between 2 and 12 and the number of times it occurred
    rolls_count_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

    while rolls_done <= rolls:

        #  gets random number between 1 and 6 inclusive
        roll1 = random.randint(1, 6)

        #  gets random number between 1 and 6 inclusive
        roll2 = random.randint(1, 6)

        # increases the count of the occurrence of a number by 1 when it occurs
        rolls_count_dict[roll1 + roll2] += 1

        #  increases count of rolls completed
        rolls_done += 1

    #  one is subtracted because the picks_done count starts at 1
    print_output_in_table_format(rolls_done-1, rolls_count_dict)


def print_output_in_table_format(rolls_done, rolls_count_dict):
    """
    prints output information in formatted table.

    :param rolls_done: int
    :param rolls_count_dict: dictionary
    :return: nothing
    """

    print("total iteration(s): " + str(rolls_done))

    print("\nnumber   picks   percent")

    rows_printed = 2
    while rows_printed <= 12:

        #  formats the output of the table
        print('{:6}{:8}{:10}'.format(rows_printed, rolls_count_dict[rows_printed],
                                     round(rolls_count_dict[rows_printed]/rolls_done, 2)))

        rows_printed += 1


if __name__ == '__main__':
    main()
