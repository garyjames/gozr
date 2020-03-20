# -*- coding: utf-8 -*-

from random import Random
from os import urandom
import logging
import sys

LOGLEVEL = logging.DEBUG

logger = logging.getLogger(__name__)
logger.setLevel(LOGLEVEL)
handler = logging.StreamHandler(sys.stdout)
# handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - '
                              '%(levelname)s - %(message)s')
# handler.setFormatter(formatter)
logger.addHandler(handler)


class Bin(frozenset):
    """Bin contains a collection of Outcomes which reflect the winning
    bets that are paid for a particular bin_ on a Odds wheel. In
    Odds, each spin of the wheel has a number of Outcomes.

    For example, a spin of 1 selects the “1” bin_ with the following
    winning Outcomes:

    “1”, “Red”, “Odd”, “Low”, “Column 1”, “Dozen 1-12”, “Split 1-2”,
    “Split 1-4”, “Street 1-2-3”, “Corner 1-2-4-5”, “Line 1-2-3-4-5-6”
    and “00-0-1-2-3” (or “Five Bet”).

    Bin.get(name) -> Outcome

    """

    pass


class Outcome(object):
    """Name for bet, contains payout odds and calculates
    payout amount.
    """

    outcomes = ('straight', 'split', 'street', 'corner', 'line', 'dozen',
                'column', 'high', 'low', 'even', 'odd', 'red', 'black',
                'basket')

    def __init__(self, name, odds):
        self.name = name
        self.odds = odds

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __hash__(self):
        return hash(f"{self.name}{self.odds}")

    def __str__(self):
        return "{name:s} ({odds:d}:1)".format_map(vars(self))

    def __repr__(self):
        return (f"{self.__class__.__name__:s}(name={self.name!r}, "
                f"odds={self.odds!r})")

    def win_amount(self, n):
        return self.odds * n


class Wheel(object):
    """Wheel contains the 38 individual bins on a wheel, plus
    a random number generator. It can select a Bin at random,
    simulating a spin of the wheel.

    A frozenset -- in the long run -- does make sense. After the wheel's
    insanely complex collections are built, they don't change. However,
    it adds a complication to have collection which are cloned and
    frozen.

    Wheel.bins
        Contains the individual Bin instances as a 38 element tuple.

     Wheel.rng
        A random number generator to select a Bin from the bins collection.

    Wheel.get(n) -> Bin
        Return Bin instance at index n.

    """

    def __init__(self, random_seed=None, wheel_size=38):
        self.bins = tuple(Bin() for _ in range(wheel_size))
        self.rng = Random()
        self.number = None
        self.all_outcomes = set()
        if random_seed:
            self.rng.seed(random_seed)
        else:
            self.rng.seed(urandom(16))

    def get(self, n: int) -> Bin:
        """Return set of Outcomes in Bin n
        """
        return self.bins[n]

    def get_outcome(self, name):
        for oc in self.all_outcomes:
            if name.lower() == oc.name.lower():
                return oc
        raise ValueError(f"{name} outcome NOT FOUND")

    def add_outcome(self, n, outcome):
        """Add outcome to Bin at index n.

        Bin is a frozenset, so we need to re-create the Bin for the
        number on the wheel, n, with a union of existing Outcomes
        (if any) and outcome.
        """

        self.all_outcomes |= set([outcome])
        self.bins = tuple(b if i != n else self.bins[n] | Bin([outcome])
                          for i, b in enumerate(self.bins))

    def choose(self):
        """Generates a random number between 0 and 37, caches the
        number and returns the randomly selected Bin instance.
        """

        self.number = self.rng.randrange(38)
        return self.bins[self.number]


class Odds(object):
    def __init__(self):
        self._straight = 35
        self._split = 17
        self._street = 11
        self._corner = 8
        self._basket = 6
        self._line = 5
        self._dozen = 2
        self._column = 2
        self._odd = 1
        self._even = 1
        self._red = 1
        self._black = 1
        self._high = 1
        self._low = 1

    @property
    def straight(self):
        return self._straight

    @property
    def split(self):
        return self._split

    @property
    def street(self):
        return self._street

    @property
    def corner(self):
        return self._corner

    @property
    def basket(self):
        return self._basket

    @property
    def line(self):
        return self._line

    @property
    def dozen(self):
        return self._dozen

    @property
    def column(self):
        return self._column

    @property
    def odd(self):
        return self._odd

    @property
    def even(self):
        return self._even

    @property
    def red(self):
        return self._red

    @property
    def black(self):
        return self._black

    @property
    def high(self):
        return self._high

    @property
    def low(self):
        return self._low


class BinBuilder(object):
    """Binbuilder"""

    def __init__(self):
        self.odds = Odds()

    def build_wheel(self, wheel):
        """Fill each bin in wheel with the collection of possible
        outcomes for each number.
        """
        for oc_name in Outcome.outcomes:
            outcomes = self.__getattribute__(oc_name)
            logger.debug(f"Building Wheel for {outcomes.__name__}")
            for bin_number, outcome in outcomes():
                wheel.add_outcome(bin_number, outcome)

    def straight(self) -> None:
        """For all numbers n such that 0 <= n < 37,
        double-zero at index 37 makes for 38 outcomes.
        """
        for bin_number in range(38):
            oc_name = "Straight {}".format(bin_number) if bin_number < 37 \
                                                       else "Straight 00"
            oc = Outcome(oc_name, self.odds.straight)
            yield (bin_number, oc)

    def split(self) -> None:
        for column in range(1, 35, 3), range(2, 36, 3):
            for number in column:
                oc_name = "{} {}-{}".format("Split", number, number + 1)
                outcome = Outcome(oc_name, self.odds.split)
                for offset in range(2):
                    yield (number + offset, outcome)
        for number in range(1, 34):
            oc_name = "{} {}-{}".format("Split", number, number + 3)
            outcome = Outcome(oc_name, self.odds.split)
            for offset in (0, 3):
                yield (number + offset, outcome)

        oc_name = "{} {}-{}".format("Split", "0", "00")
        outcome = Outcome(oc_name, self.odds.split)
        for number in (0, 37):
            yield (number, outcome)

    def street(self):
        for row in range(1, 35, 3):
            oc_name = "{} {}-{}-{}".format("Street", row, row+1, row+2)
            oc = Outcome(oc_name, self.odds.street)
            for i in 0, 1, 2:
                bin_number = row + i
                yield (bin_number, oc)

    def corner(self):
        for col in range(1, 32, 3), range(2, 33, 3):
            for number in col:
                oc_name = "{} {}-{}-{}-{}".format("Corner", number, number + 1,
                                                  number + 3, number + 4)
                outcome = Outcome(oc_name, self.odds.corner)
                for offset in [0, 1, 3, 4]:
                    yield (number + offset, outcome)

    def line(self):
        for num in range(1, 34, 3):
            oc_name = ["Line", num, num + 1, num + 2,
                       num + 3, num + 4, num + 5]
            oc = Outcome("{} {}-{}-{}-{}-{}-{}".format(*oc_name),
                         self.odds.line)
            for offset in range(6):
                yield num + offset, oc

    def dozen(self):
        for d in range(3):
            oc_name = "Dozen {}".format(d + 1)
            outcome = Outcome(oc_name, self.odds.dozen)
            for n in range(12):
                bin_number = 12 * d + n + 1
                yield bin_number, outcome

    def column(self):
        for column in (1, 2, 3):
            name = "Column {}".format(column)
            oc = Outcome(name, self.odds.column)
            for number in range(column, column + 34, 3):
                yield number, oc

    def high(self):
        name = "High"
        oc = Outcome(name, self.odds.high)
        for number in range(19, 37):
            yield number, oc

    def low(self):
        name = "Low"
        oc = Outcome(name, self.odds.low)
        for number in range(1, 19):
            yield number, oc

    def even(self):
        oc = Outcome("Even", self.odds.even)
        for number in range(1, 37):
            if number % 2 == 0:
                yield number, oc

    def odd(self):
        oc = Outcome("Odd", self.odds.odd)
        for number in range(1, 37):
            if number % 2 == 1:
                yield number, oc

    def red(self):
        red = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19,
               21, 23, 25, 27, 30, 32, 34, 36)
        outcome = Outcome("Red", self.odds.red)
        for number in red:
            yield number, outcome

    def black(self):
        black = (2, 4, 6, 8, 10, 11, 13, 15, 17, 20,
                 22, 24, 26, 28, 29, 31, 33, 35)
        outcome = Outcome("Black", self.odds.black)
        for number in black:
            yield number, outcome

    def basket(self):
        basket = (0, 1, 2, 3, 37)
        outcome = Outcome("Basket", self.odds.basket)
        for number in basket:
            yield number, outcome


class Bet:
    """Bet associates an amount with an Outcome. In a future round of
    design, we can also associate a Bet with a Player.
    """

    def __init__(self, amount: int, outcome: Outcome, player=None) -> None:
        self.amount = amount
        self.outcome = outcome
        self.player = player

    def __str__(self):
        return f"{self.amount} on {self.outcome}"

    def __repr__(self):
        return (f"{self.__class__.__name__}(amount={self.amount}, "
                f"outcome={self.outcome!r})")

    def win_amount(self) -> int:
        return self.amount + self.outcome.win_amount(self.amount)

    def lose_amount(self) -> int:
        return self.amount


if __name__ == "__main__":
    wheel = Wheel(1)
    BinBuilder().build_wheel(wheel)
