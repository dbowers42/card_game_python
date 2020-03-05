import unittest
from parameterized import parameterized
from domain.card import Card


class TestCard(unittest.TestCase):
    @parameterized.expand([
        [1, "Ace"],
        [2, "2"],
        [3, "3"],
        [4, "4"],
        [5, "5"],
        [6, "6"],
        [7, "7"],
        [8, "8"],
        [9, "9"],
        [10, "10"],
        [11, "Jack"],
        [12, "Queen"],
        [13, "King"],
        [14, "Ace"]
    ])
    def test_rank_name(self, rank, name):
        """test cards ranked 1-14"""
        self.assertEqual(Card(rank, "Clubs").rank_name(), name)

    @parameterized.expand([
        [1, "Ace of Clubs"],
        [2, "2 of Clubs"],
        [3, "3 of Clubs"],
        [4, "4 of Clubs"],
        [5, "5 of Clubs"],
        [6, "6 of Clubs"],
        [7, "7 of Clubs"],
        [8, "8 of Clubs"],
        [9, "9 of Clubs"],
        [10, "10 of Clubs"],
        [11, "Jack of Clubs"],
        [12, "Queen of Clubs"],
        [13, "King of Clubs"],
        [14, "Ace of Clubs"]
    ])
    def test_display_name_with_clubs(self, rank, name):
        """test cards ranked 1-14 with a suit of clubs"""
        self.assertEqual(Card(rank, "Clubs").display_name(), name)

    @parameterized.expand([
        [1, "Ace of Spades"],
        [2, "2 of Spades"],
        [3, "3 of Spades"],
        [4, "4 of Spades"],
        [5, "5 of Spades"],
        [6, "6 of Spades"],
        [7, "7 of Spades"],
        [8, "8 of Spades"],
        [9, "9 of Spades"],
        [10, "10 of Spades"],
        [11, "Jack of Spades"],
        [12, "Queen of Spades"],
        [13, "King of Spades"],
        [14, "Ace of Spades"]
    ])
    def test_display_name_with_spades(self, rank, name):
        """test cards ranked 1-14 with a suit of spades"""
        self.assertEqual(Card(rank, "Spades").display_name(), name)

    @parameterized.expand([
        [1, "Ace of Hearts"],
        [2, "2 of Hearts"],
        [3, "3 of Hearts"],
        [4, "4 of Hearts"],
        [5, "5 of Hearts"],
        [6, "6 of Hearts"],
        [7, "7 of Hearts"],
        [8, "8 of Hearts"],
        [9, "9 of Hearts"],
        [10, "10 of Hearts"],
        [11, "Jack of Hearts"],
        [12, "Queen of Hearts"],
        [13, "King of Hearts"],
        [14, "Ace of Hearts"]
    ])
    def test_display_name_with_hearts(self, rank, name):
        """test cards ranked 1-14 with a suit of hearts"""
        self.assertEqual(Card(rank, "Hearts").display_name(), name)

    @parameterized.expand([
        [1, "Ace of Diamonds"],
        [2, "2 of Diamonds"],
        [3, "3 of Diamonds"],
        [4, "4 of Diamonds"],
        [5, "5 of Diamonds"],
        [6, "6 of Diamonds"],
        [7, "7 of Diamonds"],
        [8, "8 of Diamonds"],
        [9, "9 of Diamonds"],
        [10, "10 of Diamonds"],
        [11, "Jack of Diamonds"],
        [12, "Queen of Diamonds"],
        [13, "King of Diamonds"],
        [14, "Ace of Diamonds"]
    ])
    def test_display_name_with_diamonds(self, rank, name):
        """test cards ranked 1-14 with a suit of diamonds"""
        self.assertEqual(Card(rank, "Diamonds").display_name(), name)

    @parameterized.expand([
        [1, 15],
        [2, 5],
        [3, 5],
        [4, 5],
        [5, 5],
        [6, 5],
        [7, 5],
        [8, 5],
        [9, 5],
        [10, 10],
        [11, 10],
        [12, 10],
        [13, 10],
        [14, 15]
    ])
    def test_points(self, rank, points):
        """test cards ranked 1-14"""
        self.assertEqual(Card(rank, "Clubs").points(), points, f"it returns {points}")


if __name__ == '__main__':
    unittest.main()
