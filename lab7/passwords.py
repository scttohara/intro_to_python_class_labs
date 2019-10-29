"""
Program to check that 2 strings (should be same password twice) match

Requirements:
Passwords Must

be at least 8 characters long.
contain at least:
one alphabetic character (a letter from a-z or A-Z);
one numeric character (a digit from 0-9);
one character that is not alphabetic or numeric (! # @ $ % for example but this is just a subset, it could be any character that you can type that is not a letter or number).

Passwords Must Not

contain spaces or dashes;
begin with an star character (*) or an ampersand (&);
contain repeating character strings of 3 or more identical characters, such as "1111" or "aaa".
"""


def main():

    i_want_to_change_password = '1'

    while i_want_to_change_password is '1':

        keep_checking_password_bool = i_want_to_change_password

        passwords_list = get_user_input()

        while keep_checking_password_bool:

            if password_is_valid(passwords_list[0]) is not True:
                keep_checking_password_bool = False

            else:
                if compare_password1_and_password2(passwords_list[0], passwords_list[1]) is True:
                    print("Congrats!! Your password was successfully saved!!!\n")
                else:
                    print("Sorry the first password you entered didn't match the second.\n\n")

                keep_checking_password_bool = False

        i_want_to_change_password = str(input("\nWould you like to start over? (Enter 1 for Yes. Enter anything else or"
                                              " press enter for No)\n"))

    print("Thanks for using the password reset-o-matic 1000...The name is a work in progress.")


def get_user_input():
    """

    :return: list. Containing two passwords entered by the user
    """
    password1 = str(input("Please enter your new password\n"))

    password2 = str(input("Please enter your new password one more time\n"))

    return [password1, password2]


def password_is_valid(password1):
    """
    a function named "password_is_valid" that returns a Boolean value. This function
    must accept a password to test as a single input parameter. This function must
    return true if the password meets all requirements and false if it does not.

    password can't be: aaaaa and something else, check assignment details.!!!!

    :param password1: string
    :return: boolean
    """
    is_valid = True

    #  Functions calls to check Password1 is valid. Results saved to variables which are checked below
    check_password_length(password1)
    contains_alpha = check_password_for_alpha(password1)
    contains_num = check_password_for_num(password1)
    contains_nonalpha_nonnum = check_password_for_special_char(password1)
    contains_space = check_password_for_space(password1)
    contains_dash = check_password_for_dash(password1)
    contains_repeating_chars = check_password_for_repeating_sequence(password1)

    #  below if statements are used to report what requirements aren't met with the given password
    if contains_alpha is False:
        is_valid = False

    if contains_num is False:
        is_valid = False

    if contains_nonalpha_nonnum is False:
        is_valid = False

    if contains_space is True:
        is_valid = False

    if contains_dash is True:
        is_valid = False

    #  below if statement, Used to avoid index out of range error
    if len(password1) > 0:
        if password1[0] is '*':
            print("You can't have an * as the first character in your password")
            is_valid = False
        if password1[0] is '&':
            print("You can't have an & as the first character in your password")
            is_valid = False

    if contains_repeating_chars is True:
        is_valid = False

    return is_valid


def check_password_length(password1):
    """
    Returns False if the password is too short and True otherwise
    :param password1: String
    :return: Boolean
    """
    if len(password1) < 8:
        print("\nPassword must be 8 characters long")
        return False
    else:
        return True


def check_password_for_alpha(password1):
    """
    Returns True if a alphabetical character exist in the string, and False otherwise
    :param password1: String
    :return: Boolean
    """
    for curr_char_in_password in password1:
        if str(curr_char_in_password).isalpha():
            return True
    print("You need at least one alphabetical character")
    return False


def check_password_for_num(password1):
    """
    Returns True if a number exist in the string and False otherwise
    :param password1: String
    :return: Boolean
    """
    for curr_char_in_password in password1:
        if str(curr_char_in_password).isnumeric():
            return True
    print("You need at least one numeric character")
    return False


def check_password_for_special_char(password1):
    """
    Returns True if a special character exist in the string, and False otherwise
    :param password1: String
    :return: Boolean
    """
    for curr_char_in_password in password1:
        if not str(curr_char_in_password).isalnum():
            return True
    print("You need at least one character that is not numeric or alphabetical (a special character)")
    return False


def check_password_for_space(password1):
    """
    Returns true if a space exist in the string and False otherwise
    :param password1: String
    :return: Boolean
    """
    for curr_char_in_password in password1:
        if str(curr_char_in_password).isspace():
            print("You can't have a space in your password")
            return True
    return False


def check_password_for_dash(password1):
    """
    Returns True if a dash exist in the string and false otherwise
    :param password1: String
    :return: Boolean
    """
    for curr_char_in_password in password1:
        if str(curr_char_in_password) is str('-'):
            print("You can't have a dash in your password")
            return True
    return False


def check_password_for_repeating_sequence(password1):
    """
    Returns True if repeating sequence exist in the string, False otherwise
    :param password1: String
    :return: Boolean
    """
    char_count_dict = {}
    placeholder = -1

    for curr_char_in_password in password1:
        placeholder += 1

        if curr_char_in_password not in char_count_dict.keys():
            char_count_dict[curr_char_in_password] = 1
        else:
            char_count_dict[curr_char_in_password] += 1

            if char_count_dict[curr_char_in_password] >= 3:
                backward_counter = placeholder

                spot_1 = password1[backward_counter]
                spot_2 = password1[backward_counter-1]
                spot_3 = password1[backward_counter-2]

                if spot_1 == spot_2 and spot_1 == spot_3 and spot_2 == spot_3:
                    print("Your password can't contain repeating character strings of 3 or more identical characters\n"
                          "i.e. 'aaa' or '2222'")
                    return True
    return False


def compare_password1_and_password2(password1, password2):
    """
    Returns True if passwords match in the string and False otherwise
    :param password1: String
    :param password2: String
    :return: boolean
    """

    if len(password1) != len(password2):
        return False

    #  Below code is taken and then modified from the lib_reverse.py from class
    for i in range(len(password1)):
        if password1[i] != password2[i]:
            return False
    return True


if __name__ == '__main__':
    main()


#  extra code below from before I changed a lot

    """
    #  below for checking if password contains at least one alphabetical, Numeric, and nonalpha-nonnumeric character
    if len(password1) < 8:

        print("\nPassword must be 8 characters long")
        is_valid = False

    contains_alpha = False
    contains_num = False
    contains_nonalpha_nonnum = False
    contains_space = False
    contains_dash = False
    placeholder = -1
    contains_repeating_chars = False


    #  Below for loop and if/elif statements are used to check the password for the different requirements
    #  for curr_char_in_password in password1:
    #    placeholder += 1

    #  if str(curr_char_in_password).isalpha() and contains_alpha is not True:
    #  contains_alpha = True

    #  elif str(curr_char_in_password).isnumeric() and contains_num is not True:
    #    contains_num = True

    #  if (not str(curr_char_in_password).isalnum()) and contains_nonalpha_nonnum is not True:
    #    contains_nonalpha_nonnum = True

    #  what the password must NOT contain is checked below
    #if str(curr_char_in_password).isspace() and contains_space is not True:
    #contains_space = True

    #  if str(curr_char_in_password) is str('-') and contains_dash is not True:
    #    contains_dash = True
    
    if curr_char_in_password not in char_count_dict.keys():
        char_count_dict[curr_char_in_password] = 1
    else:
        char_count_dict[curr_char_in_password] += 1

        if char_count_dict[curr_char_in_password] >= 3 and contains_repeating_chars is not True:
            backward_counter = placeholder

            spot_1 = password1[backward_counter]
            spot_2 = password1[backward_counter-1]
            spot_3 = password1[backward_counter-2]

            if spot_1 == spot_2 and spot_1 == spot_3 and spot_2 == spot_3:
                contains_repeating_chars = True
    
    """
