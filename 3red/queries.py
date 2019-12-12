# coding: utf-8

from collections import Counter


def get_by_type(instruments, type_=None):
    """Returns Counter instance for all instruments equal to SecurityType(167).

    Ex: get_by_type(instrument_type='mleg')
    """

    if type_:
        print('Looking for', type_)
        return Counter((i for i in instruments if type_ in i[2]))
    else:
        print(__doc__)
        return None

def get_something(*args, **kwargs):
    pass
