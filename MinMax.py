from Node import *
from Heuristic import Heuristic
import numpy as np
from treelib import Node as N, Tree

tree = Tree()


def Max(node, k, f):
    global tree
    if k == 0:
        node.value = Heuristic(node)
        return node.value
    list1 = []
    for i in range(len(node.children)):
        temp = Node(0, -99, 99, node.children[i].col0, node.children[i].col1, node.children[i].col2,
                    node.children[i].col3, node.children[i].col4, node.children[i].col5, node.children[i].col6)
        # n = tree.create_node("0", temp.id, parent=node.id)
        value = Min(temp, k - 1, f)
        # n.tag=value
        list1.append(value)

    node.value = max(list1)
    if k == f:
        # print(node.children[np.argmax(list1)].col0)
        return node.children[np.argmax(list1)], node.value
    return node.value


def Min(node, k, f):
    global tree
    if k == 0:
        node.value = Heuristic(node)
        return node.value
    list1 = []
    for i in range(len(node.children)):
        temp = Node(0, -99, 99, node.children[i].col0, node.children[i].col1, node.children[i].col2,
                    node.children[i].col3, node.children[i].col4, node.children[i].col5, node.children[i].col6)
        # n=tree.create_node("0", temp.id, parent=node.id)
        value = Max(temp, k - 1, f)
        # n.tag=value
        list1.append(value)
    node.value = min(list1)
    if k == f:
        return node.children[np.argmin(list1)], node.value
    return node.value


def MinMax(state, k, f):
    # print(state.col0)
    # global tree
    # n=tree.create_node("0",state.id)
    state1, value = Max(state, k, f)
    state2 = Node(0, 0, 0, state1.col0, state1.col1, state1.col2, state1.col3, state1.col4, state1.col5, state1.col6)
    #print(state2.col0)
    # n.tag=value
    # tree.show()
    return state
