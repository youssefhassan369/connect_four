from Heuristic import Heuristic
from Node import *
from MinMax import *
from math import inf


def AlphaBetaMin(node, k, f):
    if k == 0:
        node.value = Heuristic(node)
        return node.value
    list1 = []
    for i in range(len(node.children)):
        temp = Node(0,node.beta,inf, node.children[i].col0, node.children[i].col1, node.children[i].col2,
                    node.children[i].col3, node.children[i].col4, node.children[i].col5, node.children[i].col6)
        list1.append(Max(temp, k - 1, f))
        best = min(list1)
        node.beta = min(node.beta, best)
        if node.beta <= node.alpha:
            break
    node.value = min(list1)
    if k == f:
        return node.children[np.argmin(list1)], node.value
    return node.value


def AlphaBetaMax(node, k, f):
    if k == 0:
        node.value = Heuristic(node)
        return node.value
    list1 = []
    for i in range(len(node.children)):
        temp = Node(0, -inf, node.alpha, node.children[i].col0, node.children[i].col1, node.children[i].col2,
                    node.children[i].col3, node.children[i].col4, node.children[i].col5, node.children[i].col6)

        list1.append(Min(temp, k - 1, f))
        best = max(list1)
        node.alpha = max(node.alpha, best)
        if temp.alpha >= temp.beta:
            break

    node.value = max(list1)
    if k == f:
        return node.children[np.argmax(list1)], node.value
    return node.value

def AlphaBeta(state,k,f):
    node,val=AlphaBetaMax(state,k,f)
    print(node.col3)
