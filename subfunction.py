# version code 3ba3eff2f160+
# Please fill out this stencil and submit using the provided submission script.


## 1: () Subfunction
# Write the procedure subfunction(A, V, W) as described in the problem
# You are allowed to use other procedures you have written in previous assignments.
from matutil import coldict2mat
from solver import solve


def subfunction(A, V, W):
    '''
    >>> from vecutil import list2vec
    >>> from matutil import listlist2mat
    >>> A = listlist2mat([[1,1],[1,1]])
    >>> V = [list2vec([0,1])]
    >>> W = [list2vec([0,1]),list2vec([1,0])]
    >>> (Vstar, Wstar) = subfunction(A, V, W)
    >>> len(Vstar)
    1
    >>> abs(Vstar[0][0]) < 1e-6
    True
    >>> abs(Vstar[0][1]) > 1e-6
    True
    >>> len(Wstar)
    1
    >>> abs(Wstar[0][0] - Wstar[0][1]) < 1e-6
    True
    >>> abs(Wstar[0][0]) > 1e-6
    True
    '''

    # Vmat = coldict2mat(V)
    # VWstar = [(Vmat * sol, w) for w in W
    #           for sol in [solve(A * Vmat, w)]
    #           if (w - A * Vmat * sol).is_almost_zero()]
    # return [pair[0] for pair in VWstar], [pair[1] for pair in VWstar]

    Wmat = coldict2mat(W)
    VWstar = [(v, Wmat * sol) for v in V
              for sol in [solve(Wmat, A * v)]
              if (A * v - Wmat * sol).is_almost_zero()]
    return [pair[0] for pair in VWstar], [pair[1] for pair in VWstar]

# kernelV =

# sol = vec2rep([A * v for v in V] + W, 0)

# Vmat = coldict2mat(V)
# VWstar = [(Vmat * sol, w) for w in W
#           for sol in [solve(A * Vmat, w)]
#           if (w - A * Vmat * sol).is_almost_zero()]
# return [pair[0] for pair in VWstar], [pair[1] for pair in VWstar]
