import unittest
from roulette.outcome import Outcome
from roulette.game import Odds


class TestOutcome(unittest.TestCase):
    def setUp(self):
        self.odds = Odds()
        self.oc00 = Outcome("00", 35)
        self.oc00copy = Outcome("00", self.odds.straight)
        self.oc0 = Outcome("0", 35)
        self.oc1 = Outcome("1", 35)
        self.split_1_2 = Outcome("Split 1-2", 17)
        self.split_1_4 = Outcome("Split 1-4", 17)

    def test_outcomeNames(self):
        self.assertNotEqual("00", self.oc0.name)
        self.assertEqual("00", self.oc00.name)
        self.assertEqual("Split 1-2", self.split_1_2.name)

    def test_instances(self):
        self.assertEqual(self.oc00, self.oc00copy)
        self.assertNotEqual(self.split_1_2, self.split_1_4)

    def test_instances1(self):
        self.assertEqual(Outcome("00", 35), Outcome("00", 35))
        self.assertNotEqual(Outcome("2", 35), Outcome("00", 35))

    def test_win_amount(self):
        self.assertEqual(self.oc00.win_amount(0), 0)
        self.assertEqual(self.oc00.win_amount(1.1), 38.5)
        self.assertEqual(self.oc00.win_amount(10), 350)
        self.assertEqual(self.split_1_2.win_amount(10), 170)
        self.assertEqual(self.split_1_4.win_amount(1), 17)


def test_outcome():
    o1 = Outcome("Red", 1)
    o2 = Outcome("Red", 1)
    o3 = Outcome("Black", 2)
    assert str(o1) == "Red (1:1)"
    assert repr(o2) == "Outcome(name='Red', odds=1)"
    assert o1 == o2
    assert o1.odds == 1
    assert o1.name == "Red"
    assert o1 != o3
    assert o2 != o3
