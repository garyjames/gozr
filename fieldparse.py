# fieldparse.py

def parse(lines, types, names=None, sep=None):
    '''
    Parse a line of column oriented data into a list of dictionaries
    or tuples with type conversion.
    '''

    from collections import namedtuple

    if names:
        records = namedtuple('records', names)
    else:
        records = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        fields = line.split(sep)
        
        # Get rid of double quotes
        fields = [f.strip('"') for f in fields]
        
        # Apply type conversion to the fields 
        cfields = [converter(value) for converter,value in zip(types,fields)]

        # Optionally turn into a dictionary of named fields
        if names is not None:
            records(zip(names,cfields))
        else:
            record = tuple(cfields)

        # Save the record
        records.append(record)

    return records
