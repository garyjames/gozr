def parseline(line, idx_a='8=FIX', idx_b='\x01', SOH='\x01'):
    """list of fix pairs.

    <FixTag>=<FixValue>, ..."""

    fixmsg = line[line.find(idx_l) : line.rfind(idx_r)]
    if fixmsg:
        return fixmsg.split(SOH)
