from Node import *
from math import inf


def GameEnd(state):
    return state.col0.find('e') + state.col1.find('e') + state.col2.find('e') + state.col3.find('e') + state.col4.find \
        ('e') + state.col5.find('e') + state.col6.find('e') == -7


def generateInitialState():
    node1 = Node(0, -inf, inf, 'eeeeee', 'eeeeee', 'eeeeee', 'eeeeee', 'eeeeee', 'eeeeee', 'eeeeee')
    return node1


def Score(state):
    UserScore = 0
    CompScore = 0
    step = 6
    Rows = 6
    Columns = 7
    total_string = state.col0 + state.col1 + state.col2 + state.col3 + state.col4 + state.col5 + state.col6

    for i in range(0, Rows):
        for j in range(0, Columns - 3):
            # checking rows for user
            if total_string[i + (j * step)] == 'y' and total_string[i + (j * step) + (step * 1)] == 'y' and \
                    total_string[i + (j * step) + (step * 2)] == 'y' and total_string[
                i + (j * step) + (step * 3)] == 'y':
                UserScore += 1
            # checking rows of computer
            if total_string[i + (j * step)] == 'r' and total_string[i + (j * step) + (step * 1)] == 'r' and \
                    total_string[i + (j * step) + (step * 2)] == 'r' and total_string[
                i + (j * step) + (step * 3)] == 'r':
                CompScore += 1

    for i in range(0, Columns):
        for j in range(0, Rows - 3):
            # checking columns for user
            if total_string[i * step + j] == 'y' and total_string[i * step + j + 1] == 'y' and total_string[
                i * step + j + 2] == 'y' and total_string[i * step + j + 3] == 'y':
                UserScore += 1
            # checking columns for computer
            if total_string[i * step + j] == 'r' and total_string[i * step + j + 1] == 'r' and total_string[
                i * step + j + 2] == 'r' and total_string[i * step + j + 3] == 'r':
                CompScore += 1

    for i in range(0, Rows - 3):
        for j in range(0, Columns - 3):
            # checking +ve diag for user
            if total_string[i + (j * step)] == 'y' and total_string[i + (j * step) + (step * 1) + 1] == 'y' and \
                    total_string[i + (j * step) + (step * 2) + 2] == 'y' and total_string[
                i + (j * step) + (step * 3) + 3] == 'y':
                UserScore += 1
            # checking +ve diag for computer
            if total_string[i + (j * step)] == 'r' and total_string[i + (j * step) + (step * 1) + 1] == 'r' and \
                    total_string[i + (j * step) + (step * 2) + 2] == 'r' and total_string[
                i + (j * step) + (step * 3) + 3] == 'r':
                CompScore += 1

    for j in range(0, Rows - 2):
        for i in range(3, Columns - 1):
            # checking _ve diag for user
            if total_string[i + (j * step) + (step * 3) - 3] == 'y' and total_string[
                i + (j * step) + (step * 2) - 2] == 'y' and total_string[i + (j * step) + (step * 1) - 1] == 'y' and \
                    total_string[i + (j * step)] == 'y':
                UserScore += 1
            # checking _ve diag for computer
            if total_string[i + (j * step) + (step * 3) - 3] == 'r' and total_string[
                i + (j * step) + (step * 2) - 2] == 'r' and total_string[i + (j * step) + (step * 1) - 1] == 'r' and \
                    total_string[i + (j * step)] == 'r':
                CompScore += 1

    return UserScore, CompScore
