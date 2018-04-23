# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec
from GF2 import one

from factoring_support import dumb_factor
from factoring_support import intsqrt
from factoring_support import gcd
from factoring_support import primes
from factoring_support import prod

import echelon


def root_method(n):
    a = intsqrt(n)
    while a * a <= n: a = a + 1

    for _ in range(1000):
        b = intsqrt(a * a - n)
        if a * a - b * b == n:
            return a - b

    return None


## Task 1
def int2GF2(i):
    """
    Returns one if i is odd, 0 otherwise.

    Input:
        - i: an int
    Output:
        - one if i is congruent to 1 mod 2
        - 0   if i is congruent to 0 mod 2
    Examples:
        >>> int2GF2(3)
        one
        >>> int2GF2(100)
        0
    """
    return (i % 2) * one


## Task 2
def make_Vec(primeset, factors):
    """
    Input:
        - primeset: a set of primes
        - factors: a list of factors [(p_1,a_1), ..., (p_n, a_n)]
                   with p_i in primeset
    Output:
        - a vector v over GF(2) with domain primeset
          such that v[p_i] = int2GF2(a_i) for all i
    Example:
        >>> make_Vec({2,3,11}, [(2,3), (3,2)]) == Vec({2,3,11},{2:one})
        True
    """
    return Vec(primeset, {p: int2GF2(ex) for p, ex in factors})


## Task 3
def find_candidates(N, primeset):
    """
    Input:
        - N: an int to factor
        - primeset: a set of primes

    Output:
        - a tuple (roots, rowlist)
        - roots: a list a_0, a_1, ..., a_n where a_i*a_i - N can be factored
                 over primeset
        - rowlist: a list such that rowlist[i] is a
                   primeset-vector over GF(2) corresponding to a_i
          such that len(roots) = len(rowlist) and len(roots) > len(primeset)
    Example:
        >>> from factoring_support import primes
        >>> N = 2419
        >>> primeset = primes(32)
        >>> roots, rowlist = find_candidates(N, primeset)
        >>> set(roots) == {51, 52, 53, 58, 61, 62, 63, 67, 68, 71, 77, 79}
        True
        >>> D = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        >>> set(rowlist) == {Vec(D,{2: one, 13: one, 7: one}), Vec(D,{3: one, 19: one, 5: one}), Vec(D,{2: one, 3: one, 5: one, 13: one}), Vec(D,{3: one, 5: one, 7: one}), Vec(D,{7: one, 2: one, 3: one, 31: one}), Vec(D,{3: one, 19: one}), Vec(D,{2: one, 31: one}), Vec(D,{2: one, 5: one, 23: one}), Vec(D,{5: one}), Vec(D,{3: one, 2: one, 19: one, 23: one}), Vec(D,{2: one, 3: one, 5: one, 13: one}), Vec(D,{2: one, 3: one, 13: one})}
        True
    """
    roots = []
    rowlist = []
    len_roots = 0
    x = intsqrt(N) + 1
    while len_roots < len(primeset) + 1:
        x = x + 1
        factors = dumb_factor(x * x - N, primeset)
        if factors:
            roots.append(x)
            rowlist.append(make_Vec(primeset, factors))
            len_roots = len_roots + 1
    return roots, rowlist


## Task 4
def find_a_and_b(v, roots, N):
    """
    Input:
     - a {0,1,..., n-1}-vector v over GF(2) where n = len(roots)
     - a list roots of integers
     - an integer N to factor
    Output:
      a pair (a,b) of integers
      such that a*a-b*b is a multiple of N
      (if v is correctly chosen)
    Example:
        >>> roots = [51, 52, 53, 58, 61, 62, 63, 67, 68, 71, 77, 79]
        >>> N = 2419
        >>> v = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},{1: one, 2: one, 11: one, 5: one})
        >>> find_a_and_b(v, roots, N)
        (13498888, 778050)
        >>> v = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},{0: 0, 1: 0, 10: one, 2: one})
        >>> find_a_and_b(v, roots, N)
        (4081, 1170)
    """
    alist = [roots[i] for i in range(len(roots)) if v[i] != 0]
    a = prod(alist)
    c = prod([x * x - N for x in alist])
    b = intsqrt(c)
    assert b * b == c
    return a, b


## Task 5

nontrivial_divisor_of_2461799993978700679 = 1230926561
