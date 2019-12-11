"""Instruments.py"""


class Instruments(object):
    """Instruments class"""

    def __init__(self):
        self.d = dict()

    def add(self, iid, line):
        self.d[iid] = line

    def get(self, iid):
        return self.d[iid]
