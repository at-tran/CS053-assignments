# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist):
    return [dct[x] for x in keylist]

def list2dict(L, keylist):
    return {a:b for a, b in zip(keylist, L)}
