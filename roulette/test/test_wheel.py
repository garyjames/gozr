from unittest import TestCase
from roulette.outcome import Outcome
from roulette.bin import Bin
from roulette.wheel import Wheel
from roulette.game import Odds


class TestWheel(TestCase):
    def setUp(self):
        self.wheel = Wheel()
        self.wheel.rng.seed(1)
        self.odds = Odds()

    def test_wheel_attrs(self):
        """Wheel should NOT have an add_outcome method."""
        self.assertFalse(getattr(self.wheel, 'add_outcome', False))
        self.assertTrue(self.wheel.__getattribute__('bins'))
        self.assertTrue(self.wheel.__getattribute__('rng'))
        self.assertTrue(self.wheel.__getattribute__('get'))
        self.assertTrue(self.wheel.__getattribute__('__next__'))

    def test_rng(self):
        self.assertEqual([self.wheel.rng.randint(0, 37) for _ in range(10)],
                         [8, 36, 4, 16, 7, 31, 28, 30, 24, 13])

    def test_next(self):
        # noinspection PyTypeChecker
        self.assertEqual([next(self.wheel) for _ in range(10)],
                         [8, 36, 4, 16, 7, 31, 28, 30, 24, 13])

    def test_add_bins(self):
        self.assertEqual(self.wheel.get(0), Bin())
        self.assertEqual(self.wheel.get(37), Bin())

    def test_add_bins_with_content_and_get_bin(self):
        self.wheel.bins = tuple(Bin([i]) for i in range(38))
        self.assertEqual(self.wheel.get(0), Bin([0]))
        self.assertEqual(self.wheel.get(25), Bin([25]))
        self.assertEqual(self.wheel.get(37), Bin([37]))

    def test_add_bins_with_outcomes_and_get_outcomes(self):
        straight0 = Outcome("Straight 0", self.odds.straight)
        straight00 = Outcome("Straight 00", self.odds.straight)
        basket = Outcome("Basket 0-00-1-2-3", self.odds.basket)
        split0_00 = Outcome("Split 0-00", self.odds.split)
        bin0 = Bin([straight0, basket, split0_00])
        bin00 = Bin([straight00, basket, split0_00])
        self.wheel.bins = tuple([bin0, bin00])
        self.assertEqual(self.wheel.bins, tuple([bin0, bin00]))
        self.assertEqual(self.wheel.get(0), bin0)
