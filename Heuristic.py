from Node import *
from functions import *
Rows=6
Columns=7

def Heuristic(node):
    total_string=node.col0+node.col1+node.col2+node.col3+node.col4+node.col5+node.col6
    return FindMatchingRow(total_string)+FindMatchingCol(node)+FindMatchingDiag1(node)+FindMatchingDiag2(node)   #weights will be added

def FindMatchingRow(total_string):
    Row_score=0
    step=6
    # check 3 able to be 4
    # 3 red after each other (4th empty on the right)
    for i in range (0,Rows):
        for j in range (0,Columns-3):
            if total_string[i+(j*step)]=='r' and total_string[i+(j*step)+(step*1)]=='r' and total_string[i+(j*step)+(step*2)]=='r' and total_string[i+(j*step)+(step*3)]=='e':
                Row_score+=3
    # 3 red after each other (4th empty on the left)
    for i in range(0,Rows):
        for j in range(0,Columns-3):
            if total_string[i+(j*step)]=='e' and total_string[i+(j*step)+(step*1)]=='r' and total_string[i+(j*step)+(step*2)]=='r' and total_string[i+(j*step)+(step*3)]=='r':
                Row_score += 3
    # 1 red then empty then 2 red after each other
    for i in range(0, Rows):
        for j in range(0, Columns - 3):
            if total_string[i+(j*step)]=='r' and total_string[i+(j*step)+(step*1)]=='e' and total_string[i+(j*step)+(step*2)]=='r' and total_string[i+(j*step)+(step*3)]=='r':
                Row_score += 3

    # 2 red after each other then empty then 1 red after each
    for i in range(0, Rows):
        for j in range(0, Columns - 3):
            if total_string[i+(j*step)]=='r' and total_string[i+(j*step)+(step*1)]=='r' and total_string[i+(j*step)+(step*2)]=='e' and total_string[i+(j*step)+(step*3)]=='r':
                Row_score += 3

    # 4 red after each other
    for i in range(0, Rows):
        for j in range(0, Columns - 3):
            if total_string[i+(j*step)]=='r' and total_string[i+(j*step)+(step*1)]=='r' and total_string[i+(j*step)+(step*2)]=='r' and total_string[i+(j*step)+(step*3)]=='r':
                Row_score += 5

    # check 2 able to be 4
    # 2 red after each other (2 empty after each other on the right)
    for i in range(0, Rows):
        for j in range(0, Columns - 3):
            if total_string[i+(j*step)]=='r' and total_string[i+(j*step)+(step*1)]=='r' and total_string[i+(j*step)+(step*2)]=='e' and total_string[i+(j*step)+(step*3)]=='e':
                Row_score += 1

    # 2 red after each other (2 empty after each other on the left)
    for i in range(0, Rows):
        for j in range(0, Columns - 3):
            if total_string[i+(j*step)]=='e' and total_string[i+(j*step)+(step*1)]=='e' and total_string[i+(j*step)+(step*2)]=='r' and total_string[i+(j*step)+(step*3)]=='r':
                Row_score += 1

    # 1 red then 1 empty then 1 red then 1 empty
    for i in range(0, Rows):
        for j in range(0, Columns - 3):
            if total_string[i+(j*step)]=='r' and total_string[i+(j*step)+(step*1)] == 'e' and total_string[i+(j*step)+(step*2)]=='r' and total_string[i+(j*step)+(step*3)]=='e':
                Row_score += 1

    # 1 red then 2 empty  after each  other then 1 red
    for i in range(0, Rows):
            for j in range(0, Columns - 3):
                if total_string[i+(j*step)]=='r' and total_string[i+(j*step)+(step*1)]=='e' and total_string[i+(j*step)+(step*2)]=='e' and total_string[i+(j*step)+(step*3)]=='r':
                    Row_score += 1

    # 1 empty then 2 red  after each  other then 1 empty
    for i in range(0, Rows):
        for j in range(0, Columns - 3):
            if total_string[i+(j*step)]=='e' and total_string[i+(j*step)+(step*1)]=='r' and total_string[i+(j*step)+(step*2)]=='r' and total_string[i+(j*step)+(step*3)]=='e':
                Row_score += 1

    # 1 empty then 1 red then 1 empty then 1 red
    for i in range(0, Rows):
        for j in range(0, Columns - 3):
            if total_string[i+(j*step)]== 'e' and total_string[i+(j*step)+(step *1)]=='r' and total_string[i+(j*step)+(step*2)]=='e' and total_string[i+(j*step)+(step*3)]=='r':
                Row_score += 1

    # blocking opponent from completing 4 yellow
    # 3 yellow after each other (4th red on the right)
    for i in range(0, Rows):
        for j in range(0, Columns - 3):
            if total_string[i+(j*step)]=='y' and total_string[i+(j*step)+(step*1)]=='y' and total_string[i+(j*step)+(step*2)]=='y' and total_string[i+(j*step)+(step*3)]=='r':
                Row_score += 4

    # 3 yellow after each other (4th red on the left)
    for i in range(0, Rows):
        for j in range(0, Columns - 3):
            if total_string[i+(j*step)]=='r' and total_string[i+(j*step)+(step*1)]=='y' and total_string[i+(j*step)+(step*2)]=='y' and total_string[i+(j*step)+(step*3)]=='y':
                Row_score += 4

    # 1 yellow then red then 2 yellow after each other
    for i in range(0, Rows):
        for j in range(0, Columns - 3):
            if total_string[i+(j*step)]=='y' and total_string[i+(j*step)+(step*1)]=='r' and total_string[i+(j*step)+(step*2)]=='y' and total_string[i+(j*step)+(step*3)]=='y':
                Row_score += 4

    # 2 yellow after each other then red then 1 yellow after each
    for i in range(0, Rows):
        for j in range(0, Columns - 3):
            if total_string[i+(j*step)] =='y' and total_string[i+(j*step)+(step*1)]=='y' and total_string[i+(j*step)+(step*2)] == 'r' and total_string[i+(j*step)+(step*3)]=='y':
                Row_score += 4

    return Row_score

def FindMatchingCol(node):
    Column_score=0
    return Column_score


def FindMatchingDiag1(node): #+ve diagonal
    Diag1_score=0
    return Diag1_score

def FindMatchingDiag2(node):  # -ve diagonal
    Diag2_score=0
    return Diag2_score