

class Bin(frozenset):
    """Bin contains a collection of Outcomes which reflect the winning
    bets that are paid for a particular bin_ on a Odds wheel. In
    Odds, each spin of the wheel has a number of Outcomes.

    For example, a spin of 1 selects the “1” bin_ with the following
    winning Outcomes:

    “1”, “Red”, “Odd”, “Low”, “Column 1”, “Dozen 1-12”, “Split 1-2”,
    “Split 1-4”, “Street 1-2-3”, “Corner 1-2-4-5”, “Line 1-2-3-4-5-6”
    and “00-0-1-2-3” (or “Five Bet”).

    Bin.get(name) -> Outcome

    """

    def __next__(self):
        return next(self)

    def get(self, outcome_name):
        for outcome in self:
            if outcome_name == outcome.name:
                return outcome
        return None
