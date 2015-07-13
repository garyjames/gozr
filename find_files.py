import glob

def find_files(s):
    found = []
    try:
	s = str(s)
        found = glob.iglob(s)	
    except TypeError:
        for item in s:
            found.append(glob.iglob(item))

    return found
