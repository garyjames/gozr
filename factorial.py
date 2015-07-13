# coding: utf-8
def factorial(n):
#    if n <= 1:
#        yield 1
#    else:
#        for i in factorial(n-1):
#            yield n * i
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
