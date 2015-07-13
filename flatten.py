# flatten.py

def flatten(lists):
    for s in lists:
        if isinstance(s, list):
            flatten(s)
        else:
            print s
