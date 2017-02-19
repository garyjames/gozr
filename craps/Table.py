# coding: utf-8

from collections import defaultdict

class Table(object):
    """Table - craps table"""


    def __init__(self):
        self.input = input
        self.dice = None
        self.point = False
        self.account = 0
        self.game_on = False
        self.wagers = defaultdict(list)

    def __call__(self):
        self.dice = self.input()

    def payout(self):
        if not self.point:
            if sum(self.dice) == 7:
                #this should be a logger thing
                print 'winner!'
        else:
            pass

    def callwagers(self):
            for k in self.wagers:
                self.wagers[k]()

if __name__ == '__main__':
    table = Table()
    table.wagers['player1'].append(int)
    table.game_on = True
    while table.game_on == True:
        table()
        table.payout()
        table.callwagers()
        r = raw_input('continue? [Y]n')
        if r == '\n':
            table.game_on = raw_input('continue? [Y]n')
        elif r == False:
            table.game_on = False
            
        
