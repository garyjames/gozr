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
        self.ocsplit1_2 = Outcome("Split 1-2", 17)
        self.ocsplit1_4 = Outcome("Split 1-4", 17)

    def test_outcomeNames(self):
        self.assertNotEqual("00", self.oc0.name)
        self.assertEqual("00", self.oc00.name)
        self.assertEqual(self.oc1, self.oc1)
        self.assertEqual("Split 1-2", self.ocsplit1_2.name)

    def test_instances(self):
        self.assertEqual(self.oc00, self.oc00copy)
        self.assertNotEqual(self.ocsplit1_2, self.ocsplit1_4)

    def test_instances1(self):
        self.assertEqual(Outcome("00", 35), Outcome("00", 35))
        self.assertNotEqual(Outcome("2", 35), Outcome("00", 35))

    def test_win_amount(self):
        self.assertEqual(self.oc00.win_amount(0), 0)
        self.assertEqual(self.oc00.win_amount(1.1), 38.5)
        self.assertEqual(self.oc00.win_amount(10), 350)
        self.assertEqual(self.ocsplit1_2.win_amount(10), 170)
        self.assertEqual(self.ocsplit1_4.win_amount(1), 17)


if __name__ == '__main__':
    unittest.main()
