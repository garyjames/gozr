import unittest
from casino.roulette.outcome import Outcome
from casino.roulette.bin import Bin


class TestBin(unittest.TestCase):
    def setUp(self):
        self.oc_0 = Outcome("0", 35)
        self.oc_00 = Outcome("00", 35)
        self.oc_basket = Outcome("0-00-1-2-3", 6)
        self.oc_split_0_00 = Outcome("Split 0-00", 17)

        self.bin0 = Bin([self.oc_0, self.oc_split_0_00, self.oc_basket])
        self.bin0copy = Bin([self.oc_0, self.oc_split_0_00, self.oc_basket])
        self.bin00 = Bin([self.oc_00, self.oc_split_0_00, self.oc_basket])
        self.bin16 = Bin([Outcome("16", 35), Outcome("Red", 1),
                          Outcome("Corner 16-17-19-20", 8),
                          Outcome("Corner 13-14-16-17", 8), Outcome("Even", 1),
                          Outcome("Column 1", 2), Outcome("Line 13-16", 5),
                          Outcome("Line 16-19", 5), Outcome("Split 13-16", 17),
                          Outcome("Split 16-17", 17), Outcome("Low", 1),
                          Outcome("Split 16-19", 17),
                          Outcome("Line 16-18", 11), Outcome("Dozen 2", 2)])

    def test_oc_in_bin(self):
        for oc in (Outcome("Column 1", 2), Outcome("Split 16-17", 17),
                   Outcome("Low", 1), Outcome("Line 16-19", 5)):
            assert oc in self.bin16
        assert Outcome("0-00-1-2-3", 6) in self.bin0
        assert Outcome("00", 35) in self.bin00

    def test_is_frozenset(self):
        assert isinstance(self.bin16, frozenset)

    def test_bin_length(self):
        assert len(self.bin16) == 14

    def test_bin_is_iterable(self):
        assert len([i for i in self.bin16]) == 14


if __name__ == "__main__":
    unittest.main()
