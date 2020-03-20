import pytest
from src.roulette import Wheel, Bin, Outcome, BinBuilder


@pytest.fixture
def wheel():
    """seed(1) returns 8, 36, 4, 16, 7, 31, 28, 30, 24, 13, ..."""

    w = Wheel(random_seed=1)
    w.known_seq = [8, 36, 4, 16, 7, 31, 28, 30, 24, 13]
    return w


def test_init_number_is_None(wheel):
    assert wheel.number is None


def test_choose(wheel):
    s = [Bin() for _ in range(10)]
    assert s == [wheel.choose() for _ in range(10)]


def test_get_empty_bins(wheel):
    assert wheel.get(0) == Bin()
    assert wheel.get(37) == Bin()


def test_bin_length(wheel):
    assert len(wheel.bins) == 38
    with pytest.raises(IndexError):
        wheel.get(38)
        wheel.get(39)


def test_sequence_II(wheel):
    seq = [(wheel.choose(), wheel.number) for _ in range(10)]
    assert seq == [(Bin(), 8), (Bin(), 36), (Bin(), 4), (Bin(), 16),
                   (Bin(), 7), (Bin(), 31), (Bin(), 28), (Bin(), 30),
                   (Bin(), 24), (Bin(), 13)]

    seq = list(list(zip(*seq))[1])
    assert seq == wheel.known_seq


def test_sequence_III(wheel):
    a = [o.number for _ in range(10) for o in [wheel] for _ in [wheel.choose()]
         ]
    assert a == wheel.known_seq


def test_sequence_IV(wheel):
    for i in range(10):
        wheel.add_outcome(i, Outcome("test", i))
        assert Outcome("test", i) in wheel.get(i)


def test_add_outcome(wheel):
    for i in wheel.known_seq[:4]:
        wheel.add_outcome(i, Outcome("test", i))
        assert Outcome("test", i) in wheel.choose()
    assert Outcome("test", 16) in wheel.bins[i]


def test_get_outcome(wheel):
    binbuilder = BinBuilder()
    binbuilder.build_wheel(wheel)
    assert Outcome('Straight 16', 35) == wheel.get_outcome('Straight 16')
    with pytest.raises(ValueError):
        wheel.get_outcome('Straight')
        wheel.get_outcome('Foo')
