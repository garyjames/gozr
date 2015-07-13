import os

def get_size(start_path='/home/'):
    getsize_error = []
    for dirpath, dirnames, filenames in os.walk(start_path):
	if dirpath == start_path:
	    # initialize
	    users = dirnames
            counter = dict.fromkeys(users, tuple([0, 0]))

	# for each file found, add to respective user's counter
	if filenames:
	    for f in filenames:

	        absolute_path = os.path.join(dirpath, f)

		try:
		    user = absolute_path.replace(start_path, '')
		    # in case trailing '/' in start_path missing
		    user = user.lstrip('/')
		    idx = user.find('/')
		    user = user[:idx]
		    fcount, fsize = counter[user]
		    fcount += 1
		    fsize = fsize + os.path.getsize(absolute_path)
		    counter[user] = fcount, fsize
                except OSError as msg:
		    getsize_error.append(['error geting size for', 
		                         absolute_path, msg])

    return counter, getsize_error
	        
if __name__ == '__main__':
    print get_size()
    print len(get_size())
