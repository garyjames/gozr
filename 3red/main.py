"""CME Security Definition File tool
"""


import gzip
import cme_exchange
from collections import Counter
from fileparser import regex
from queries import count_by_type
from queries import count_by_underlying
from queries import get_symbol


class Secdef(object):

    """Run-time interface for the secdef tool. The default arguments in
    each method will answer each question from the assesment.


    Usage:

      secdef = Secdef()
      secdef.get_secdef_file() (will overwrite existing file)
      secdef.load_instruments()

      1) futures = secdef.get_count_by_type()
      2) futures_grouped_by_underlying = secdef.get_count_by_underlying()
      3) symbols = secdef.get_symbol()


    You can run methods with different TYPE values:

      oof = secdef.get_count_by_type(security_type='oof')
      all_grouped = secdef.get_count_by_underlying(security_type='all')
      symbols_10 = secdef.get_symbol(front_expiry_count=10)


    The default location of the secdef file is the current working
    directory. To use another *.gz file:

      secdef.secdef_sourcefile = '/my/other/secdef.dat.gz'
      secdef.load_instruments()


    Use the pprint to display for groups:

      secdef.pprint(futures_grouped_by_underlying)

    """

    def __init__(self):
        self._count_by_type = count_by_type
        self._count_by_underlying = count_by_underlying
        self._get_symbol = get_symbol
        self.secdef_sourcefile = 'secdef.dat.gz'
        self.instruments = None

    @staticmethod
    def get_secdef_file():
        cme_exchange.get_file()

    def load_instruments(self):
        self.instruments = []
        with gzip.open(self.secdef_sourcefile, 'rt') as FH:
            for line in FH:
                self.instruments.append(regex(line))

    def get_count_by_type(self, security_type='fut'):
        return self._count_by_type(self.instruments, type_=security_type)

    def get_count_by_underlying(self, security_type='fut'):
        return self._count_by_underlying(self.instruments, type_=security_type)

    def get_symbol(self, security_type='fut', front_expiry_count=4, asset='ge',
                   leg_no=0):
        return self._get_symbol(self.instruments, type_=security_type,
                               front_expiry_count=front_expiry_count,
                               asset=asset, leg_no=leg_no) 

    @staticmethod
    def pprint(d):
        product_complexes = {
            '': 'Undefined',
            '2': 'Commodity/Agriculture',
            '4': 'Currency',
            '5': 'Equity',
            '12': 'Other',
            '14': 'Interest Rate',
            '15': 'FX Cash',
            '16': 'Energy',
            '17': 'Metals'
        }
        if isinstance(d, Counter):
            for k in d:
                print('{:<22} {:>8}'.format(product_complexes[k], d[k]))
        else:
            for t in d:
                print(t)
                for k in d[t]:
                    print('\t{:<22}{:>8}'.format(product_complexes[k],
                                                 d[t][k]))
                print()


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--get-secdef-file', action='store_true',
                        help='Downloads secdef.dat.gz into current directory')
    parser.add_argument('--count-by-type', type=str, nargs='?', const='all',
                        help='Get instruments by type')
    parser.add_argument('--count-by-underlying', type=str, nargs='?',
                        const='all', help='Get instruments by underlying')
    args = parser.parse_args()

    if args.get_secdef_file:
        cme_exchange.get_file()

    instruments = []
    with gzip.open(args.secdef_sourcefile, 'rt') as FH:
        for line in FH:
            instruments.append(regex(line))

    if args.count_by_type:
        ret = count_by_type(instruments, type_=args.count_by_type)
        print(ret)
    if args.count_by_underlying:
        ret = count_by_underlying(instruments, type_=args.count_by_underlying)
        print(ret)
