from collections import defaultdict
from sys import exit
from observer import Observable, Observer


class Player(Observable):
    def __init__(self, name=None, account=0):
        Observable.__init__(self)
        self._account = account
        self.name = name
        self.wager = None
        self.history = []

    def __repr__(self):
        return '{0.name}'.format(self)

    def transaction(f):
        def rec(self, *args, **kw):
            self.history.append((f.func_name, f(self, *args, **kw)))
        return rec

    @property
    def balance(self):
        return self._account

    @transaction
    def rename(self, s):
        self.name = s
        return s

    @transaction
    def deposit(self, n):
        self._account += n
        return n

    @transaction
    def withdraw(self, n):
        self._account -= n
        return -n

    @transaction
    def roll_dice(self):
        tbl = self._Observable__observers[0]
        tbl.notify(self, throw='dice')

    @transaction
    def bet(self, bet=None):
        tbl = self._Observable__observers[0]
        tbl.notify(self, bet)


class Table(Observer):
    def __init__(self, obsrvbl):
        Observer.__init__(self, obsrvbl)
        self.numbers = (
            'zero','one','two','three','four',
            'five','six','seven','eight',
            'nine','ten', 'eleven','twelve')
        self.wagernames = self.numbers + (
            'place','come','dontcome','horn','odds','hi-lo',
            'craps','passline','any7', 'whirl','hop','lay',)
        self.board = dict(zip(xrange(len(self.wagernames)), self.wagernames))
        self.wagers = defaultdict(list)

    def notify(self, obsrvbl, *args, **kwargs):
        for k in kwargs:
            if k == 'throw':
                self.(obsrvbl, input('enter: '))
            elif k == 'bet':
                btype, amount = kwargs[k]
                self.wagers[obsrvbl].append(kwargs[k])


class Dice(Observable):
    def __init__(self):
        Observable.__init__(self)
        self.values = None

    def __call__(self):
        self.values = input()
        return self.value

    @property
    def total(self):
        return sum(self.value)

if __name__ == '__main__':
    player1 = Player(name='Bond, James', account=1000)
    bones = Dice()
    tbl = Table(player1)
    bones.register_observer(tbl)
    player1.notify_observers('somethinggoeshere')

