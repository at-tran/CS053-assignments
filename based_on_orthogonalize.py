# version code 3df3986b06e3+
# Please fill out this stencil and submit using the provided submission script.

from orthogonalization import orthogonalize


## 1: () Basis Function
def basis(vlist):
    '''
    Input:
        - vlist: a list of Vecs
    Output:
        - a list of linearly independent Vecs with equal span to vlist
    '''
    return [v for v in orthogonalize(vlist) if not v.is_almost_zero()]


## 2: () Subset Basis
def subset_basis(vlist):
    '''
    Input:
        - vlist: a list of Vecs
    Output:
        - linearly independent subset of vlist with the same span as vlist
    '''
    return [vlist[i] for i in range(len(vlist)) if not orthogonalize(vlist)[i].is_almost_zero()]
