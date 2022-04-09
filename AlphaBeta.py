from Heuristic import Heuristic
from Node import Node
from math import inf
from treelib import Tree
import numpy as np


def AlphaBetaMin(node, k, f, tree, count):
    count += 1
    if k == 0:
        computer = Heuristic(node, 'r', 'y')
        user = Heuristic(node, 'y', 'r')
        node.value = computer - 2 * user
        return node.value, count
    list1 = []
    for i in range(len(node.children)):
        temp = Node(0, node.beta, inf, node.children[i].col0, node.children[i].col1, node.children[i].col2,
                    node.children[i].col3, node.children[i].col4, node.children[i].col5, node.children[i].col6)

        n = tree.create_node("0", temp.id, parent=node.id)

        value, count = AlphaBetaMax(temp, k - 1, f, tree, count)
        list1.append(value)
        best = min(list1)
        node.beta = min(node.beta, best)
        n.tag = str(value) + ',' + str(node.alpha) + ',' + str(node.beta)
        if node.beta <= node.alpha:
            break
    if len(list1) == 0:
        computer = Heuristic(node, 'r', 'y')
        user = Heuristic(node, 'y', 'r')
        node.value = computer - 2 * user

        return node.value, count
    node.value = min(list1)
    if k == f:
        return node.children[np.argmin(list1)], node.value, node.alpha, node.beta, count
    return node.value, count


def AlphaBetaMax(node, k, f, tree, count):
    count += 1
    print(count)
    if k == 0:
        computer = Heuristic(node, 'r', 'y')
        user = Heuristic(node, 'y', 'r')
        node.value = computer - 2 * user
        return node.value, count
    list1 = []
    for i in range(len(node.children)):
        temp = Node(0, -inf, node.alpha, node.children[i].col0, node.children[i].col1, node.children[i].col2,
                    node.children[i].col3, node.children[i].col4, node.children[i].col5, node.children[i].col6)

        n = tree.create_node("0", temp.id, parent=node.id)

        value, count = AlphaBetaMin(temp, k - 1, f, tree, count)
        list1.append(value)
        best = max(list1)
        node.alpha = max(node.alpha, best)
        n.tag = str(value) + ',' + str(node.alpha) + ',' + str(node.beta)
        if node.alpha >= node.beta:
            break
    if len(list1) == 0:
        computer = Heuristic(node, 'r', 'y')
        user = Heuristic(node, 'y', 'r')
        node.value = computer - 2 * user

        return node.value, count
    node.value = max(list1)
    if k == f:
        return node.children[np.argmax(list1)], node.value, node.alpha, node.beta, count
    return node.value, count


def AlphaBeta(state, k, f):
    count = 0

    tree = Tree()
    n = tree.create_node("0", state.id)
    state1, value, alpha, beta, count = AlphaBetaMax(state, k, f, tree, count)
    state2 = Node(0, 0, 0, state1.col0, state1.col1, state1.col2, state1.col3, state1.col4, state1.col5, state1.col6)
    n.tag = str(value) + ',' + str(alpha) + ',' + str(beta)
    tree.show()

    return state2, count
