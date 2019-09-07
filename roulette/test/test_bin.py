import unittest
from roulette.outcome import Outcome
from roulette.bin import Bin


class TestBin(unittest.TestCase):
    def setUp(self):
        self.oc_0 = Outcome("0", 35)
        self.oc_00 = Outcome("00", 35)
        self.oc_basket = Outcome("0-00-1-2-3", 6)
        self.oc_split_0_00 = Outcome("Split 0-00", 17)

        self.oc_16 = Outcome("16", 35)
        self.oc_line_16 = Outcome("16-17-18", 11)
        self.oc_column_1 = Outcome("Column 1", 2)
        self.oc_even = Outcome("even", 1)
        self.oc_red = Outcome("red", 1)
        self.oc_low = Outcome("low", 1)
        self.oc_2nd_dozen = Outcome("2nd Dozen", 2)
        self.oc_2line_13_16 = Outcome("2line_13_16", 5)
        self.oc_2line_16_19 = Outcome("2line_16_19", 5)
        self.oc_split_13_16 = Outcome("Split 13-16", 17)
        self.oc_split_16_17 = Outcome("Split 16-17", 17)
        self.oc_split_16_19 = Outcome("Split 16-19", 17)
        self.oc_corner_13_14_16_17 = Outcome("Corner 13-14-16-17", 8)
        self.oc_corner_16_17_19_20 = Outcome("Corner 16-17-19-20", 8)

        self.bin0 = Bin([self.oc_0, self.oc_split_0_00, self.oc_basket])
        self.bin0copy = Bin([self.oc_0, self.oc_split_0_00, self.oc_basket])
        self.bin00 = Bin([self.oc_00, self.oc_split_0_00, self.oc_basket])
        self.bin16 = Bin([self.oc_16, self.oc_red, self.oc_corner_16_17_19_20,
                          self.oc_corner_13_14_16_17, self.oc_even,
                          self.oc_column_1,self.oc_2line_13_16, self.oc_2line_16_19,
                          self.oc_split_13_16, self.oc_split_16_17, self.oc_low,
                          self.oc_split_16_19, self.oc_line_16, self.oc_2nd_dozen])
        self.bins = [set() for _ in range(38)]
        self.bins[0] |= self.bin0
        self.bins[16] |= self.bin16

    def test_attrs(self):
        self.assertTrue(getattr(self.bin0, '__next__'))
        self.assertTrue(getattr(self.bin0, 'get'))

    def test_container(self):
        self.assertTrue(self.oc_basket in self.bin0)
        self.assertTrue(Outcome("00", 35) in self.bin00)

    def test_equality(self):
        self.assertEqual(self.bin0, self.bin0copy)

    def test_methods(self):
        self.assertTrue(self.bin16.get("Split 16-17") == self.oc_split_16_17)
        self.assertEqual(self.bin16.get("Split 16-17").odds, 17)
        self.assertFalse(self.bin16.get("Split 16-19") == self.oc_split_16_17)


if __name__ == "__main__":
    unittest.main()
