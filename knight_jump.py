# knight_jump

def makeboard():
    """define a board and return generator"""
    for x in xrange(5):
        for y in xrange(4):
	    # omit bottom right and left squares on board
	    if (x == 0 and  y == 3) or (x == 4 and y == 3):
	        pass
	    else:
	        yield x,y


board = tuple(makeboard())


def knight_choices(coordinates):
    """Return all legal jumps from starting position (coordinates)"""

    ret = []

    # Identify 'first-leg' and 'second-leg' (move 2, then 1)
    for axis in [0,1]:
        opposite_axis = 0 if axis == 1 else 1

        # move a distance of 2-spaces along current axis in both directions
        for d in [-2,2]:
            first_leg = list(coordinates)
            first_leg[axis] = coordinates[axis] + d
            if legal_move(tuple(first_leg)) or tuple(first_leg) in [(0,3),(4,3)]:

                # now move 1-space in the opposite direction
                for d in [-1,1]:
                    second_leg = first_leg[:]
                    second_leg[opposite_axis] = first_leg[opposite_axis] + d
                    if legal_move(tuple(second_leg)):
                        ret.append(tuple(second_leg))

    return ret


def legal_move(position):
    return True if position in board else False


def sequencer_old(n, depth):
    choices = knight_choices(n)
    if depth > 1:
        depth -= 1
        for c in choices:
            for i in sequencer(c, depth):
                yield 1
    else:
        yield 1


def main_old():
    seq = 0
    depth = 2
    for b in board:
        for i in sequencer(b, depth):
            seq += i
    print seq


def sequencer(n, depth, vowelcount=0):

    vowels = [(0,0), (3,1), (4,0), (4,2)]
    V = 1 if n in vowels else 0
    vowelcount += V

    choices = knight_choices(n)

    if depth > 1:
        depth -= 1
        for c in choices:
            for i, v in sequencer(c, depth, vowelcount):
                #print n,
                yield i, v
    else:
        #print n,
        yield 1, vowelcount

def main(seq, depth):

    VCOUNT = 0 # vowelcount

    for b in board:
        vcount = 0
        for i,v in sequencer(b, depth):
            seq += i
	    if v > 2:
	        vcount += 1
        VCOUNT += vcount
    print '{}'.format(seq - VCOUNT)


if __name__ == '__main__':

    main(seq=0, depth=10)

