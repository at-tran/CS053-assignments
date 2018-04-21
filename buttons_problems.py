# version code 5cbd6dced682+
# Please fill out this stencil and submit using the provided submission script.


## 1: () Solvability of Lights Out
# Write a procedure that returns the button vectors for an nxn board
# Please be sure to use the GF2 one, rather than the int 1.
from GF2 import one
from The_Basis_other_problems import is_superfluous
from matutil import coldict2mat
from vec import Vec
from solver import solve


def button_vectors(n):
    buttons = [(i, j) for i in range(n) for j in range(n)]
    return {button: Vec(set(buttons),
                        {(button[0] + x, button[1] + y): one
                         for x, y in [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]
                         if 0 <= button[0] + x <= n - 1
                         and 0 <= button[1] + y <= n - 1})
            for button in buttons}


# Here is a place for your code for the second subproblem.

def buttons_to_push(n, init):
    """
    :param n: the width and height of an n x n Lights Out table
    :param init: dict of form {(x, y): one}, the initial configuration of the table,
    """
    buttons = [(i, j) for i in range(n) for j in range(n)]
    end_vec = Vec(set(buttons), init)
    buttons_mat = coldict2mat(button_vectors(n))
    sol = solve(buttons_mat, end_vec)
    if buttons_mat * sol == end_vec:
        return {button for button in buttons if sol[button] == one}
    else:
        return None


# Here is a place for your code for the third subproblem

def subset_basis(T):
    '''
    Input:
        - T: a set of Vecs
    Output:
        - set S containing Vecs from T that is a basis for Span T.
    Examples:
        The following tests use the procedure is_independent, provided in module independence
    '''
    res = T
    for v in T.copy():
        if is_superfluous(res, v):
            res.remove(v)
    return res


def n_not_solvable(n):
    return 2 ** (n ** 2) - 2 ** (len(subset_basis(set(button_vectors(n).values()))) ** 2)
