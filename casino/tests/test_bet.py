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


def test_bet_0(wheel):
    bet = Bet(25, wheel.get_outcome('Straight 16'))
    assert bet.outcome.name == 'Straight 16'
    assert bet.outcome.odds == 35
    assert bet.amount == 25


def test_bet_1(wheel):
    bet = Bet(25, wheel.get_outcome('Straight 11'))
    assert bet.win_amount() == 25 * 35 + 25
    assert bet.win_amount() == bet.amount * bet.outcome.odds + bet.amount
    assert bet.lose_amount() == 25


def test_bet_2(wheel):
    bet = Bet(25, wheel.get_outcome('Street 16-17-18'))
    assert bet.win_amount() == 25 * 11 + 25
    assert bet.win_amount() == bet.amount * bet.outcome.odds + bet.amount
    assert bet.lose_amount() == 25
