from Node import *
from Heuristic import Heuristic
import numpy as np
from treelib import Node as N, Tree




def Max(node, k, f,tree,count):

    count+=1

    if k == 0:
        computer = Heuristic(node, 'r', 'y')
        user = Heuristic(node, 'y', 'r')
        node.value = computer - 2 * user

        return node.value,count
    list1 = []
    for i in range(len(node.children)):
        temp = Node(0, -99, 99, node.children[i].col0, node.children[i].col1, node.children[i].col2,
                    node.children[i].col3, node.children[i].col4, node.children[i].col5, node.children[i].col6)
        n = tree.create_node("0", temp.id, parent=node.id)
        value,count = Min(temp, k - 1, f,tree,count)
        n.tag=value
        list1.append(value)
    if len(list1)==0:
        computer = Heuristic(node, 'r', 'y')
        user = Heuristic(node, 'y', 'r')
        node.value = computer - 2 * user

        return node.value,count
    node.value = max(list1)
    if k == f:

        return node.children[np.argmax(list1)], node.value,count
    return node.value,count


def Min(node, k, f,tree,count):

    count += 1
    if k == 0:
        computer = Heuristic(node, 'r', 'y')
        user = Heuristic(node, 'y', 'r')
        node.value = computer - 2 * user

        return node.value,count
    list1 = []
    for i in range(len(node.children)):
        temp = Node(0, -99, 99, node.children[i].col0, node.children[i].col1, node.children[i].col2,
                    node.children[i].col3, node.children[i].col4, node.children[i].col5, node.children[i].col6)
        n=tree.create_node("0", temp.id, parent=node.id)
        value,count = Max(temp, k - 1, f,tree,count)
        n.tag=value
        list1.append(value)
    if len(list1)==0:
        computer = Heuristic(node, 'r', 'y')
        user = Heuristic(node, 'y', 'r')
        node.value = computer - 2 * user

        return node.value,count
    node.value = min(list1)
    if k == f:
        return node.children[np.argmin(list1)], node.value,count
    return node.value,count


def MinMax(state, k, f):
    tree=Tree()

    count=0

    n=tree.create_node("0",state.id)
    state1, value,count = Max(state, k, f,tree,count)
    state2 = Node(0, 0, 0, state1.col0, state1.col1, state1.col2, state1.col3, state1.col4, state1.col5, state1.col6)
    n.tag=value
    tree.show()


    return state2,count
