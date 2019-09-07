from random import Random
from os import urandom
from roulette.bin import Bin


class Wheel(object):
    """Wheel contains the 38 individual bins on a Odds wheel, plus
    a random number generator. It can select a Bin at random,
    simulating a spin of the Odds wheel.

    The Wheel is a collection and each Bin is also a collection.
    Both need `__next__()` methods.

    A frozenset -- in the long run -- does make sense. After the wheel's
    insanely complex collections are built, they don't change. However,
    it adds a complication to have collection which are cloned and
    frozen.

    Wheel.get(bin_number) -> Bin

    """

    def __init__(self):
        self.bins = tuple(set() for _ in range(38))
        self.rng = Random()
        self.rng.seed(urandom(16))

    def __next__(self):
        return self.rng.randint(0, 37)

    def get(self, n):
        return self.bins[n]
