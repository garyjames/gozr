from roulette.outcome import Outcome
from roulette.game import Odds


class BinBuilder(object):
    """Binbuilder
    """
    def __init__(self):
        self.odds = Odds()
        self.col_1s = BinBuilder.col_n()
        self.col_2s = BinBuilder.col_n(n=range(2, 36, 3))
        self.col_3s = BinBuilder.col_n(n=range(3, 37, 3))

    @staticmethod
    def tmp_bins():
        return [set() for _ in range(0, 38)]

    @staticmethod
    def col_n(n=range(1, 35, 3)):
        """(1, 35, 3) -> 1, 4, 7, ..., 34
        (2, 36, 3) -> 2, 5, 8, ..., 35
        (3, 37, 3) -> 3, 6, 9, ..., 36
        """
        for i in n:
            yield i

    def straight_outcomes(self, oc_name="Straight"):
        """For all numbers n such that 0 <= n < 37,
        double-zero at index 37 makes for 38 outcomes.
        """
        tmpbins = BinBuilder.tmp_bins()
        for n in range(38):
            name = "Straight {}".format(n) if n < 37 else "Straight 00"
            oc = Outcome(name, self.odds.straight)
            tmpbins[n].add(oc)
        return tmpbins

    def split_outcomes(self, oc_group="Split"):
        tmpbins = BinBuilder.tmp_bins()
        for col in self.col_1s, self.col_2s:
            for num in col:
                oc_name = "{} {}-{}".format(oc_group, num, num+1)
                tmpbins[num].add(Outcome(oc_name, self.odds.split))
                tmpbins[num+1].add(Outcome(oc_name, self.odds.split))
        for num in range(1, 34):
            oc_name = "{} {}-{}".format(oc_group, num, num+3)
            tmpbins[num].add(Outcome(oc_name, self.odds.split))
            tmpbins[num+3].add(Outcome(oc_name, self.odds.split))

        oc_name = "{} {}-{}".format(oc_group, "0", "00")
        tmpbins[0].add(Outcome(oc_name, self.odds.split))
        tmpbins[37].add(Outcome(oc_name, self.odds.split))
        return tmpbins

    def street_outcomes(self, oc_group="Street"):
        tmpbins = BinBuilder.tmp_bins()
        for row in self.col_1s:
            oc_name = "{} {}-{}-{}".format(oc_group, row, row+1, row+2)
            for i in 0, 1, 2:
                tmpbins[row+i].add(Outcome(oc_name, self.odds.street))
        return tmpbins

    def corner_outcomes(self, oc_group="Corner"):
        tmpbins = BinBuilder.tmp_bins()
        for col in range(1, 32, 3), range(2, 33, 3):
            for row in col:
                for i in [0, 1, 3, 4]:
                    oc_name = "{} {}-{}-{}-{}".format(oc_group, row, row+1, row+3, row+4)
                    tmpbins[row+i].add(Outcome(oc_name, self.odds.corner))
        return tmpbins

    def line_outcomes(self):
        tmpbins = BinBuilder.tmp_bins()
        for i in range(1, 34, 3):
            oc_name = ["Line", i, i+1, i+2, i+3, i+4, i+5]
            oc = Outcome("{} {}-{}-{}-{}-{}-{}".format(*oc_name), self.odds.line)
            for j in range(6):
                tmpbins[i+j].add(oc)
        return tmpbins

    def dozen_outcomes(self):
        tmpbins = BinBuilder.tmp_bins()
        for d in range(3):
            for n in range(12):
                name = "Dozen {}".format(d+1)
                bin_ = 12*d + n + 1
                tmpbins[bin_].add(Outcome(name, self.odds.dozen))
        return tmpbins

    def column(self):
        tmpbins = BinBuilder.tmp_bins()
        for i in range(3):
            name = "Column {}".format(i+1)
            oc = Outcome(name, self.odds.column)
            for j in getattr(self, 'col_{}s'.format(i+1)):
                tmpbins[j].add(oc)
        return tmpbins

    def high(self):
        tmpbins = BinBuilder.tmp_bins()
        name = "High"
        oc = Outcome(name, self.odds.high)
        for n in range(19, 37):
            tmpbins[n].add(oc)
        return tmpbins

    def low(self):
        tmpbins = BinBuilder.tmp_bins()
        name = "Low"
        oc = Outcome(name, self.odds.low)
        for n in range(1, 19):
            tmpbins[n].add(oc)
        return tmpbins

    def even(self):
        tmpbins = BinBuilder.tmp_bins()
        for i in range(1, 37):
            if i % 2 == 0:
                oc = Outcome("Even", self.odds.even)
                tmpbins[n].add(oc)
        return tmpbins

    def odd(self):
        tmpbins = BinBuilder.tmp_bins()
        for i in range(1, 37):
            if i % 2 != 0:
                oc = Outcome("Odd", self.odds.odd)
                tmpbins[n].add(oc)
        return tmpbins

    def red(self):
        tmpbins = BinBuilder.tmp_bins()
        red = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19,
                 21, 23, 25, 27, 30, 32, 34, 36)
        for n in red:
            oc = Outcome("Red", self.odds.red)
            tmpbins[n].add(oc)
        return tmpbins

    def black(self):
        tmpbins = BinBuilder.tmp_bins()
        black = (2, 4, 6, 8, 10, 11, 13, 15, 17, 20,
               22, 24, 26, 28, 29, 31, 33, 35)
        for n in black:
            oc = Outcome("Black", self.odds.black)
            tmpbins[n].add(oc)
        return tmpbins


if __name__ == "__main__":
    builder = BinBuilder()
