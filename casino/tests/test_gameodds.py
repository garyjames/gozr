from src.roulette import Odds


def test_odds():
    odds = Odds()
    assert odds.straight == 35
    assert odds.split == 17
    assert odds.street == 11
    assert odds.corner == 8
    assert odds.basket == 6
    assert odds.line == 5
    assert odds.dozen == 2
    assert odds.column == 2
    assert odds.odd == 1
    assert odds.even == 1
    assert odds.red == 1
    assert odds.black == 1
    assert odds.high == 1
    assert odds.low == 1
