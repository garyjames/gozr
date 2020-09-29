from src.roulette import Wheel, BinBuilder, Odds, Bet, Table
import pytest


@pytest.fixture
def table():
    w = Wheel()
    builder = BinBuilder()
    builder.build_wheel(w)
    t = Table(w)
    return t


def test_table_0(table):
    bet = Bet(25, table.wheel.get_outcome('Straight 16'))
    table.accept_bet(bet)


def test_iter(table):
    bet = Bet(25, table.wheel.get_outcome('Straight 16'))
    table.accept_bet(bet)
    bet = Bet(5, table.wheel.get_outcome('Straight 1'))
    table.accept_bet(bet)
    bet = Bet(10, table.wheel.get_outcome('Straight 6'))
    table.accept_bet(bet)
    bet = Bet(20, table.wheel.get_outcome('Straight 11'))
    table.accept_bet(bet)
    bet = Bet(30, table.wheel.get_outcome('Straight 10'))
    table.accept_bet(bet)
    bet = Bet(35, table.wheel.get_outcome('Straight 18'))
    table.accept_bet(bet)
    bet = Bet(40, table.wheel.get_outcome('Straight 3'))
    table.accept_bet(bet)
    bet = Bet(45, table.wheel.get_outcome('Straight 33'))
    table.accept_bet(bet)
    bet = Bet(40, table.wheel.get_outcome('Straight 8'))
    table.accept_bet(bet)
    bet = Bet(55, table.wheel.get_outcome('Straight 9'))
    table.accept_bet(bet)

    assert 10 == len([x for x in table.bets])

    for i in table:
        assert isinstance(i, Bet)
        assert getattr(i, 'amount', None) != None
        assert getattr(i, 'outcome', None) != None
        assert getattr(i, 'scome') == None
        assert isinstance(i.amount, int)
        assert isinstance(i.outcome, Outcome)
