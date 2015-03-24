import os
import sys
from bs4 import BeautifulSoup as bs

def myfunc():

    for filename in os.listdir(os.curdir):
        if filename.endswith('.aml'):
            modified = False
            with open(filename) as fh:
                soup = bs(fh)
            print '{}'.format(filename)
            ret = soup.findAll(
                  lambda x: x.has_attr('file') and 'python' in x['file']
            )

            for i in ret:
                if not i.has_attr('foo'):
                    i['FOO'] = 'bar'
                    modified = True

            if modified:
                with open(filename + '.new', 'w') as fh:
                    fh.write(soup.prettify())

if __name__ == "__main__":
    myfunc()
