class Outcome(object):
    """Name for bet, contains payout odds and calculates
    payout amount.
    """

    def __init__(self, name, odds):
        self.name = name
        self.odds = odds

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return "{name:s} ({odds:d}:1)".format_map(vars(self))

    def __repr__(self):
        return "{class_:s}({name!r}, {odds!r})".format(
            class_=type(self).__name__, **vars(self))

    def win_amount(self, n):
        return self.odds * n
