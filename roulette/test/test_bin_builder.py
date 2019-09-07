import unittest
from roulette.game import Odds
from roulette.outcome import Outcome
from roulette.binbuilder import BinBuilder


class defaultSetup(unittest.TestCase):
    def setUp(self):
        self.builder = BinBuilder()
        self.odds = Odds()
        self.col1_gen = self.builder.col_1s
        self.col2_gen = self.builder.col_2s
        self.col3_gen = self.builder.col_3s
        self.col1_nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
        self.col2_nums = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
        self.col3_nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

        self.bins = [set() for _ in range(38)]
        for n, oc in enumerate(self.builder.split_outcomes()):
            self.bins[n] |= oc
        for n, oc in enumerate(self.builder.straight_outcomes()):
            self.bins[n] |= oc
        for n, oc in enumerate(self.builder.street_outcomes()):
            self.bins[n] |= oc
        for n, oc in enumerate(self.builder.corner_outcomes()):
            self.bins[n] |= oc
        for n, oc in enumerate(self.builder.line_outcomes()):
            self.bins[n] |= oc
        for n, oc in enumerate(self.builder.dozen_outcomes()):
            self.bins[n] |= oc


class TestColumnGenerators(defaultSetup):
    def test_ranges(self):
        self.assertTrue(self.col1_nums, range(1, 35, 3))
        self.assertTrue(self.col2_nums, range(2, 36, 3))
        self.assertTrue(self.col3_nums, range(3, 37, 3))

    @unittest.skip('TODO')
    def test_generators(self):
        self.assertEqual([i for i in self.col1_gen], self.col1_nums)
        self.assertEqual(self.col2_nums, [i for i in self.col2_gen])
        self.assertEqual(self.col3_nums, [i for i in self.col3_gen])


class ConfirmTmpBinsLength(defaultSetup):
    def test_length(self):
        self.assertTrue(len(self.builder.tmp_bins()) == 38)


class TestStraightOdds(defaultSetup):
    def test_straights(self):
        for i in range(37):
            self.assertIn(Outcome("Straight {}".format(i), self.odds.straight), self.bins[i])
        self.assertIn(Outcome("Straight 00", self.odds.straight), self.bins[37])


class TestSplitOdds(defaultSetup):
    def test_0s(self):
        self.assertTrue(Outcome("Split 0-00", self.odds.split) in self.bins[0])
        self.assertTrue(Outcome("Split 0-00", self.odds.split) in self.bins[37])

    def test_1(self):
        self.assertTrue(Outcome("Split 1-2", self.odds.split) in self.bins[1])
        self.assertTrue(Outcome("Split 1-4", self.odds.split) in self.bins[1])

    def test_5(self):
        self.assertTrue(Outcome("Split 2-5", self.odds.split) in self.bins[5])
        self.assertTrue(Outcome("Split 4-5", self.odds.split) in self.bins[5])
        self.assertTrue(Outcome("Split 5-6", self.odds.split) in self.bins[5])
        self.assertTrue(Outcome("Split 5-8", self.odds.split) in self.bins[5])

    def test_34(self):
        self.assertTrue(Outcome("Split 31-34", self.odds.split) in self.bins[34])
        self.assertTrue(Outcome("Split 34-35", self.odds.split) in self.bins[34])


class TestDozen(defaultSetup):
    def test_0(self):
        self.assertTrue(Outcome("Dozen 1", self.odds.dozen))
        self.assertTrue(Outcome("Dozen 1", self.odds.dozen) in self.bins[1])
        self.assertTrue(Outcome("Dozen 2", self.odds.dozen) in self.bins[13])
        self.assertTrue(Outcome("Dozen 3", self.odds.dozen) in self.bins[25])

    def test_1(self):
        self.assertTrue(Outcome("Dozen 1", self.odds.dozen) in self.bins[1])
        self.assertTrue(Outcome("Dozen 1", self.odds.dozen) in self.bins[2])
        self.assertTrue(Outcome("Dozen 1", self.odds.dozen) in self.bins[3])
        self.assertTrue(Outcome("Dozen 1", self.odds.dozen) in self.bins[12])

    def test_2(self):
        self.assertTrue(Outcome("Dozen 2", self.odds.dozen) in self.bins[13])
        self.assertTrue(Outcome("Dozen 2", self.odds.dozen) in self.bins[14])
        self.assertTrue(Outcome("Dozen 2", self.odds.dozen) in self.bins[15])
        self.assertTrue(Outcome("Dozen 2", self.odds.dozen) in self.bins[24])

    def test_3(self):
        self.assertTrue(Outcome("Dozen 3", self.odds.dozen) in self.bins[25])
        self.assertTrue(Outcome("Dozen 3", self.odds.dozen) in self.bins[26])
        self.assertTrue(Outcome("Dozen 3", self.odds.dozen) in self.bins[27])
        self.assertTrue(Outcome("Dozen 3", self.odds.dozen) in self.bins[36])


class AreColumnsReallyColumns(defaultSetup):
    def setUp(self) -> None:
        self.builder = BinBuilder()
        self.columns = self.builder.column()
        self.odds = Odds()

    def test_0(self):
        for n in range(1, 35, 3):
            self.assertEqual(Outcome("Column {}".format(1), self.odds.column).win_amount(10), 20)

    def test_1(self):
        for n in self.builder.col_1s:
            self.assertIn(Outcome("Column {}".format(1), self.odds.column), self.columns[n])

    def test_2(self):
        for n in self.builder.col_2s:
            self.assertIn(Outcome("Column {}".format(2), self.odds.column), self.columns[n])


class TestAllOutcomes(defaultSetup):
    def test_street(self):
        oc_name = "Street"
        for row in self.builder.col_1s:
            for n in [row, row + 1, row + 2]:
                self.assertIn(Outcome("{} {}-{}-{}".format(oc_name, row, row + 1, row + 2),
                                      self.odds.street), self.bins[n])

    def test_corner(self):
        oc_name = "Corner"
        for row in range(1, 32, 3):
            for i in [0, 1, 3, 4]:
                self.assertIn(
                    Outcome("{} {}-{}-{}-{}".format(oc_name, row, row + 1, row + 3, row + 4), self.odds.corner),
                    self.bins[row + i])
        for row in range(2, 33, 3):
            for i in [0, 1, 3, 4]:
                self.assertIn(
                    Outcome("{} {}-{}-{}-{}".format(oc_name, row, row + 1, row + 3, row + 4), self.odds.corner),
                    self.bins[row + i])

    def test_line(self):
        for i in range(1, 34, 3):
            oc = ["Line", i, i + 1, i + 2, i + 3, i + 4, i + 5]
            for j in range(6):
                self.assertIn(Outcome("{} {}-{}-{}-{}-{}-{}".format(*oc), self.odds.line), self.bins[i + j])

    def test_straights(self):
        for i in range(1, 37):
            self.assertIn(Outcome("Straight {}".format(i), self.odds.straight), self.bins[i])
        self.assertIn(Outcome("Straight {}".format('00'), self.odds.straight), self.bins[37])

    def test_splits(self):
        for i in self.builder.col_1s:
            self.assertIn(Outcome("Split {}-{}".format(i, i + 1), self.odds.split), self.bins[i])
            self.assertIn(Outcome("Split {}-{}".format(i, i + 1), self.odds.split), self.bins[i + 1])
        for i in self.builder.col_2s:
            self.assertIn(Outcome("Split {}-{}".format(i, i + 1), self.odds.split), self.bins[i])
            self.assertIn(Outcome("Split {}-{}".format(i, i + 1), self.odds.split), self.bins[i + 1])

        self.assertIn(Outcome("Split 0-00", self.odds.split), self.bins[0])
        self.assertIn(Outcome("Split 0-00", self.odds.split), self.bins[37])

