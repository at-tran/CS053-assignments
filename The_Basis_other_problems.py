# version code d70bb75e3fb2+
# Please fill out this stencil and submit using the provided submission script.

from matutil import coldict2mat
from solver import solve
from vec import Vec
from vecutil import list2vec



## 1: () Superfluous Vector in Python
def is_superfluous(S, v):
    '''
    Input:
        - S: set of vectors as instances of Vec class
        - v: vector in S as instance of Vec class
    Output:
        True if the span of the vectors of S is the same
        as the span of the vectors of S, excluding v.

        False otherwise.
    Examples:
    >>> from vec import Vec
    >>> D={'a','b','c','d'}
    >>> S = {Vec(D, {'a':1,'b':-1}), Vec(D, {'c':-1,'b':1}), Vec(D, {'c':1,'d':-1}), Vec(D, {'a':-1,'d':1}), Vec(D, {'b':1, 'c':1, 'd':-1})}
    >>> is_superfluous(S,Vec(D, {'b':1, 'c':1, 'd':-1}))
    False
    >>> is_superfluous(S,Vec(D, {'a':-1,'d':1}))
    True
    >>> is_superfluous(S,Vec(D, {'c':1,'d':-1}))
    True
    >>> S == {Vec(D,{'a':1,'b':-1}),Vec(D,{'c':-1,'b':1}),Vec(D,{'c':1,'d':-1}),Vec(D, {'a':-1,'d':1}),Vec(D,{'b':1, 'c':1, 'd':-1})}
    True
    >>> is_superfluous({Vec({0,1}, {})}, Vec({0,1}, {}))
    True
    >>> is_superfluous({Vec({0,1}, {0:1})}, Vec({0,1}, {0:1}))
    False
    >>> from GF2 import one
    >>> from vecutil import list2vec
    >>> S = {list2vec(v) for v in [[one,0,0,0],[0,one,0,0],[0,0,one,0],[0,0,0,one],[one,one,one,0]]}
    >>> is_superfluous(S, list2vec([one,0,0,0])) 
    True
    >>> is_superfluous(S, list2vec([one,one,one,0])) 
    True
    >>> is_superfluous(S, list2vec([0,0,0,one])) 
    False
    >>> S = {list2vec(v) for v in [[one,one,one,0,one],[0,0,one,0,one],[0,one,one,0,0],[0,one,one,one,one]]} 
    >>> is_superfluous(S, list2vec([0,one,one,one,one])) 
    False
    >>> L = [list2vec(v) for v in [[1,2,4,8],[2,4,8,16],[0,1,2,3]]]
    >>> is_superfluous(set(L), L[0])
    True
    >>> is_superfluous(set(L), L[1])
    True
    >>> is_superfluous(set(L), L[2])
    False
    >>> is_superfluous({list2vec([1,2]),list2vec([2,4])}, list2vec([1,2]))
    True
    '''
    assert v in S
    if len(S) == 1:
        return list(S)[0] == -list(S)[0]
    
    S = S.copy()
    S.remove(v)
    A = coldict2mat(list(S))
    resid = v - A * solve(A, v)
    return resid.is_almost_zero()



## 2: () is_independent in Python
def is_independent(S):
    '''
    Input:
        - S: a set of Vecs
    Output:
        - boolean: True if vectors in S are linearly independent
    Examples:
    >>> is_independent(set())
    True
    >>> is_independent({Vec({'a'},{})})
    False
    >>> is_independent({Vec({'a'},{'a':1})})
    True
    >>> is_independent({list2vec(v) for v in [[1,2,1],[2,1,2],[1,1,1]]})
    False
    >>> is_independent({list2vec(v) for v in [[1,2,1],[2,1,2],[1,1,0]]})
    True
    >>> from GF2 import one
    >>> from vecutil import list2vec
    >>> is_independent({list2vec(v) for v in [[one,one,0],[0,one,one],[one,0,one],[one,0,0]]})
    False
    >>> is_independent({list2vec(v) for v in [[one,one,0,0,0],[0,one,0,0,one],[0,0,one,one,0],[0,0,0,one,one],[one,0,0,0,one]]})
    False
    >>> is_independent({list2vec(v) for v in [[one,one,0,0,0],[0,one,one,0,0],[0,0,one,one,0],[0,0,0,one,one]]})
    True
    '''
    return len([v for v in S if is_superfluous(S, v)]) == 0



## 3: () Exchange Lemma in Python
def exchange(S, A, z):
    '''
    Input:
        - S: a set of Vecs (not necessarily linearly independent)
        - A: a set of Vecs, a proper subset of S
        - z: an instance of Vec such that A | {z} is linearly independent
    Output: a vector w in S but not in A such that Span S = Span ({z} | S - {w})
    Examples:
        >>> from vecutil import list2vec
        >>> from vec import Vec
        >>> S = {list2vec(v) for v in [[0,0,5,3],[2,0,1,3],[0,0,1,0],[1,2,3,4]]}
        >>> A = {list2vec(v) for v in [[0,0,5,3],[2,0,1,3]]}
        >>> z = list2vec([0,2,1,1])
        >>> (exchange(S, A, z) == Vec({0, 1, 2, 3},{0: 0, 1: 0, 2: 1, 3: 0})) or (exchange(S, A, z) == Vec({0, 1, 2, 3},{0: 1, 1: 2, 2: 3, 3: 4}))
        True
        >>> S == {list2vec(v) for v in [[0,0,5,3],[2,0,1,3],[0,0,1,0],[1,2,3,4]]}
        True
        >>> A == {list2vec(v) for v in [[0,0,5,3],[2,0,1,3]]}
        True
        >>> z == list2vec([0,2,1,1])
        True
        >>> from GF2 import one
        >>> S = {Vec({0,1,2,3,4}, {i:one, (i+1)%5:one}) for i in range(5)}
        >>> A = {list2vec([0,one,one,0,0]),list2vec([0,0,one,one,0])}
        >>> z = list2vec([0,0,one,0,one])
        >>> exchange(S, A, z) in {list2vec(v) for v in [[one, one,0,0,0],[one,0,0,0,one],[0,0,0,one,one]]}
        True
        >>> S = {list2vec(v) for v in [[one,0,one,0],[one,one,one,one],[one,one,0,0],[one,one,one,0]]}
        >>> A = {list2vec([one,one,one,0])}
        >>> z = list2vec([0,one,0,0])
        >>> exchange(S, A, z) == list2vec([one,0,one,0])
        True
        >>> S = {list2vec(v) for v in [[0, 0, 0, one], [0, one, one, one], [0, 0, one, one], [one, 0, 0, 0], [0, one, one, 0]]}
        >>> A = {list2vec(v) for v in [[0, one, one, one], [0, 0, 0, one]]}
        >>> z = list2vec([0, one, 0, one])
        >>> exchange(S, A, z) in [list2vec([0, 0, one, one]), list2vec([0, one, one, 0])]
        True
    '''
    pass

