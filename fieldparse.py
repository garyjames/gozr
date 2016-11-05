# fieldparse.py

def parse(lines, types, names=None, sep=None):
    '''
    Parse a line of column oriented data into a list of dictionaries
    or tuples with type conversion.
    '''
    records = []
    for line in lines:
        line = line.strip() # strip whitespace
        if not line:
            continue # ignore blank lines

        fields = line.split(sep)
        
        fields = [f.strip('"') for f in fields] # remove double quotes
        
        # Apply type conversion to the fields 
        cfields = [converter(value) for converter,value in zip(types,fields)]

        # Optionally turn into a dictionary of named fields
        if names:
            record = dict(zip(names,cfields))
        else:
            record = tuple(cfields)

        records.append(record)

    return records
