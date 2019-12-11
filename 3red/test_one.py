# coding: utf-8

import gzip
from fileparser import lineparser

def test_one(line):
    with gzip.open('secdef.dat.gz', 'rt') as FH:
        for line in FH:
            ret = lineparser(line)

if __name__ == '__main__':
    import timeit
    t = timeit.Timer("open('secdef.dat.gz', 'rt') as FH:\n    for line in FH:\n        lineparser(line)")
    t.timeit()
