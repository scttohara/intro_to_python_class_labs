
def main():
    read_text_file_and_split_into_two_lists()


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


if __name__ == '__main__':
    main()
