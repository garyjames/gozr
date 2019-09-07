
class Odds(object):
    def __init__(self):
        self._straight = 35
        self._split = 17
        self.StreetOdds = 11
        self.CornerOdds = 8
        self.BasketOdds = 6
        self.LineOdds = 5
        self.DozenOdds = 2
        self.ColumnOdds = 2
        self.OddOdds = 1
        self.EvenOdds = 1
        self.RedOdds = 1
        self.BlackOdds = 1
        self.HighOdds = 1
        self.LowOdds = 1

    @property
    def straight(self):
        return self._straight

    @property
    def split(self):
        return self._split

    @property
    def street(self):
        return self.StreetOdds

    @property
    def corner(self):
        return self.CornerOdds

    @property
    def basket(self):
        return self.BasketOdds

    @property
    def line(self):
        return self.LineOdds

    @property
    def dozen(self):
        return self.DozenOdds

    @property
    def column(self):
        return self.ColumnOdds

    @property
    def odd(self):
        return self.OddOdds

    @property
    def even(self):
        return self.EvenOdds

    @property
    def red(self):
        return self.RedOdds

    @property
    def black(self):
        return self.BlackOdds

    @property
    def high(self):
        return self.HighOdds

    @property
    def low(self):
        return self.LowOdds

