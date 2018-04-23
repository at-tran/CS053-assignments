# version code c2eb1c41017f+
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from independence import is_independent


## 1: (Task 7.7.1) Choosing a Secret Vector
def randGF2(): return random.randint(0, 1) * one


a0 = list2vec([one, one, 0, one, 0, one])
b0 = list2vec([one, one, 0, 0, 0, one])


def rand_6vec():
    return list2vec([randGF2() for _ in range(6)])


def choose_secret_vector(s, t):
    while True:
        u = rand_6vec()
        if a0 * u == s and b0 * u == t:
            return u


## 2: (Task 7.7.2) Finding Secret Sharing Vectors
# Give each vector as a Vec instance


def find_vectors():
    """
    Find 4 vector pairs so that for any 3 pairs,
    the corresponding 6 vectors are linearly independent.
    """
    while True:
        a = [a0] + [rand_6vec() for _ in range(4)]
        b = [b0] + [rand_6vec() for _ in range(4)]
        if all(is_independent([a[i], b[i], a[j], b[j], a[k], b[k]])
               for i in range(5)
               for j in range(i + 1, 5)
               for k in range(j + 1, 5)):
            return a, b


a, b = find_vectors()

secret_a0 = a0
secret_b0 = b0
secret_a1 = a[1]
secret_b1 = b[1]
secret_a2 = a[2]
secret_b2 = b[2]
secret_a3 = a[3]
secret_b3 = b[3]
secret_a4 = a[4]
secret_b4 = b[4]

## Sharing a long string
