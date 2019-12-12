"""CME Security Definition File tools.
"""


import gzip

import cme_exchange

from fileparser import regex
from fileparser import foobar

from queries import get_by_type


menu = """Select item and press <ENTER>:
 1. Foo
 2. Bar
 3. Baz
 4. Moe
 5. Larry
 6. Curly
 7. Shemp

> """

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('--get-secdef-file', action='store_true',
                        help='Downloads secdef.dat.gz into current directory.')
    parser.add_argument('--display-by-type', type=str, nargs='?', const='all',
                        help='Display instruments by type')

    parser.add_argument('--secdef-sourcefile', default='secdef.dat.gz',
                        help='filename')
    parser.add_argument('--regex', action='store_true',
                        help='Use fileparser.regex')
    parser.add_argument('--foobar', action='store_true',
                        help='Use fileparser.foobar')
    parser.add_argument('--count-security-types', action='store_true',
                        help='Count the number of unique types.')
    parser.add_argument('--menu-driven', action='store_true',
                        help='Use numbered menu interface')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--symbols-as-key', action='store_true',
                       help='Index by Symbol, Tag 55')
    group.add_argument('--iid-as-key', action='store_true',
                       help='Index by SecurityID, Tag 48')
    group.add_argument('--use-regex', action='store_true',
                       help='Use regex')

    args = parser.parse_args()

    product_complexes = {
        '2': 'Commodity/Agriculture',
        '4': 'Currency',
        '5': 'Equity',
        '12': 'Other',
        '14': 'Interest Rate',
        '15': 'FX Cash',
        '16': 'Energy',
        '17': 'Metals',
        '': 'Undefined'
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

    if args.get_secdef_file:
        cme_exchange.get_file()

    instruments = []

    with gzip.open(args.secdef_sourcefile, 'rt') as FH:
        for line in FH:
            instruments.append(regex(line))

    if args.display_by_type:
        print('Display by type == dbt', args.display_by_type)
        pass

    if args.foobar:
        print(foobar(line))

    if args.menu_driven:
        while True:
            ret = int(input(menu))
            if ret == 1:
                print('You pressed 1')
            if ret == 2:
                print('You pressed 2')
            if ret == 3:
                print('You pressed 3')
