from src.roulette import Wheel, BinBuilder, Odds, Bet
import pytest


@pytest.fixture
def wheel():
    w = Wheel()
    builder = BinBuilder()
    builder.build_wheel(w)
    return w


@pytest.fixture
def odds():
    return Odds()


def test_bet_0(wheel, odds):
    bet = Bet(25, wheel.get_outcome('Straight 16'))
    assert bet.outcome.name == 'Straight 16'
    assert bet.outcome.odds == odds.straight
