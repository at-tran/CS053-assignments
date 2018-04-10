# version code 9f73479f460b+
# Please fill out this stencil and submit using the provided submission script.
from GF2 import one
from The_Basis_problems import is_independent
from matutil import coldict2mat
from vecutil import list2vec
from solver import solve

## 1: () Exchange Lemma in Python
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
    S = list(S)
    sol = solve(coldict2mat(S), z)
    for i in sol.D:
        if sol[i] != 0 and S[i] not in A:
            return S[i]


## 2: () Subset Basis
def subset_basis(T):
    '''
    Input:
        - T: a set of Vecs
    Output: 
        - set S containing Vecs from T that is a basis for Span T.
    Examples:
        The following tests use the procedure is_independent, provided in module independence
        
        >>> from vec import Vec
        >>> from independence import is_independent
        >>> a0 = Vec({'a','b','c','d'}, {'a':1})
        >>> a1 = Vec({'a','b','c','d'}, {'b':1})
        >>> a2 = Vec({'a','b','c','d'}, {'c':1})
        >>> a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})
        >>> sb = subset_basis({a0, a1, a2, a3})
        >>> len(sb)
        3
        >>> all(v in [a0, a1, a2, a3] for v in sb)
        True
        >>> is_independent(sb)
        True

        >>> b0 = Vec({0,1,2,3},{0:2,1:2,3:4})
        >>> b1 = Vec({0,1,2,3},{0:1,1:1})
        >>> b2 = Vec({0,1,2,3},{2:3,3:4})
        >>> b3 = Vec({0,1,2,3},{3:3})
        >>> sb = subset_basis({b0, b1, b2, b3})
        >>> len(sb)
        3
        >>> all(v in [b0, b1, b2, b3] for v in sb)
        True
        >>> is_independent(sb)
        True

        >>> D = {'a','b','c','d'}
        >>> c0, c1, c2, c3, c4 = Vec(D,{'d': one, 'c': one}), Vec(D,{'d': one, 'a': one, 'c': one, 'b': one}), Vec(D,{'a': one}), Vec(D,{}), Vec(D,{'d': one, 'a': one, 'b': one})
        >>> subset_basis({c0,c1,c2,c3,c4}) == {c0,c1,c2,c4}
        True
    '''
    res = set()
    for v in T:
        if is_independent(list(res | {v})):
            res.add(v)
    return res


## 3: () Superset Basis Lemma in Python
def superset_basis(C, T):
    '''
    Input:
        - C: linearly independent set of Vecs
        - T: set of Vecs such that every Vec in C is in Span(T)
    Output:
        Linearly independent set S consisting of all Vecs in C and some in T
        such that the span of S is the span of T (i.e. S is a basis for the span
        of T).
    Example:
        >>> from vec import Vec
        >>> from independence import is_independent
        >>> a0 = Vec({'a','b','c','d'}, {'a':1})
        >>> a1 = Vec({'a','b','c','d'}, {'b':1})
        >>> a2 = Vec({'a','b','c','d'}, {'c':1})
        >>> a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})
        >>> sb = superset_basis({a0, a3}, {a0, a1, a2})
        >>> a0 in sb and a3 in sb
        True
        >>> is_independent(sb)
        True
        >>> all(x in [a0,a1,a2,a3] for x in sb)
        True
    '''
    pass
