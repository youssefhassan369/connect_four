import copy


def changeCol(col):
    index = col.find('e')
    if index == -1:
        return -1
    temp = list(col)
    temp[index] = 'r'
    return "".join(temp)


def GenerateChildren(state):
    list1 = []
    if changeCol(state.col0) != -1:
        child0 = copy.copy(state)
        child0.col0 = changeCol(state.col0)
        list1.append(child0)

    if changeCol(state.col1) != -1:
        child1 = copy.copy(state)
        child1.col1 = changeCol(state.col1)
        list1.append(child1)

    if changeCol(state.col2) != -1:
        child2 = copy.copy(state)
        child2.col2 = changeCol(state.col2)
        list1.append(child2)

    if changeCol(state.col3) != -1:
        child3 = copy.copy(state)
        child3.col3 = changeCol(state.col3)
        list1.append(child3)

    if changeCol(state.col4) != -1:
        child4 = copy.copy(state)
        child4.col4 = changeCol(state.col4)
        list1.append(child4)
    if changeCol(state.col5) != -1:
        child5 = copy.copy(state)
        child5.col5 = changeCol(state.col5)
        list1.append(child5)

    if changeCol(state.col6) != -1:
        child6 = copy.copy(state)
        child6.col6 = changeCol(state.col6)
        list1.append(child6)

    return list1


class Node:
    def __init__(self, value, alpha, beta, col0, col1, col2, col3, col4, col5, col6):
        self.value = value
        self.alpha = alpha
        self.beta = beta
        self.col0 = col0
        self.col1 = col1
        self.col2 = col2
        self.col3 = col3
        self.col4 = col4
        self.col5 = col5
        self.col6 = col6
        self.children = GenerateChildren(self)
