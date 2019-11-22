import unittest
import todo
import time


class MyTodoListTestCases(unittest.TestCase):

    #  Test for add_item below
    def test_add_item_function_adds_one_item(self):
        todo_list = [{'task_name': 'empty dishwasher', 'completed': False, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean front door', 'completed': False, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())}]

        new_todo_item = {'task_name': 'fill dishwasher', 'completed': False, 'priority': 2,
                         'time_added': time.mktime(time.gmtime())}

        todo.add_item(todo_list, new_todo_item)
        self.assertEqual(todo_list, [{'task_name': 'empty dishwasher', 'completed': False, 'priority': 10,
                                      'time_added': time.mktime(time.gmtime())},
                                     {'task_name': 'Clean front door', 'completed': False, 'priority': 5,
                                      'time_added': time.mktime(time.gmtime())},
                                     {'task_name': 'fill dishwasher', 'completed': False, 'priority': 2,
                                      'time_added': time.mktime(time.gmtime())}])

    def test_add_item_function_adds_four_items(self):
        todo_list = [{'task_name': 'empty dishwasher', 'completed': False, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean front door', 'completed': False, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())}]

        new_todo_item_1 = {'task_name': 'fill dishwasher', 'completed': False, 'priority': 2,
                           'time_added': time.mktime(time.gmtime())}

        todo.add_item(todo_list, new_todo_item_1)

        new_todo_item_2 = {'task_name': 'kick dishwasher', 'completed': False, 'priority': 8,
                           'time_added': time.mktime(time.gmtime())}

        todo.add_item(todo_list, new_todo_item_2)

        new_todo_item_3 = {'task_name': 'punch dishwasher', 'completed': False, 'priority': 5,
                           'time_added': time.mktime(time.gmtime())}

        todo.add_item(todo_list, new_todo_item_3)

        new_todo_item_4 = {'task_name': 'cry about dishwasher', 'completed': False, 'priority': 10,
                           'time_added': time.mktime(time.gmtime())}

        todo.add_item(todo_list, new_todo_item_4)

        self.assertEqual(todo_list, [{'task_name': 'empty dishwasher', 'completed': False, 'priority': 10,
                                      'time_added': time.mktime(time.gmtime())},
                                     {'task_name': 'Clean front door', 'completed': False, 'priority': 5,
                                      'time_added': time.mktime(time.gmtime())},
                                     {'task_name': 'fill dishwasher', 'completed': False, 'priority': 2,
                                      'time_added': time.mktime(time.gmtime())},
                                     {'task_name': 'kick dishwasher', 'completed': False, 'priority': 8,
                                      'time_added': time.mktime(time.gmtime())},
                                     {'task_name': 'punch dishwasher', 'completed': False, 'priority': 5,
                                      'time_added': time.mktime(time.gmtime())},
                                     {'task_name': 'cry about dishwasher', 'completed': False, 'priority': 10,
                                      'time_added': time.mktime(time.gmtime())}])

    #  Should add more test for add_item function here!!!!!!!

    #  Test for show_complete function start below
    def test_show_complete_function(self):
        todo_list = [{'task_name': 'empty dishwasher', 'completed': True, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean front door', 'completed': True, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'fill dishwasher', 'completed': False, 'priority': 2,
                      'time_added': time.mktime(time.gmtime())}]

        self.assertEqual(todo.show_completed(todo_list),
                         [{'task_name': 'empty dishwasher', 'completed': True,
                           'priority': 10, 'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'Clean front door', 'completed': True, 'priority': 5,
                           'time_added': time.mktime(time.gmtime())}])

    def test_show_complete_function_should_end_up_with_empty_completed_list(self):
        todo_list = [{'task_name': 'empty dishwasher', 'completed': False, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean front door', 'completed': False, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'fill dishwasher', 'completed': False, 'priority': 2,
                      'time_added': time.mktime(time.gmtime())}]

        self.assertEqual(todo.show_completed(todo_list), [])

    #  Test for show_outstanding function start below
    def test_show_outstanding_function_should_end_up_with_three_task_in_outstanding_list(self):
        todo_list = [{'task_name': 'empty dishwasher', 'completed': False, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean front door', 'completed': False, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'fill dishwasher', 'completed': False, 'priority': 2,
                      'time_added': time.mktime(time.gmtime())}]

        self.assertEqual(todo.show_outstanding(todo_list), [{'task_name': 'empty dishwasher', 'completed': False,
                                                             'priority': 10,
                                                             'time_added': time.mktime(time.gmtime())},
                                                            {'task_name': 'Clean front door', 'completed': False,
                                                             'priority': 5,
                                                             'time_added': time.mktime(time.gmtime())},
                                                            {'task_name': 'fill dishwasher', 'completed': False,
                                                             'priority': 2,
                                                             'time_added': time.mktime(time.gmtime())}])

    def test_show_outstanding_function_should_end_up_with_empty_outstanding_list(self):
        todo_list = [{'task_name': 'empty dishwasher', 'completed': True, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean front door', 'completed': True, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'fill dishwasher', 'completed': True, 'priority': 2,
                      'time_added': time.mktime(time.gmtime())}]

        self.assertEqual(todo.show_outstanding(todo_list), [])

    #  Test for remove_completed function below
    def test_remove_completed_function_should_end_up_with_one_item_in_list(self):
        todo_list = [{'task_name': 'lay down', 'completed': False, 'priority': 2,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'empty dishwasher', 'completed': True, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean front door', 'completed': True, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean backyard', 'completed': True, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'rake leaves', 'completed': True, 'priority': 7,
                      'time_added': time.mktime(time.gmtime())}]

        todo.remove_completed(todo_list)

        self.assertEqual(todo_list, [{'task_name': 'lay down', 'completed': False, 'priority': 2,
                                      'time_added': time.mktime(time.gmtime())}])

    def test_remove_completed_function_should_end_up_with_two_item_in_list(self):
        todo_list = [{'task_name': 'lay down', 'completed': False, 'priority': 2,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'empty dishwasher', 'completed': True, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean front door', 'completed': True, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean backyard', 'completed': True, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'rake leaves', 'completed': True, 'priority': 7,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'go for run', 'completed': False, 'priority': 9,
                      'time_added': time.mktime(time.gmtime())}]

        todo.remove_completed(todo_list)

        self.assertEqual(todo_list, [{'task_name': 'lay down', 'completed': False, 'priority': 2,
                                      'time_added': time.mktime(time.gmtime())},
                                     {'task_name': 'go for run', 'completed': False, 'priority': 9,
                                      'time_added': time.mktime(time.gmtime())}])

    def test_remove_completed_function_should_end_up_with_three_item_in_list(self):
        todo_list = [{'task_name': 'lay down', 'completed': False, 'priority': 2,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'empty dishwasher', 'completed': True, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean front door', 'completed': True, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'fill dishwasher', 'completed': False, 'priority': 2,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean backyard', 'completed': True, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'rake leaves', 'completed': True, 'priority': 7,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'go for run', 'completed': False, 'priority': 9,
                      'time_added': time.mktime(time.gmtime())}]

        todo.remove_completed(todo_list)

        self.assertEqual(todo_list, [{'task_name': 'lay down', 'completed': False, 'priority': 2,
                                      'time_added': time.mktime(time.gmtime())},
                                     {'task_name': 'fill dishwasher', 'completed': False, 'priority': 2,
                                      'time_added': time.mktime(time.gmtime())},
                                     {'task_name': 'go for run', 'completed': False, 'priority': 9,
                                      'time_added': time.mktime(time.gmtime())}])

    #  Test for show_priority below
    def test_show_priority_function_testing_priority_in_first_middle_and_last(self):
        todo_list = [{'task_name': 'lay down', 'completed': False, 'priority': 2,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'empty dishwasher', 'completed': True, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean front door', 'completed': True, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'fill dishwasher', 'completed': False, 'priority': 2,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean backyard', 'completed': True, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'rake leaves', 'completed': True, 'priority': 7,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'go for run', 'completed': False, 'priority': 2,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'cut the lawn', 'completed': True, 'priority': 2,
                      'time_added': time.mktime(time.gmtime())}]

        self.assertEqual(todo.show_priority(todo_list, 2), [{'task_name': 'lay down', 'completed': False,
                                                             'priority': 2, 'time_added': time.mktime(time.gmtime())},
                                                            {'task_name': 'fill dishwasher', 'completed': False,
                                                             'priority': 2,
                                                             'time_added': time.mktime(time.gmtime())},
                                                            {'task_name': 'go for run',
                                                             'completed': False, 'priority': 2,
                                                             'time_added': time.mktime(time.gmtime())},
                                                            {'task_name': 'cut the lawn', 'completed': True,
                                                             'priority': 2,
                                                             'time_added': time.mktime(time.gmtime())}])

    def test_show_priority_function_testing_when_whole_list_is_the_same(self):
        todo_list = [{'task_name': 'lay down', 'completed': False, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'empty dishwasher', 'completed': True, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean front door', 'completed': True, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'fill dishwasher', 'completed': False, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean backyard', 'completed': True, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'rake leaves', 'completed': True, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'go for run', 'completed': False, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'cut the lawn', 'completed': True, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())}]

        self.assertEqual(todo.show_priority(todo_list, 10), todo_list)

    def test_show_priority_function_testing_when_new_list_should_be_empty(self):
        todo_list = [{'task_name': 'lay down', 'completed': False, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'empty dishwasher', 'completed': True, 'priority': 20,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean front door', 'completed': True, 'priority': 7,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'fill dishwasher', 'completed': False, 'priority': 15,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean backyard', 'completed': True, 'priority': 0,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'rake leaves', 'completed': True, 'priority': 8,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'go for run', 'completed': False, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'cut the lawn', 'completed': True, 'priority': 6,
                      'time_added': time.mktime(time.gmtime())}]

        self.assertEqual(todo.show_priority(todo_list, 1), [])

    #  Test for get_next_item below
    def test_get_next_item_eight_items_in_list(self):
        todo_list = [{'task_name': 'lay down', 'completed': False, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'empty dishwasher', 'completed': True, 'priority': 20,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean front door', 'completed': True, 'priority': 7,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'fill dishwasher', 'completed': False, 'priority': 15,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean backyard', 'completed': True, 'priority': 0,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'rake leaves', 'completed': True, 'priority': 8,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'go for run', 'completed': False, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'cut the lawn', 'completed': True, 'priority': 6,
                      'time_added': time.mktime(time.gmtime())}]

        self.assertEqual(todo.get_next_item(todo_list),
                         {'task_name': 'lay down', 'completed': False, 'priority': 10,
                          'time_added': time.mktime(time.gmtime())})

    def test_get_next_item_zero_items_in_list(self):
        todo_list = []

        self.assertEqual(todo.get_next_item(todo_list), {})

    def test_get_next_item_with_empty_item_in_list(self):
        todo_list = [{}]

        self.assertEqual(todo.get_next_item(todo_list), {})

    def test_get_next_item_with_two_items_in_list(self):
        todo_list = [{'task_name': 'lay down', 'completed': False, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'empty dishwasher', 'completed': True, 'priority': 20,
                      'time_added': time.mktime(time.gmtime())}]

        self.assertEqual(todo.get_next_item(todo_list),
                         {'task_name': 'lay down', 'completed': False, 'priority': 10,
                          'time_added': time.mktime(time.gmtime())},
                         {'task_name': 'empty dishwasher',
                          'completed': True, 'priority': 20, 'time_added': time.mktime(time.gmtime())})

    # Extra Credit sorting function tests below
    def test_sort_priority_ten_items_different_priorities_no_priority_conflicts(self):
        todo_list = [{'task_name': 'lay down', 'completed': False, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'empty dishwasher', 'completed': True, 'priority': 20,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean front door', 'completed': True, 'priority': 7,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'fill dishwasher', 'completed': False, 'priority': 15,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean backyard', 'completed': True, 'priority': 0,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'rake leaves', 'completed': True, 'priority': 8,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'go for run', 'completed': False, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'cut the lawn', 'completed': True, 'priority': 6,
                      'time_added': time.mktime(time.gmtime())}]

        todo.sort_priority(todo_list)

        self.assertEqual(todo_list,
                         [{'task_name': 'Clean backyard', 'completed': True, 'priority': 0,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'go for run', 'completed': False, 'priority': 5,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'cut the lawn', 'completed': True, 'priority': 6,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'Clean front door', 'completed': True, 'priority': 7,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'rake leaves', 'completed': True, 'priority': 8,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'lay down', 'completed': False, 'priority': 10,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'fill dishwasher', 'completed': False, 'priority': 15,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'empty dishwasher', 'completed': True, 'priority': 20,
                           'time_added': time.mktime(time.gmtime())}])

    def test_sort_priority_ten_items_with_priority_conflicts(self):
        todo_list = [{'task_name': 'lay down', 'completed': False, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'empty dishwasher', 'completed': True, 'priority': 20,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean front door', 'completed': True, 'priority': 7,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'fill dishwasher', 'completed': False, 'priority': 10,
                      'time_added': (time.mktime(time.gmtime()) + 1)},
                     {'task_name': 'Clean backyard', 'completed': True, 'priority': 0,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'rake leaves', 'completed': True, 'priority': 8,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'go for run', 'completed': False, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'cut the lawn', 'completed': True, 'priority': 6,
                      'time_added': time.mktime(time.gmtime())}]

        todo.sort_priority(todo_list)

        self.assertEqual(todo_list,
                         [{'task_name': 'Clean backyard', 'completed': True, 'priority': 0,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'go for run', 'completed': False, 'priority': 5,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'cut the lawn', 'completed': True, 'priority': 6,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'Clean front door', 'completed': True, 'priority': 7,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'rake leaves', 'completed': True, 'priority': 8,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'lay down', 'completed': False, 'priority': 10,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'fill dishwasher', 'completed': False, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 1)},
                          {'task_name': 'empty dishwasher', 'completed': True, 'priority': 20,
                           'time_added': time.mktime(time.gmtime())}])

    def test_sort_priority_ten_items_with_two_different_priority_conflicts(self):
        todo_list = [{'task_name': 'lay down', 'completed': False, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'empty dishwasher', 'completed': True, 'priority': 20,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean front door', 'completed': True, 'priority': 7,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'fill dishwasher', 'completed': False, 'priority': 10,
                      'time_added': (time.mktime(time.gmtime()) + 1)},
                     {'task_name': 'Clean backyard', 'completed': True, 'priority': 0,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'rake leaves', 'completed': True, 'priority': 8,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'go for run', 'completed': True, 'priority': 5,
                      'time_added': time.mktime(time.gmtime()) + 1},
                     {'task_name': 'cut the lawn', 'completed': True, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())}]

        todo.sort_priority(todo_list)

        self.assertEqual(todo_list,
                         [{'task_name': 'Clean backyard', 'completed': True, 'priority': 0,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'cut the lawn', 'completed': True, 'priority': 5,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'go for run', 'completed': True, 'priority': 5,
                           'time_added': (time.mktime(time.gmtime()) + 1)},
                          {'task_name': 'Clean front door', 'completed': True, 'priority': 7,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'rake leaves', 'completed': True, 'priority': 8,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'lay down', 'completed': False, 'priority': 10,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'fill dishwasher', 'completed': False, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 1)},
                          {'task_name': 'empty dishwasher', 'completed': True, 'priority': 20,
                           'time_added': time.mktime(time.gmtime())}])

    def test_sort_priority_ten_items_with_three_different_priority_conflicts(self):
        todo_list = [{'task_name': 'lay down', 'completed': False, 'priority': 10,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'empty dishwasher', 'completed': True, 'priority': 20,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'Clean front door', 'completed': True, 'priority': 8,
                      'time_added': (time.mktime(time.gmtime()) + 1)},
                     {'task_name': 'fill dishwasher', 'completed': False, 'priority': 10,
                      'time_added': (time.mktime(time.gmtime()) + 1)},
                     {'task_name': 'Clean backyard', 'completed': True, 'priority': 10,
                      'time_added': (time.mktime(time.gmtime()) + 2)},
                     {'task_name': 'rake leaves', 'completed': True, 'priority': 8,
                      'time_added': time.mktime(time.gmtime())},
                     {'task_name': 'go for run', 'completed': True, 'priority': 5,
                      'time_added': time.mktime(time.gmtime()) + 1},
                     {'task_name': 'cut the lawn', 'completed': True, 'priority': 5,
                      'time_added': time.mktime(time.gmtime())}]

        todo.sort_priority(todo_list)

        self.assertEqual(todo_list,
                         [{'task_name': 'cut the lawn', 'completed': True, 'priority': 5,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'go for run', 'completed': True, 'priority': 5,
                           'time_added': (time.mktime(time.gmtime()) + 1)},
                          {'task_name': 'rake leaves', 'completed': True, 'priority': 8,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'Clean front door', 'completed': True, 'priority': 8,
                           'time_added': (time.mktime(time.gmtime()) + 1)},
                          {'task_name': 'lay down', 'completed': False, 'priority': 10,
                           'time_added': time.mktime(time.gmtime())},
                          {'task_name': 'fill dishwasher', 'completed': False, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 1)},
                          {'task_name': 'Clean backyard', 'completed': True, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 2)},
                          {'task_name': 'empty dishwasher', 'completed': True, 'priority': 20,
                           'time_added': time.mktime(time.gmtime())}])

    def test_sort_priority_ten_items_with_same_priority_every_item_has_priority_conflicts(self):
        todo_list = [{'task_name': 'lay down', 'completed': False, 'priority': 10,
                      'time_added': (time.mktime(time.gmtime()) + 5)},
                     {'task_name': 'empty dishwasher', 'completed': True, 'priority': 10,
                      'time_added': (time.mktime(time.gmtime()) + 8)},
                     {'task_name': 'Clean front door', 'completed': True, 'priority': 10,
                      'time_added': (time.mktime(time.gmtime()) + 4)},
                     {'task_name': 'fill dishwasher', 'completed': False, 'priority': 10,
                      'time_added': (time.mktime(time.gmtime()) + 6)},
                     {'task_name': 'Clean backyard', 'completed': True, 'priority': 10,
                      'time_added': (time.mktime(time.gmtime()) + 7)},
                     {'task_name': 'rake leaves', 'completed': True, 'priority': 10,
                      'time_added': (time.mktime(time.gmtime()) + 3)},
                     {'task_name': 'go for run', 'completed': True, 'priority': 10,
                      'time_added': time.mktime(time.gmtime()) + 2},
                     {'task_name': 'cut the lawn', 'completed': True, 'priority': 10,
                      'time_added': (time.mktime(time.gmtime()) + 1)}]

        todo.sort_priority(todo_list)

        self.assertEqual(todo_list,
                         [{'task_name': 'cut the lawn', 'completed': True, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 1)},
                          {'task_name': 'go for run', 'completed': True, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 2)},
                          {'task_name': 'rake leaves', 'completed': True, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 3)},
                          {'task_name': 'Clean front door', 'completed': True, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 4)},
                          {'task_name': 'lay down', 'completed': False, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 5)},
                          {'task_name': 'fill dishwasher', 'completed': False, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 6)},
                          {'task_name': 'Clean backyard', 'completed': True, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 7)},
                          {'task_name': 'empty dishwasher', 'completed': True, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 8)}])

    def test_sort_priority_ten_items_with_same_priority_every_item_has_priority_conflicts_two_with_same_time_added(self):
        todo_list = [{'task_name': 'lay down', 'completed': False, 'priority': 10,
                      'time_added': (time.mktime(time.gmtime()) + 5)},
                     {'task_name': 'empty dishwasher', 'completed': True, 'priority': 10,
                      'time_added': (time.mktime(time.gmtime()) + 8)},
                     {'task_name': 'Clean front door', 'completed': True, 'priority': 10,
                      'time_added': (time.mktime(time.gmtime()) + 3)},
                     {'task_name': 'fill dishwasher', 'completed': False, 'priority': 10,
                      'time_added': (time.mktime(time.gmtime()) + 6)},
                     {'task_name': 'Clean backyard', 'completed': True, 'priority': 10,
                      'time_added': (time.mktime(time.gmtime()) + 7)},
                     {'task_name': 'rake leaves', 'completed': True, 'priority': 10,
                      'time_added': (time.mktime(time.gmtime()) + 3)},
                     {'task_name': 'go for run', 'completed': True, 'priority': 10,
                      'time_added': time.mktime(time.gmtime()) + 2},
                     {'task_name': 'cut the lawn', 'completed': True, 'priority': 10,
                      'time_added': (time.mktime(time.gmtime()) + 1)}]

        todo.sort_priority(todo_list)

        self.assertEqual(todo_list,
                         [{'task_name': 'cut the lawn', 'completed': True, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 1)},
                          {'task_name': 'go for run', 'completed': True, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 2)},
                          {'task_name': 'Clean front door', 'completed': True, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 3)},
                          {'task_name': 'rake leaves', 'completed': True, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 3)},
                          {'task_name': 'lay down', 'completed': False, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 5)},
                          {'task_name': 'fill dishwasher', 'completed': False, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 6)},
                          {'task_name': 'Clean backyard', 'completed': True, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 7)},
                          {'task_name': 'empty dishwasher', 'completed': True, 'priority': 10,
                           'time_added': (time.mktime(time.gmtime()) + 8)}])


if __name__ == '__main__':
    unittest.main()
