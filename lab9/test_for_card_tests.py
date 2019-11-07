import unittest
import card_tests


class MyTestCase(unittest.TestCase):
    #  Below tests flush

    def test_is_flush_when_there_is_a_flush(self):
        hand = [{'value': 8, 'suit': 'Clubs', 'face': '8', 'color': 'black'},
                {'value': 14, 'suit': 'Clubs', 'face': 'A', 'color': 'black'},
                {'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                {'value': 3, 'suit': 'Clubs', 'face': '3', 'color': 'red'},
                {'value': 6, 'suit': 'Clubs', 'face': '6', 'color': 'red'}]

        self.assertEqual(card_tests.is_flush(hand), True)

    def test_is_flush_when_there_is_not_a_flush(self):
        hand = [{'value': 8, 'suit': 'Clubs', 'face': '8', 'color': 'black'},
                {'value': 14, 'suit': 'Spades', 'face': 'A', 'color': 'black'},
                {'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                {'value': 3, 'suit': 'Clubs', 'face': '3', 'color': 'red'},
                {'value': 6, 'suit': 'Clubs', 'face': '6', 'color': 'red'}]

        self.assertEqual(card_tests.is_flush(hand), False)

    #  Below tests ...
    def test_is_straight_when_there_is_a_straight_numerals(self):
        hand = [{'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                {'value': 6, 'suit': 'Spades', 'face': '6', 'color': 'black'},
                {'value': 3, 'suit': 'Clubs', 'face': '3', 'color': 'black'},
                {'value': 5, 'suit': 'Hearts', 'face': '5', 'color': 'red'},
                {'value': 4, 'suit': 'Clubs', 'face': '4', 'color': 'red'}]

        self.assertEqual(card_tests.is_straight(hand), True)

    def test_is_straight_when_there_is_a_straight_numerals_and_face(self):
        hand = [{'value': 11, 'suit': 'Clubs', 'face': 'J', 'color': 'black'},
                {'value': 14, 'suit': 'Spades', 'face': 'A', 'color': 'black'},
                {'value': 13, 'suit': 'Clubs', 'face': 'K', 'color': 'black'},
                {'value': 12, 'suit': 'Hearts', 'face': 'Q', 'color': 'red'},
                {'value': 10, 'suit': 'Clubs', 'face': '10', 'color': 'red'}]

        self.assertEqual(card_tests.is_straight(hand), True)

    def test_is_straight_when_there_is_no_straight(self):
        hand = [{'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                {'value': 14, 'suit': 'Spades', 'face': 'A', 'color': 'black'},
                {'value': 13, 'suit': 'Clubs', 'face': 'K', 'color': 'black'},
                {'value': 12, 'suit': 'Hearts', 'face': 'Q', 'color': 'red'},
                {'value': 10, 'suit': 'Clubs', 'face': '10', 'color': 'red'}]

        self.assertEqual(card_tests.is_straight(hand), False)

    def test_is_straight_flush_when_there_is_no_straight_but_is_flush(self):
        hand = [{'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                {'value': 14, 'suit': 'Clubs', 'face': 'A', 'color': 'black'},
                {'value': 13, 'suit': 'Clubs', 'face': 'K', 'color': 'black'},
                {'value': 12, 'suit': 'Clubs', 'face': 'Q', 'color': 'red'},
                {'value': 5, 'suit': 'Clubs', 'face': '10', 'color': 'red'}]

        self.assertEqual(card_tests.is_straight_flush(hand), False)

    def test_is_straight_flush_when_there_is_straight_but_no_flush(self):
        hand = [{'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                {'value': 3, 'suit': 'Spades', 'face': '3', 'color': 'black'},
                {'value': 4, 'suit': 'Clubs', 'face': '4', 'color': 'black'},
                {'value': 5, 'suit': 'Clubs', 'face': '5', 'color': 'red'},
                {'value': 6, 'suit': 'Clubs', 'face': '6', 'color': 'red'}]

        self.assertEqual(card_tests.is_straight_flush(hand), False)

    def test_is_straight_flush_when_there_is_straight_and_flush(self):
        hand = [{'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                {'value': 3, 'suit': 'Clubs', 'face': '3', 'color': 'black'},
                {'value': 4, 'suit': 'Clubs', 'face': '4', 'color': 'black'},
                {'value': 5, 'suit': 'Clubs', 'face': '5', 'color': 'red'},
                {'value': 6, 'suit': 'Clubs', 'face': '6', 'color': 'red'}]

        self.assertEqual(card_tests.is_straight_flush(hand), True)

    def test_is_pair_when_pair_exist(self):
        hand = [{'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                {'value': 2, 'suit': 'Hearts', 'face': '2', 'color': 'black'},
                {'value': 4, 'suit': 'Clubs', 'face': '4', 'color': 'black'},
                {'value': 5, 'suit': 'Clubs', 'face': '5', 'color': 'red'},
                {'value': 6, 'suit': 'Clubs', 'face': '6', 'color': 'red'}]

        self.assertEqual(card_tests.is_pair(hand), True)

    def test_is_pair_when_2_pair_exists(self):
        hand = [{'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                {'value': 2, 'suit': 'Hearts', 'face': '2', 'color': 'black'},
                {'value': 4, 'suit': 'Clubs', 'face': '4', 'color': 'black'},
                {'value': 4, 'suit': 'Diamonds', 'face': '4', 'color': 'red'},
                {'value': 6, 'suit': 'Clubs', 'face': '6', 'color': 'red'}]

        self.assertEqual(card_tests.is_pair(hand), False)

    def test_is_pair_when_3_pair_exists(self):
        hand = [{'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                {'value': 2, 'suit': 'Hearts', 'face': '2', 'color': 'black'},
                {'value': 4, 'suit': 'Clubs', 'face': '4', 'color': 'black'},
                {'value': 4, 'suit': 'Diamonds', 'face': '4', 'color': 'red'},
                {'value': 4, 'suit': 'Clubs', 'face': '4', 'color': 'red'}]

        self.assertEqual(card_tests.is_pair(hand), False)

    def test_is_pair_when_full_house_exist(self):
        hand = [{'value': 12, 'suit': 'Clubs', 'face': 'Q', 'color': 'black'},
                 {'value': 12, 'suit': 'Spades', 'face': 'Q', 'color': 'black'},
                 {'value': 8, 'suit': 'Spades', 'face': '8', 'color': 'black'},
                 {'value': 12, 'suit': 'Hearts', 'face': 'Q', 'color': 'red'},
                 {'value': 8, 'suit': 'Clubs', 'face': '8', 'color': 'red'}]

        self.assertEqual(card_tests.is_pair(hand), False)

    def test_is_high_card_when_flush_exist(self):
        hand = [{'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                {'value': 2, 'suit': 'Hearts', 'face': '2', 'color': 'black'},
                {'value': 4, 'suit': 'Clubs', 'face': '4', 'color': 'black'},
                {'value': 4, 'suit': 'Hearts', 'face': '4', 'color': 'red'},
                {'value': 6, 'suit': 'Clubs', 'face': '6', 'color': 'red'}]

        self.assertEqual(card_tests.is_high_card(hand), False)

    def test_is_high_card_when_should_be_True(self):
        hand = [{'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                {'value': 5, 'suit': 'Clubs', 'face': '5', 'color': 'black'},
                {'value': 4, 'suit': 'Spades', 'face': '4', 'color': 'black'},
                {'value': 8, 'suit': 'Clubs', 'face': '8', 'color': 'red'},
                {'value': 10, 'suit': 'Clubs', 'face': '10', 'color': 'red'}]

        self.assertEqual(card_tests.is_high_card(hand), True)

    def test_is_2_pair_should_be_true(self):
        hand = [{'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                 {'value': 2, 'suit': 'Spades', 'face': '2', 'color': 'black'},
                 {'value': 4, 'suit': 'Spades', 'face': '4', 'color': 'black'},
                 {'value': 4, 'suit': 'Clubs', 'face': '4', 'color': 'red'},
                 {'value': 10, 'suit': 'Clubs', 'face': '10', 'color': 'red'}]

        self.assertEqual(card_tests.is_2_pair(hand), True)

    def test_is_2_pair_should_be_false(self):
        hand = [{'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                 {'value': 2, 'suit': 'Spades', 'face': '2', 'color': 'black'},
                 {'value': 2, 'suit': 'Diamonds', 'face': '2', 'color': 'black'},
                 {'value': 4, 'suit': 'Clubs', 'face': '4', 'color': 'red'},
                 {'value': 10, 'suit': 'Clubs', 'face': '10', 'color': 'red'}]

        self.assertEqual(card_tests.is_2_pair(hand), False)

    def test_is_3_of_a_kind_should_be_true(self):
        hand = [{'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                 {'value': 2, 'suit': 'Spades', 'face': '2', 'color': 'black'},
                 {'value': 2, 'suit': 'Hearts', 'face': '2', 'color': 'black'},
                 {'value': 4, 'suit': 'Clubs', 'face': '4', 'color': 'red'},
                 {'value': 10, 'suit': 'Clubs', 'face': '10', 'color': 'red'}]

        self.assertEqual(card_tests.is_3_of_a_kind(hand), True)

    def test_is_3_of_a_kind_should_be_false_its_full_house(self):
        hand = [{'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                 {'value': 2, 'suit': 'Spades', 'face': '2', 'color': 'black'},
                 {'value': 4, 'suit': 'Spades', 'face': '2', 'color': 'black'},
                 {'value': 4, 'suit': 'Clubs', 'face': '4', 'color': 'red'},
                 {'value': 4, 'suit': 'Clubs', 'face': '4', 'color': 'red'}]

        self.assertEqual(card_tests.is_3_of_a_kind(hand), False)

    def test_is_3_of_a_kind_should_be_false_has_4_of_a_kind(self):
        hand = [{'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                 {'value': 2, 'suit': 'Spades', 'face': '2', 'color': 'black'},
                 {'value': 8, 'suit': 'Spades', 'face': '8', 'color': 'black'},
                 {'value': 2, 'suit': 'Hearts', 'face': '2', 'color': 'red'},
                 {'value': 2, 'suit': 'Diamonds', 'face': '2', 'color': 'red'}]

        self.assertEqual(card_tests.is_3_of_a_kind(hand), False)

    def test_is_3_of_a_kind_when_full_house_exist(self):
        hand = [{'value': 12, 'suit': 'Clubs', 'face': 'Q', 'color': 'black'},
                {'value': 12, 'suit': 'Spades', 'face': 'Q', 'color': 'black'},
                {'value': 8, 'suit': 'Spades', 'face': '8', 'color': 'black'},
                {'value': 12, 'suit': 'Hearts', 'face': 'Q', 'color': 'red'},
                {'value': 8, 'suit': 'Clubs', 'face': '8', 'color': 'red'}]

        self.assertEqual(card_tests.is_3_of_a_kind(hand), False)

    def test_is_4_of_a_kind_should_be_true_has_4_of_a_kind(self):
        hand1 = [{'value': 2, 'suit': 'Hearts', 'face': '2', 'color': 'black'},
                 {'value': 2, 'suit': 'Spades', 'face': '2', 'color': 'black'},
                 {'value': 8, 'suit': 'Spades', 'face': '8', 'color': 'black'},
                 {'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'red'},
                 {'value': 2, 'suit': 'Diamonds', 'face': '2', 'color': 'red'}]

        self.assertEqual(card_tests.is_4_of_a_kind(hand1), True)

    def test_is_4_of_a_kind_should_be_false(self):
        hand = [{'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                 {'value': 2, 'suit': 'Spades', 'face': '2', 'color': 'black'},
                 {'value': 8, 'suit': 'Spades', 'face': '8', 'color': 'black'},
                 {'value': 4, 'suit': 'Clubs', 'face': '4', 'color': 'red'},
                 {'value': 10, 'suit': 'Clubs', 'face': '10', 'color': 'red'}]

        self.assertEqual(card_tests.is_4_of_a_kind(hand), False)

    def test_is_4_of_a_kind_should_be_true(self):
        hand = [{'value': 12, 'suit': 'Diamonds', 'face': 'Q', 'color': 'black'},
                 {'value': 12, 'suit': 'Spades', 'face': 'Q', 'color': 'black'},
                 {'value': 8, 'suit': 'Spades', 'face': '8', 'color': 'black'},
                 {'value': 12, 'suit': 'Clubs', 'face': 'Q', 'color': 'red'},
                 {'value': 12, 'suit': 'Hearts', 'face': 'Q', 'color': 'red'}]

        self.assertEqual(card_tests.is_4_of_a_kind(hand), True)

    def test_is_full_house_should_be_true(self):
        hand = [{'value': 12, 'suit': 'Clubs', 'face': 'Q', 'color': 'black'},
                 {'value': 12, 'suit': 'Spades', 'face': 'Q', 'color': 'black'},
                 {'value': 8, 'suit': 'Spades', 'face': '8', 'color': 'black'},
                 {'value': 12, 'suit': 'Hearts', 'face': 'Q', 'color': 'red'},
                 {'value': 8, 'suit': 'Clubs', 'face': '8', 'color': 'red'}]

        self.assertEqual(card_tests.is_full_house(hand), True)

    def test_is_full_house_should_be_false(self):
        hand = [{'value': 12, 'suit': 'Clubs', 'face': 'Q', 'color': 'black'},
                 {'value': 12, 'suit': 'Spades', 'face': 'Q', 'color': 'black'},
                 {'value': 8, 'suit': 'Spades', 'face': '8', 'color': 'black'},
                 {'value': 12, 'suit': 'Hearts', 'face': 'Q', 'color': 'red'},
                 {'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'red'}]

        self.assertEqual(card_tests.is_full_house(hand), False)

    def test_is_full_house_should_be_false_has_4_of_a_kind(self):
        hand = [{'value': 12, 'suit': 'Diamonds', 'face': 'Q', 'color': 'black'},
                 {'value': 12, 'suit': 'Spades', 'face': 'Q', 'color': 'black'},
                 {'value': 8, 'suit': 'Spades', 'face': '8', 'color': 'black'},
                 {'value': 12, 'suit': 'Clubs', 'face': 'Q', 'color': 'red'},
                 {'value': 12, 'suit': 'Hearts', 'face': 'Q', 'color': 'red'}]

        self.assertEqual(card_tests.is_full_house(hand), False)

    def test_is_full_house_and_flush_should_be_true(self):
        hand = [{'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                {'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                {'value': 2, 'suit': 'Clubs', 'face': '2', 'color': 'black'},
                {'value': 4, 'suit': 'Clubs', 'face': '4', 'color': 'red'},
                {'value': 4, 'suit': 'Clubs', 'face': '4', 'color': 'red'}]

        self.assertEqual(card_tests.is_full_house(hand), True)


if __name__ == '__main__':
    unittest.main()
