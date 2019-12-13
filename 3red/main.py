"""CME Security Definition File tools.
"""


import gzip

import cme_exchange

from fileparser import regex
from queries import count_by_type
from queries import count_by_underlying
from queries import get_symbol


class Secdef(object):
    def __init__(self, secdef_sourcefile='secdef.dat.gz'):
        self.count_by_type = count_by_type
        self.count_by_underlying = count_by_underlying
        self.get_symbol = get_symbol
        self.secdef_sourcefile = secdef_sourcefile
        self.instruments = []

    @staticmethod
    def get_secdef_file():
        cme_exchange.get_file()

    def load_instruments(self):
        with gzip.open(self.secdef_sourcefile, 'rt') as FH:
            for line in FH:
                self.instruments.append(regex(line))

    def get_count_by_type(self, security_type='fut'):
        return self.count_by_type(self.instruments,
                                  type_=security_type)

    def get_count_by_underlying(self, security_type='all'):
        return self.count_by_underlying(self.instruments,
                                        type_=security_type)

    def get_symbol(self, security_type='fut', front_expiry_count=4, asset='ge',
                   leg_no=None):
        return self.get_symbol(self.instruments,
                               type_=security_type,
                               front_expiry_count=4,
                               asset='ge',
                               leg_no=0) 
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
            '17': 'Metals',
        }
        for k in d:
            print(product_complexes[k], d[k])


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
