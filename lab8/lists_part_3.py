"""
Program should read from a text file and split the capitals and states in the file into two lists.
"""
import random


def main():
    """
    reads from text file into two lists. asks the user what they want to be quizzed on then passes choice to quiz
    function
    :return: Nothing
    """
    #  states_list and capitals_list take the return values from read_text_file_...
    states_list, capitals_list = read_text_file_and_split_into_two_lists()

    #  variable used to determine if game starts over
    user_choice_to_play_again = 'yes'

    while user_choice_to_play_again == 'yes':

        state_or_capital = input("Want to be quizzed on capital names or state names? Type 1 for capitals, "
                                 "2 for states:\n")

        #  While loop makes sure user enters 1 or 2. protects against users entering long string to break program.
        while state_or_capital != '1' and state_or_capital != '2':
            state_or_capital = input("Want to be quizzed on capital names or state names? Type 1 for capitals, "
                                     "2 for states:\n")

        #  passes the users quiz choice, the states_list, and the capitals_list
        quiz_on_cap_or_states(int(state_or_capital), states_list, capitals_list)

        #  variable used to determine if game starts over
        user_choice_to_play_again = str(input("Want to play again? Type yes or no:\n").lower())


def quiz_on_cap_or_states(state_or_capital, states_list, capitals_list):

    current_random_number = random.randint(0, 49)
    if state_or_capital is 1:

        user_capital_guess = str(input("What is the capital name for the state {}? Please Type:\n".format(states_list[current_random_number])))
        final_user_capital_guess = user_capital_guess[0].upper() + user_capital_guess[1:]

        if final_user_capital_guess == capitals_list[current_random_number]:
            print("That's the right answer, CONGRATS!!!\n")
        else:
            print("Sorry, wrong answer.\n")

    elif state_or_capital is 2:

        user_state_guess = str(input("What is the state name for the capital {}? Please Type:\n".format(capitals_list[current_random_number])))
        final_user_state_guess = user_state_guess[0].upper() + user_state_guess[1:]

        if final_user_state_guess == states_list[current_random_number]:
            print("That's the right answer, CONGRATS!\n")
        else:
            print("Sorry, wrong answer.\n")


def read_text_file_and_split_into_two_lists():
    states_list = []
    capitals_list = []

    file_input = open('capitals.txt')

    count = 0
    for line in file_input:
        capital_or_state_string = str(line.strip())

        if (count % 2 is 0) or count is 0:
            states_list.append(capital_or_state_string)
        else:
            capitals_list.append(capital_or_state_string)
        count += 1

    #  print(states_list, '\n', len(states_list), '\n', capitals_list, '\n', len(capitals_list))
    return states_list, capitals_list


if __name__ == '__main__':
    main()
