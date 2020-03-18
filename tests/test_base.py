from src.roulette import Outcome, Wheel, BinBuilder, Odds
import pytest


@pytest.fixture
def wheel():
    w = Wheel(1)
    builder = BinBuilder()
    builder.build_wheel(w)
    w.known_seq = [8, 36, 4, 16, 7, 31, 28, 30, 24, 13]
    return w


@pytest.fixture
def odds():
    return Odds()


def test_straight(wheel, odds):
    for i in range(37):
        assert Outcome("Straight {}".format(i), odds.straight) in wheel.get(i)
    assert Outcome("Straight 00", odds.straight) in wheel.get(37)


def test_split(wheel, odds):
    assert Outcome("Split 0-00", odds.split) in wheel.get(0)
    assert Outcome("Split 1-2", odds.split) in wheel.get(1)
    assert Outcome("Split 1-4", odds.split) in wheel.get(1)
    assert Outcome("Split 33-36", odds.split) in wheel.get(36)
    assert Outcome("Split 35-36", odds.split) in wheel.get(36)
    assert Outcome("Split 0-00", odds.split) in wheel.get(37)


def test_street(wheel, odds):
    assert Outcome("Street 1-2-3", odds.street) in wheel.get(1)
    assert Outcome("Street 1-2-3", odds.street) in wheel.get(2)
    assert Outcome("Street 34-35-36", odds.street) in wheel.get(35)
    assert Outcome("Street 34-35-36", odds.street) in wheel.get(36)


def test_corner(wheel, odds):
    """Test corner bets around 1, 4, and 5"""

    assert Outcome("Corner 1-2-4-5", odds.corner) in wheel.get(1)
    assert Outcome("Corner 1-2-4-5", odds.corner) in wheel.get(4)
    assert Outcome("Corner 4-5-7-8", odds.corner) in wheel.get(4)
    assert Outcome("Corner 1-2-4-5", odds.corner) in wheel.get(5)
    assert Outcome("Corner 2-3-5-6", odds.corner) in wheel.get(5)
    assert Outcome("Corner 4-5-7-8", odds.corner) in wheel.get(5)
    assert Outcome("Corner 5-6-8-9", odds.corner) in wheel.get(5)


def test_line(wheel, odds):
    """Test line bets to be sure that 1 is only in a single line bet,
    where 4 is part of two separate line bets.
    """

    assert Outcome("Line 1-2-3-4-5-6", odds.line) in wheel.get(1)
    assert Outcome("Line 1-2-3-4-5-6", odds.line) in wheel.get(4)
    assert Outcome("Line 4-5-6-7-8-9", odds.line) in wheel.get(4)
    assert Outcome("Line 31-32-33-34-35-36", odds.line) in wheel.get(33)
    assert Outcome("Line 31-32-33-34-35-36", odds.line) in wheel.get(36)


def test_dozen(wheel, odds):
    assert Outcome("Dozen 1", odds.dozen) in wheel.get(1)
    assert Outcome("Dozen 2", odds.dozen) in wheel.get(17)
    assert Outcome("Dozen 3", odds.dozen) in wheel.get(33)
    assert Outcome("Dozen 3", odds.dozen) in wheel.get(36)


def test_column(wheel, odds):
    assert Outcome("Column 1", odds.dozen) in wheel.get(1)
    assert Outcome("Column 2", odds.dozen) in wheel.get(17)
    assert Outcome("Column 3", odds.dozen) in wheel.get(33)
    assert Outcome("Column 3", odds.dozen) in wheel.get(36)


def test_high(wheel, odds):
    assert Outcome("High", odds.high) in wheel.get(19)
    assert Outcome("High", odds.high) in wheel.get(36)


def test_low(wheel, odds):
    assert Outcome("Low", odds.low) in wheel.get(1)
    assert Outcome("Low", odds.low) in wheel.get(17)
    assert Outcome("Low", odds.low) in wheel.get(18)


def test_red(wheel, odds):
    assert Outcome("Red", odds.red) in wheel.get(1)
    assert Outcome("Red", odds.red) in wheel.get(3)
    assert Outcome("Red", odds.red) in wheel.get(36)


def test_black(wheel, odds):
    Outcome("Black", odds.black) in wheel.get(2)
    Outcome("Black", odds.black) in wheel.get(10)
    Outcome("Black", odds.black) in wheel.get(35)


def test_even(wheel, odds):
    assert Outcome("Even", odds.even) in wheel.get(2)
    assert Outcome("Even", odds.even) in wheel.get(18)
    assert Outcome("Even", odds.even) in wheel.get(36)


def test_odd(wheel, odds):
    assert Outcome("Odd", odds.odd) in wheel.get(1)
    assert Outcome("Odd", odds.odd) in wheel.get(17)
    assert Outcome("Odd", odds.odd) in wheel.get(35)


def test_basket(wheel, odds):
    assert Outcome("Basket", odds.basket) in wheel.get(0)
    assert Outcome("Basket", odds.basket) in wheel.get(1)
    assert Outcome("Basket", odds.basket) in wheel.get(37)
