# coding: utf-8
from src.roulette import BinBuilder, Wheel, Bet, Outcome, Table

builder = BinBuilder()
wheel = Wheel()
builder.build_wheel(wheel)

for bin_num in range(38):
    print(f"Bin [{bin_num}]")
    for oc in wheel.get(bin_num):
        print(f"    {oc}")
    print()

str16 = Outcome('Straight 16', 35)
bet = Bet(25, wheel.get_outcome('Straight 16'))
assert bet.outcome == str16
table = Table(wheel)
