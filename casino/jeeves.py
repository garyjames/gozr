# coding: utf-8
from src.roulette import BinBuilder, Wheel, Bet, Outcome

builder = BinBuilder()
wheel = Wheel(random_seed=1)
builder.build_wheel(wheel)

for bin_num in range(38):
    print(f"Bin [{bin_num}]")
    for oc in wheel.get(bin_num):
        print(f"    {oc}")
    print()

str16 = Outcome('Straight 16', 35)
bet = Bet(25, wheel.get_outcome('Straight 16'))
print(bet)
