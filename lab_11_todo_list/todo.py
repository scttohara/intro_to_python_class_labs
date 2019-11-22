"""
This module contains the list manipulation functions for a todo list
"""


def add_item(todo_list, todo_new_item):
    """
    adds item to the todo list

    :param todo_list: list of dictionaries
    :param todo_new_item: list of dictionaries
    :return: Boolean
    """
    check = True
    try:
        todo_list.append(todo_new_item)
    except todo_list:
        print("Could not add new item to todo list")
        check = False

    return check


def show_completed(todo_list):
    """

    :param todo_list: list of dictionaries
    :return: new list of dictionaries with the completed tasks in it
    """
    completed_todo_list = []

    try:
        for item in todo_list:
            if item['completed']:
                completed_todo_list.append(item)
    except completed_todo_list:
        print("Issue with completed_todo_list")
    except todo_list:
        print("Issue with todo_list in show_completed")

    return completed_todo_list


def show_outstanding(todo_list):
    """
    Creates a new list with only the completed tasks from todo_list
    :param todo_list: list of dictionaries
    :return: new list of dictionaries with all task that have 'completed' marked False
    """
    outstanding_todo_list = []

    try:
        for item in todo_list:
            if not item['completed']:
                outstanding_todo_list.append(item)
    except outstanding_todo_list:
        print("Issue with outstanding list")
    except todo_list:
        print("Issue with todo_list in show_outstanding")

    return outstanding_todo_list


def remove_completed(todo_list):
    """
    Removes completed task from the original todo_list
    :param todo_list: list of dictionaries
    :return:
    """
    try:
        count = len(todo_list) - 1
        number = 0
        while number <= count:
            if todo_list[number]['completed']:
                del todo_list[number]
                count -= 1
            else:
                number += 1

    except todo_list:
        print("Issue with todo_list in remove_completed")
    except IndexError:
        print("index error in remove_completed")


def show_priority(todo_list, priority_number):
    """
    Creates a list with only the desired priority from the original todo_list
    :param todo_list: list of dictionaries
    :param priority_number: int
    :return: new_show_priority_todo_list: list of dictionaries with the desired priority
    """
    new_show_priority_todo_list = []

    try:
        for item in todo_list:
            if item['priority'] == priority_number:
                new_show_priority_todo_list.append(item)

    except priority_number:
        print("Could not create priority list, issue with priority number, show_priority()")
    except todo_list:
        print("Could not create list, issue with todo_list, show_priority()")

    return new_show_priority_todo_list


def get_next_item(todo_list):
    """
    Returns the first item in the list
    :param todo_list: list of dictionaries
    :return: next_item: dictionary, the next item in the list
    """
    next_item = {}

    try:
        if len(todo_list) > 0:
            next_item = todo_list[0]
    except next_item:
        print("next_item could not be created")

    return next_item


# Extra Credit sorting function below
# below code was taken and modified from sorting-1.py from class
def sort_priority(todo_list):
    """
    sorts the original list by priority
    :param todo_list: list of dictionaries
    :return: nothing
    """
    for index in range(len(todo_list)):
        smallest_index = find_index_of_smallest_after(todo_list, index)
        swap_values_at_indexes(todo_list, index, smallest_index)


# The next 2 methods are used in sort_priority. Above.
def find_index_of_smallest_after(todo_list, index):
    """
    Used in sort_priority function
    finds index of the smallest index after the current index

    :param todo_list: list of dictionaries
    :param index: int
    :return: smallest_index: int, location of smallest priority
    """
    smallest = todo_list[index]['priority']
    smallest_index = index
    for i in range(index, len(todo_list)):
        if todo_list[i]['priority'] < smallest:
            smallest = todo_list[i]['priority']
            smallest_index = i
        elif todo_list[i]['priority'] == smallest:
            # logic to handle two matching priorities
            if todo_list[i]['time_added'] < todo_list[smallest_index]['time_added']:
                smallest = todo_list[i]['priority']
                smallest_index = i

    return smallest_index


def swap_values_at_indexes(todo_list, first, second):
    """
    Used in sort_priority function
    swaps item in current index with item in index of next lowest priority

    :param todo_list: list of dictionaries
    :param first: int, current index
    :param second: int, lowest index
    :return: nothing
    """
    try:
        temp = todo_list[first]
        todo_list[first] = todo_list[second]
        todo_list[second] = temp
    except first:
        print("issue with first")
    except second:
        print("issue with second")
