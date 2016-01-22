import logging
from sys import argv 
from os import path 

if 'Windows' in os.uname():
    logdir = os.path.join('C:\\', 'logs')
else:
    logdir = os.path.join('/logs')

def wraplogging(f):
    logging.basicConfig(
        filename = path.join(logdir, f.__name__),
        datefmt = "%Y-%m-%d %H:%M:%S",
        format = "%(levelname)-10s %(asctime)s %(module)s %(message)s",
    )
    log = logging.getLogger(path.basename(f.__name__))
    log.setLevel(logging.INFO)

    def f1(*args, **kwargs):
        log.info('starting {} {}'.format(args, kwargs))
        ret = f(*args, **kwargs)
        log.info('{} returned {}'.format(f.__name__, ret))
        return ret

    return f1

def parseline(line, idx_l='8=FIX', idx_r='\x01', SOH='\x01'):
    return line[line.find(idx_l) : line.rfind(idx_r) + 1]

@wraplogging
def parsefile(filename):
    with open(filename) as fh:
        for line in fh:
            ret = parseline(line)
            if ret:
                print ret

if __name__ == '__main__':
    filename = argv[1]
    parsefile(filename)
