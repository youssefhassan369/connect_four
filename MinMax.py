import math

from Node import Node
from Heuristic import Heuristic
import copy
import numpy as np


def Max(node, k):
    if k == 0:
        return Heuristic(node)
    list1 = []
    for i in range(len(node.children)):
        list1.append(Min(node.children[i], k - 1))
    return max(list1)


def Min(node, k):
    if k == 0:
        return Heuristic(node)
    list1 = []
    for i in range(len(node.children)):
        list1.append(Max(node.children[i], k - 1))
    return min(list1)


def MinMax(k,state):
    Max(state,k)

