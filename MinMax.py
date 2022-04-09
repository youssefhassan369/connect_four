
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
        n = tree.create_node("0", temp.id, parent=node.id)
        value = Min(temp, k-1, f)
        n.tag=value
        list1.append(value)

    node.value = max(list1)
    if k == f:
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
        n=tree.create_node("0", temp.id, parent=node.id)
        value = Max(temp, k - 1, f)
        n.tag=value
        list1.append(value)
    node.value = min(list1)
    if k == f:
        return node.children[np.argmin(list1)], node.value
    return node.value


def MinMax(state, k, f):
    global tree
    n=tree.create_node("0",state.id)
    state, value = Max(state, k, f)
    n.tag=value
    tree.show()

    return state,tree
