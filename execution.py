# execution.py

def execution(fixmsg, tags={'ClOrdID': '11', 'LastShares': '32', 'Symbol': '55'}):
    # identify an execution from the fixmsg tuple
    tag_values = {}
    for tag in tags:
        for i in fixmsg:
            if i.startswith(tags[tag]+'='):
                tag_values[tag] = i.split('=')[1]
    #if len(tag_values) == len(tags):
    return tag_values

