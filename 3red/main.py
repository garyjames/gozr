"""CME Security Definition File tools.
"""


import gzip

from collections import Counter

import cme_exchange
from fileparser import lineparser


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('--get-secdef-file', action='store_true',
                        help='Downloads secdef.dat.gz into current directory.')
    parser.add_argument('--secdef-sourcefile', default='secdef.dat.gz',
                        help='filename')
    parser.add_argument('--inspect', action='store_true',
                        help='Run through the raw file line-by-line')
    parser.add_argument('--count-security-types', action='store_true',
                        help='Count the number of unique types.')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--symbols-as-key', action='store_true',
                       help='Index by Symbol, Tag 55')
    group.add_argument('--iid-as-key', action='store_true',
                       help='Index by SecurityID, Tag 48')
    group.add_argument('--use-regex', action='store_true',
                       help='Use regex')

    args = parser.parse_args()

    if args.get_secdef_file:
        cme_exchange.get_file()

    product_complexes = {
        2: 'Commodity/Agriculture',
        4: 'Currency',
        5: 'Equity',
        12: 'Other',
        14: 'Interest Rate',
        15: 'FX Cash',
        16: 'Energy',
        17: 'Metals',
    }

    product_complexes_by_name = dict(zip(
                                     [v for v in product_complexes.values()],
                                     [k for k in product_complexes]))

    output_template = (
        'Asset/Product Family: {:<10} '
        'Asset/Product: {:<10} '
        'SecType: {:<10} '
        'ID: {:<10} '
        'Sym: {:<20} '
    )

    if args.inspect:
        with gzip.open(args.secdef_sourcefile, 'rt') as FH:
            for line in FH:
                input('> ')
                print(line.replace('\x01', '    '))
                if args.verbose >= 1:
                    print(lineparser(line))
