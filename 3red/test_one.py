# coding: utf-8

import gzip
import timeit

from fileparser import regex
from fileparser import foobar

s = """\
with gzip.open('secdef.dat.gz', 'rt') as FH:
    for line in FH:
        ret = regex(line)
"""
ret = timeit.timeit(stmt=s, number=1, globals=globals())
print(ret)

s = """\
with gzip.open('secdef.dat.gz', 'rt') as FH:
    for line in FH:
        ret = foobar(line)
"""
ret = timeit.timeit(stmt=s, number=1, globals=globals())
print(ret)
