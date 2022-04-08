import math

from Node import *
from Heuristic import Heuristic
import numpy as np


def Max(node, k, f):
    if k == 0:
        node.value = Heuristic(node)
        return node.value
    list1 = []
    for i in range(len(node.children)):
        temp = Node(0, -99, 99, node.children[i].col0, node.children[i].col1, node.children[i].col2,
                    node.children[i].col3, node.children[i].col4, node.children[i].col5, node.children[i].col6)

        list1.append(Min(temp, k - 1, f))

    node.value = max(list1)
    if k == f:
        return node.children[np.argmax(list1)], node.value
    return node.value


def Min(node, k, f):
    if k == 0:
        node.value = Heuristic(node)
        return node.value
    list1 = []
    for i in range(len(node.children)):
        temp = Node(0, -99, 99, node.children[i].col0, node.children[i].col1, node.children[i].col2,
                    node.children[i].col3, node.children[i].col4, node.children[i].col5, node.children[i].col6)
        list1.append(Max(temp, k - 1, f))
    node.value = min(list1)
    if k == f:
        return node.children[np.argmin(list1)], node.value
    return node.value


def MinMax(state, k, f):
    Max(state, k, f)
