# base 32 encode

map32 = ( 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L',
    'M', 'N', 'P', 'Q', 'R', 'T', 'U', 'W', 'X', 'Y', 'Z'
)

map32 = dict(enumerate(map32))

def encode32(n, b32=str(), exp=0):
    if n < 32:
        return map32[n] + b32
    else:
        return intTo32(n/32, b32=map32[n%32]+b32, exp=exp+1)

def decode32(s):
    result = 0
    exp = len(s)
    pass

if __name__ == '__main__':
    from sys import argv
    n = int(argv[1])
    print encode32(n)
