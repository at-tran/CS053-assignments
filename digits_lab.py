# version code 0caa61797a35+
# Please fill out this stencil and submit using the provided submission script.

import time  # for timing
from mnist_loader import load_data
import svd
from matutil import *
from vecutil import *
import random
from orthonormalization import orthonormalize


## 1: () Squared Distance
def sq_dist(u, v):
    '''
    Input:
        - u, v: two Vecs with the same domain
    Output:
        - the square of the Euclidean distance between u and v
    Example:
        >>> u = list2vec([1, 2])
        >>> v = list2vec([2, 3])
        >>> sq_dist(u, v)
        2
    '''
    return sum((u[i] - v[i]) ** 2 for i in u.D)


## 2: () Nearest Neighbor
def nn(u, veclist):
    '''
    Input:
        - u: a Vec
        - veclist: a list of Vecs
    Output:
        - The index of the vector in veclist nearest to u
    Example:
        >>> from vecutil import list2vec
        >>> nn(list2vec([1,2]), [list2vec(l) for l in [[2,5],[1,3],[1.5,2]]])
        2
    '''
    return min(range(len(veclist)), key=lambda i: sq_dist(u, veclist[i]))


## 3: () Nearest Neighbor Label
def nn_label(u, veclist, labels):
    '''
    Input:
        - u: a Vec
        - veclist: a list of Vecs
        - labels: a list of labels, one for each Vec in veclist
    Output:
        - the label of the vector in veclist nearest to u
    Example:
        >>> from vecutil import list2vec
        >>> u = list2vec([1,2])
        >>> veclist = [list2vec(l) for l in [[2,5],[1,3],[1.5,2]]]
        >>> labels = [0, 1, 0]
        >>> nn_label(u, veclist, labels)
        0
    '''
    return labels[nn(u, veclist)]


## 4: () Error Rate
def error_rate(guessed_labels, correct_labels):
    '''
    Input:
        - guessed_labels: a list of guessed labels
        - correct_labels: a list of true labels
    Output:
        - the fraction of guessed labels that are not equal to the corresponding correct label
    Example:
        >>> error_rate([0, 1, 0, 1, 1], [0, 1, 2, 3, 4])
        0.6
    '''
    return sum(guess != correct for guess, correct in zip(guessed_labels, correct_labels)) / len(guessed_labels)


# Load training and testing data
images, labels = load_data()
train_images = images[:3000]
train_labels = labels[:3000]
test_images = images[3000:3100]
test_labels = labels[3000:3100]

## 5: () Predictions from Nearest Neighbor on Image Vectors
guessed_labels_raw = [3, 5, 1, 4, 1, 9, 7, 7, 0, 5, 8, 1, 4, 2, 2, 1, 5, 2, 0, 1, 2, 4, 9, 1, 9, 2, 5, 7, 1, 6, 7, 5, 1,
                      5, 4, 4, 9, 1, 1, 7, 8, 0, 2, 4, 5, 2, 7, 6, 9, 4, 1, 7, 3, 1, 1, 1, 1, 7, 3, 9, 7, 7, 1, 1, 2, 0,
                      8, 3, 5, 6, 1, 3, 1, 4, 3, 8, 6, 7, 2, 6, 7, 1, 9, 2, 6, 3, 6, 2, 7, 8, 8, 8, 6, 4, 6, 7, 2, 1, 2,
                      8]

## 6: () Error Rate for Nearest Neighbor on Image Vectors
raw_nn_error_rate = 0.09


## 7: (Task 11.6.2) Procedure to Find Centroid
def find_centroid(veclist):
    '''
    Input:
        - veclist: a list of Vecs
    Output:
        - a Vec, the centroid of veclist
    Example:
        >>> from vecutil import list2vec
        >>> vs = [list2vec(l) for l in [[1,2,3],[2,3,4],[9,10,11]]]
        >>> find_centroid(vs)
        Vec({0, 1, 2},{0: 4.0, 1: 5.0, 2: 6.0})
    '''
    return sum(veclist) / len(veclist)


## 8: () Centroid of Training Images
centroid = find_centroid(train_images)

## 9: () Centered Training Images
centered_train_images = [v - centroid for v in train_images]

## 10: () Centered Test Images
centered_test_images = [v - centroid for v in test_images]

## 11: () Right Singular Vectors
right_singular_vs = ...

## 12: () 10 Principal Components
M10 = ...

## 13: () Predictions from Nearest Neighbor on 10 Principal Components
# From your Python interaction, copy the list of labels that nearest neighbor assigns
# to the 100 test images; paste the list here.

guessed_labels_10 = ...

## 14: () Error Rate for Nearest Neighbor on 10 Principal Components
# In your Python interaction, find the error rate of nearest neighbor, and enter it here.

svd10_nn_error_rate = ...

## 15: () 20 Principal Components
M20 = ...

## 16: () Predictions from Nearest Neighbor on 20 Principal Components
# From your Python interaction, copy the list of labels that nearest neighbor assigns
# to the 100 test images; paste the list here.

guessed_labels_20 = ...

## 17: () Error Rate for Nearest Neighbor on 20 Principal Components
# In your Python interaction, find the error rate of nearest neighbor, and enter it here.

svd20_nn_error_rate = ...
