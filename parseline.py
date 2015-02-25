def parseline(line, idx_l='8=FIX', idx_r='\x01', SOH='\x01'):
    rec = line[line.find(idx_l) : line.rfind(idx_r)]
    if rec:
        return tuple(rec.split(SOH))