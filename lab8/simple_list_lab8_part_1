"""
two hard coded parallel lines for......


"""
STATES_LIST = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
               'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
               'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
               'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
               'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
               'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
               'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

CAPITALS_LIST = ['Montgomery', 'Juneau', 'Phoenix', 'Little Rock', 'Sacramento', 'Denver', 'Hartford', 'Dover',
                 'Tallahassee', 'Atlanta', 'Honolulu', 'Boise', 'Springfield', 'Indianapolis', 'Des Moines',
                 'Topeka', 'Frankfort', 'Baton Rouge', 'Augusta', 'Annapolis', 'Boston', 'Lansing', 'Saint Paul',
                 'Jackson', 'Jefferson City', 'Helena', 'Lincoln', 'Carson City', 'Concord', 'Trenton', 'Santa Fe',
                 'Albany', 'Raleigh', 'Bismarck', 'Columbus', 'Oklahoma City', 'Salem', 'Harrisburg', 'Providence',
                 'Columbia', 'Pierre', 'Nashville', 'Austin', 'Salt Lake City', 'Montpelier', 'Richmond', 'Olympia',
                 'Charleston', 'Madison', 'Cheyenne']


def main():
    """
    Calls user_input_state() which returns the user_selected_state which is passed to check_user_input()
    :return: Nothing
    """
    user_input = user_input_state()
    check_user_input(user_input)


def user_input_state():
    """
    user_selected_state is returned

    :return: String
    """
    user_selected_state = str(input("Please enter one of the U.S. states. If the state exist "
                                    "I'll tell you its' capital\n"))

    final_user_selected_state = user_selected_state[0].upper() + user_selected_state[1:]

    return final_user_selected_state


def check_user_input(user_selected_state):
    """

    :param user_selected_state:
    :return: Nothing
    """
    if user_selected_state in STATES_LIST:
        found_state_placeholder = STATES_LIST.index(user_selected_state)

        print('You entered {}, the capital is {}'.format(user_selected_state, CAPITALS_LIST[found_state_placeholder]))
    else:
        print("The state you entered wasn't found in our list")


if __name__ == '__main__':
    main()
