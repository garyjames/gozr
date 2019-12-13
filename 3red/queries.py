# coding: utf-8

from collections import Counter


def count_by_type(instruments, type_=None):
    """SecurityID(48) grouped by SecurityType(167)

    Returns counter with tally of TYPE found in SecurityType(167).
    If TYPE is 'all', returns count of every instrument grouped by TYPE.

    Example:    count_by_type(instrument_type='mleg') -> {'MLEG': n}
    """

    type_ = type_.upper()
    if type_:
        if 'ALL' in type_:
            return Counter((i[2] for i in instruments))
        else:
            return Counter((i[2] for i in instruments if type_ in i[2]))
    else:
        print(__doc__)
        return None


def count_by_underlying(instruments, type_=None):
    """SecurityID(48) grouped by UnderlyingProduct(462) (i.e. Product Complex)

    Returns counter with tally grouped by UnderlyingProduct(462).
    If TYPE is 'all', returns dict of SecurityType(167).

    Example:

      count_by_underlying(type_='all') -> { 'FUT': { 'Energy': n, ... },
                                            'OOF': { 'Energy': n, ... }, ... }
    """

    type_ = type_.upper()
    if type_:
        if 'ALL' in type_:
            ret = {}
            for t in set((i[2] for i in instruments)):
                ret[t] = Counter((i[4] for i in instruments if t in i[2]))
            return ret
        else:
            return Counter((i[4] for i in instruments if type_ in i[2]))

    else:
        print(__doc__)
        return None


def get_symbol(instruments, type_='fut',
               front_expiry_count=4, asset='ge', leg_no=None):
    """Returns list of tuples matching arguments"""

    if leg_no in [None, 0]:
        leg_no = ''

    type_ = type_.upper()
    asset = asset.upper()
    ret = [(i[1], int(i[3])) for i in instruments
            if type_ in i[2] and
            asset == i[7] and
            leg_no == i[5]]

    ret.sort(key=lambda tup: tup[1])

    if front_expiry_count:
        return ret[:4]
    else:
        return ret
