from unittest import TestCase
from roulette.game import Odds


class TestGameOdds(TestCase):
    def test_odds(self):
        self.odds = Odds()
        self.assertEqual(self.odds.straight, 35)
        self.assertEqual(self.odds.split, 17)
        self.assertEqual(self.odds.street, 11)
        self.assertEqual(self.odds.corner, 8)
        self.assertEqual(self.odds.basket, 6)
        self.assertEqual(self.odds.line, 5)
        self.assertEqual(self.odds.dozen, 2)
        self.assertEqual(self.odds.column, 2)
        self.assertEqual(self.odds.odd, 1)
        self.assertEqual(self.odds.even, 1)
        self.assertEqual(self.odds.red, 1)
        self.assertEqual(self.odds.black, 1)
        self.assertEqual(self.odds.high, 1)
        self.assertEqual(self.odds.low, 1)
