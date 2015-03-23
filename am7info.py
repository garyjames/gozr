import os
import sys
from bs4 import BeautifulSoup as bs

def myfunc():
    _d = {}
    for filename in os.listdir(os.curdir):
        if '.aml' in filename:
            with open(filename,'r') as fh:
                soup = bs(fh)
            print '{}'.format(fh.name)
            print soup.prettify()
            print
            ret = soup.findAll(lambda x: x.has_attr('OUTPUTFILE'))
            for i in ret:
                print ret
            print

if __name__ == "__main__":
    myfunc()
