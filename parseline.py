def parseline(line, idx_a='8=FIX', idx_b='\x01'):
    """list of n tokens [t0, t1, ... t(n-1)]"""

    t = line[line.find(idx_l) : line.rfind(idx_r)]
    if t:
        return t
