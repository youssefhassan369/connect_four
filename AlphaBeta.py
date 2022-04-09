from Heuristic import Heuristic
from Node import Node
from MinMax import *
from math import inf
from treelib import Node as N, Tree
tree = Tree()

def AlphaBetaMin(node, k, f):
    global tree
    if k == 0:
        node.value = Heuristic(node)
        return node.value
    list1 = []
    for i in range(len(node.children)):
        temp = Node(0, node.beta, inf, node.children[i].col0, node.children[i].col1, node.children[i].col2,
                    node.children[i].col3, node.children[i].col4, node.children[i].col5, node.children[i].col6)
        print('min')
        n = tree.create_node("0", temp.id, parent=node.id)
        print(n)
        value=Max(temp, k - 1, f)
        list1.append(value)
        best = min(list1)
        node.beta = min(node.beta, best)
        n.tag = value + ',' + node.alpha + ',' + node.beta
        if node.beta <= node.alpha:
            break
    node.value = min(list1)
    if k == f:
        return node.children[np.argmin(list1)], node.value
    return node.value


def AlphaBetaMax(node, k, f):
    global tree
    if k == 0:
        node.value = Heuristic(node)
        return node.value
    list1 = []
    for i in range(len(node.children)):
        temp = Node(0, -9999, node.alpha, node.children[i].col0, node.children[i].col1, node.children[i].col2,
                    node.children[i].col3, node.children[i].col4, node.children[i].col5, node.children[i].col6)
        print('max')
        n = tree.create_node("0", temp.id, parent=node.id)
        #print(n)
        value = Min(temp, k - 1, f)
        list1.append(value)
        best = max(list1)
        node.alpha = max(node.alpha, best)
        n.tag = value + ',' + node.alpha + ',' + node.beta
        if temp.alpha >= temp.beta:
            break

    node.value = max(list1)
    if k == f:
        return node.children[np.argmax(list1)], node.value
    return node.value


def AlphaBeta(state, k, f):
    #global tree
    #n=tree.create_node("0", state.id)
    state1, value = AlphaBetaMax(state, k, f)
    state2 = Node(0, 0, 0, state1.col0, state1.col1, state1.col2, state1.col3, state1.col4, state1.col5, state1.col6)
    #n.tag = value + ',' + state.alpha + ',' + state.beta
    #tree.show()

    return state2
