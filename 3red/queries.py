# coding: utf-8

from collections import Counter


def get_by_type(instruments, type_=None):
    """Returns counter instance for all instruments equal to SecurityType(167).

    Ex: get_all_instruments(instrument_type='MLEG')
    """

    if None is instrument_type:
        print(__doc__)
        return None

    return Counter((i for i in instruments if instrument_type in i[2]))

def get_something(*args, **kwargs):
    pass
