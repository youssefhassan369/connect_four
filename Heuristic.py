Rows = 6
Columns = 7


def Heuristic(node, x, y):
    total_string = node.col0 + node.col1 + node.col2 + node.col3 + node.col4 + node.col5 + node.col6
    return FindMatchingRow(total_string, x, y) + FindMatchingCol(total_string, x, y) + FindMatchingDiag1(total_string,
                                                                                                         x,
                                                                                                         y) + FindMatchingDiag2(
        total_string, x, y)  # weights will be added


def FindMatchingRow(total_string, x, y):
    Row_score = 0
    step = 6

    for i in range(0, Rows):
        for j in range(0, Columns - 3):

            # check 3 able to be 4
            # 3 red after each other (4th empty on the right)
            if total_string[i + (j * step)] == x and total_string[i + (j * step) + (step * 1)] == x and total_string[
                i + (j * step) + (step * 2)] == x and total_string[i + (j * step) + (step * 3)] == 'e':
                Row_score += 3

            # 3 red after each other (4th empty on the left)
            if total_string[i + (j * step)] == 'e' and total_string[i + (j * step) + (step * 1)] == x and total_string[
                i + (j * step) + (step * 2)] == x and total_string[i + (j * step) + (step * 3)] == x:
                Row_score += 3

            # 1 red then empty then 2 red after each other
            if total_string[i + (j * step)] == x and total_string[i + (j * step) + (step * 1)] == 'e' and total_string[
                i + (j * step) + (step * 2)] == x and total_string[i + (j * step) + (step * 3)] == x:
                Row_score += 3

            # 2 red after each other then empty then 1 red after each
            if total_string[i + (j * step)] == x and total_string[i + (j * step) + (step * 1)] == x and total_string[
                i + (j * step) + (step * 2)] == 'e' and total_string[i + (j * step) + (step * 3)] == x:
                Row_score += 3

            # 4 red after each other
            if total_string[i + (j * step)] == x and total_string[i + (j * step) + (step * 1)] == x and total_string[
                i + (j * step) + (step * 2)] == x and total_string[i + (j * step) + (step * 3)] == x:
                Row_score += 60

            # check 2 able to be 4
            # 2 red after each other (2 empty after each other on the right)
            if total_string[i + (j * step)] == x and total_string[i + (j * step) + (step * 1)] == x and total_string[
                i + (j * step) + (step * 2)] == 'e' and total_string[i + (j * step) + (step * 3)] == 'e':
                Row_score += 1

            # 2 red after each other (2 empty after each other on the left)
            if total_string[i + (j * step)] == 'e' and total_string[i + (j * step) + (step * 1)] == 'e' and \
                    total_string[i + (j * step) + (step * 2)] == x and total_string[i + (j * step) + (step * 3)] == x:
                Row_score += 1

            # 1 red then 1 empty then 1 red then 1 empty
            if total_string[i + (j * step)] == x and total_string[i + (j * step) + (step * 1)] == 'e' and total_string[
                i + (j * step) + (step * 2)] == x and total_string[i + (j * step) + (step * 3)] == 'e':
                Row_score += 1

            # 1 red then 2 empty  after each  other then 1 red
            if total_string[i + (j * step)] == x and total_string[i + (j * step) + (step * 1)] == 'e' and total_string[
                i + (j * step) + (step * 2)] == 'e' and total_string[i + (j * step) + (step * 3)] == x:
                Row_score += 1

            # 1 empty then 2 red  after each  other then 1 empty
            if total_string[i + (j * step)] == 'e' and total_string[i + (j * step) + (step * 1)] == x and total_string[
                i + (j * step) + (step * 2)] == x and total_string[i + (j * step) + (step * 3)] == 'e':
                Row_score += 1

            # 1 empty then 1 red then 1 empty then 1 red
            if total_string[i + (j * step)] == 'e' and total_string[i + (j * step) + (step * 1)] == x and total_string[
                i + (j * step) + (step * 2)] == 'e' and total_string[i + (j * step) + (step * 3)] == x:
                Row_score += 1

            # blocking opponent from completing 4 yellow
            # 3 yellow after each other (4th red on the right)
            if total_string[i + (j * step)] == y and total_string[i + (j * step) + (step * 1)] == y and total_string[
                i + (j * step) + (step * 2)] == y and total_string[i + (j * step) + (step * 3)] == x:
                Row_score += 50

            # 3 yellow after each other (4th red on the left)
            if total_string[i + (j * step)] == x and total_string[i + (j * step) + (step * 1)] == y and total_string[
                i + (j * step) + (step * 2)] == y and total_string[i + (j * step) + (step * 3)] == y:
                Row_score += 50

            # 1 yellow then red then 2 yellow after each other
            if total_string[i + (j * step)] == y and total_string[i + (j * step) + (step * 1)] == x and total_string[
                i + (j * step) + (step * 2)] == y and total_string[i + (j * step) + (step * 3)] == y:
                Row_score += 50

            # 2 yellow after each other then red then 1 yellow after each
            if total_string[i + (j * step)] == y and total_string[i + (j * step) + (step * 1)] == y and total_string[
                i + (j * step) + (step * 2)] == x and total_string[i + (j * step) + (step * 3)] == y:
                Row_score += 50

    return Row_score


def FindMatchingCol(total_string, x, y):
    Column_score = 0
    step = 6
    for i in range(0, Columns):
        for j in range(0, Rows - 3):

            # check 3 able to be 4
            # 3 red after each other (4th empty on the right)
            if total_string[i * step + j] == x and total_string[i * step + j + 1] == x and total_string[
                i * step + j + 2] == x and total_string[i * step + j + 3] == 'e':
                Column_score += 3

            # 3 red after each other (4th empty on the left)
            if total_string[i * step + j] == 'e' and total_string[i * step + j + 1] == x and total_string[
                i * step + j + 2] == x and total_string[i * step + j + 3] == x:
                Column_score += 3

            # 1 red then empty then 2 red after each other
            if total_string[i * step + j] == x and total_string[i * step + j + 1] == 'e' and total_string[
                i * step + j + 2] == x and total_string[i * step + j + 3] == x:
                Column_score += 3

            # 2 red after each other then empty then 1 red after each
            if total_string[i * step + j] == x and total_string[i * step + j + 1] == x and total_string[
                i * step + j + 2] == 'e' and total_string[i * step + j + 3] == x:
                Column_score += 3

            # 4 red after each other
            if total_string[i * step + j] == x and total_string[i * step + j + 1] == x and total_string[
                i * step + j + 2] == x and total_string[i * step + j + 3] == x:
                Column_score += 60

            # check 2 able to be 4
            # 2 red after each other (2 empty after each other on the right)
            if total_string[i * step + j] == x and total_string[i * step + j + 1] == x and total_string[
                i * step + j + 2] == 'e' and total_string[i * step + j + 3] == 'e':
                Column_score += 1

            # 2 red after each other (2 empty after each other on the left)
            if total_string[i * step + j] == 'e' and total_string[i * step + j + 1] == 'e' and total_string[
                i * step + j + 2] == x and total_string[i * step + j + 3] == x:
                Column_score += 1

            # 1 red then 1 empty then 1 red then 1 empty
            if total_string[i * step + j] == x and total_string[i * step + j + 1] == 'e' and total_string[
                i * step + j + 2] == x and total_string[i * step + j + 3] == 'e':
                Column_score += 1

            # 1 red then 2 empty  after each  other then 1 red
            if total_string[i * step + j] == x and total_string[i * step + j + 1] == 'e' and total_string[
                i * step + j + 2] == 'e' and total_string[i * step + j + 3] == x:
                Column_score += 1

            # 1 empty then 2 red  after each  other then 1 empty
            if total_string[i * step + j] == 'e' and total_string[i * step + j + 1] == x and total_string[
                i * step + j + 2] == x and total_string[i * step + j + 3] == 'e':
                Column_score += 1

            # 1 empty then 1 red then 1 empty then 1 red
            if total_string[i * step + j] == 'e' and total_string[i * step + j + 1] == x and total_string[
                i * step + j + 2] == 'e' and total_string[i * step + j + 3] == x:
                Column_score += 1

            # blocking opponent from completing 4 yellow
            # 3 yellow after each other (4th red on the right)
            if total_string[i * step + j] == y and total_string[i * step + j + 1] == y and total_string[
                i * step + j + 2] == y and total_string[i * step + j + 3] == x:
                Column_score += 50  # edited was 4

            # 3 yellow after each other (4th red on the left)
            if total_string[i * step + j] == x and total_string[i * step + j + 1] == y and total_string[
                i * step + j + 2] == y and total_string[i * step + j + 3] == y:
                Column_score += 50  # edited was 4

            # 1 yellow then red then 2 yellow after each other
            if total_string[i * step + j] == y and total_string[i * step + j + 1] == x and total_string[
                i * step + j + 2] == y and total_string[i * step + j + 3] == y:
                Column_score += 50

            # 2 yellow after each other then red then 1 yellow after each
            if total_string[i * step + j] == y and total_string[i * step + j + 1] == y and total_string[
                i * step + j + 2] == x and total_string[i * step + j + 3] == y:
                Column_score += 50

    return Column_score


def FindMatchingDiag1(total_string, x, y):  # +ve diagonal
    Diag1_score = 0
    step = 6
    for i in range(0, Rows - 3):
        for j in range(0, Columns - 3):

            # check 3 able to be 4
            # 3 red after each other (4th empty on the right)
            if total_string[i + (j * step)] == x and total_string[i + (j * step) + (step * 1) + 1] == x and \
                    total_string[i + (j * step) + (step * 2) + 2] == x and total_string[
                i + (j * step) + (step * 3) + 3] == 'e':
                Diag1_score += 3

            # 3 red after each other (4th empty on the left)
            if total_string[i + (j * step)] == 'e' and total_string[i + (j * step) + (step * 1) + 1] == x and \
                    total_string[i + (j * step) + (step * 2) + 2] == x and total_string[
                i + (j * step) + (step * 3) + 3] == x:
                Diag1_score += 3

            # 1 red then empty then 2 red after each other
            if total_string[i + (j * step)] == x and total_string[i + (j * step) + (step * 1) + 1] == 'e' and \
                    total_string[i + (j * step) + (step * 2) + 2] == x and total_string[
                i + (j * step) + (step * 3) + 3] == x:
                Diag1_score += 3

            # 2 red after each other then empty then 1 red after each
            if total_string[i + (j * step)] == x and total_string[i + (j * step) + (step * 1) + 1] == x and \
                    total_string[i + (j * step) + (step * 2) + 2] == 'e' and total_string[
                i + (j * step) + (step * 3) + 3] == x:
                Diag1_score += 3

            # 4 red after each other
            if total_string[i + (j * step)] == x and total_string[i + (j * step) + (step * 1) + 1] == x and \
                    total_string[i + (j * step) + (step * 2) + 2] == x and total_string[
                i + (j * step) + (step * 3) + 3] == x:
                Diag1_score += 60

            # check 2 able to be 4
            # 2 red after each other (2 empty after each other on the right)
            if total_string[i + (j * step)] == x and total_string[i + (j * step) + (step * 1) + 1] == x and \
                    total_string[i + (j * step) + (step * 2) + 2] == 'e' and total_string[
                i + (j * step) + (step * 3) + 3] == 'e':
                Diag1_score += 1

            # 2 red after each other (2 empty after each other on the left)
            if total_string[i + (j * step)] == 'e' and total_string[i + (j * step) + (step * 1) + 1] == 'e' and \
                    total_string[i + (j * step) + (step * 2) + 2] == x and total_string[
                i + (j * step) + (step * 3) + 3] == x:
                Diag1_score += 1

            # 1 red then 1 empty then 1 red then 1 empty
            if total_string[i + (j * step)] == x and total_string[i + (j * step) + (step * 1) + 1] == 'e' and \
                    total_string[i + (j * step) + (step * 2) + 2] == x and total_string[
                i + (j * step) + (step * 3) + 3] == 'e':
                Diag1_score += 1

            # 1 red then 2 empty  after each  other then 1 red
            if total_string[i + (j * step)] == x and total_string[i + (j * step) + (step * 1) + 1] == 'e' and \
                    total_string[i + (j * step) + (step * 2) + 2] == 'e' and total_string[
                i + (j * step) + (step * 3) + 3] == x:
                Diag1_score += 1

            # 1 empty then 2 red  after each  other then 1 empty
            if total_string[i + (j * step)] == 'e' and total_string[i + (j * step) + (step * 1) + 1] == x and \
                    total_string[i + (j * step) + (step * 2) + 2] == x and total_string[
                i + (j * step) + (step * 3) + 3] == 'e':
                Diag1_score += 1

            # 1 empty then 1 red then 1 empty then 1 red
            if total_string[i + (j * step)] == 'e' and total_string[i + (j * step) + (step * 1) + 1] == x and \
                    total_string[i + (j * step) + (step * 2) + 2] == 'e' and total_string[
                i + (j * step) + (step * 3) + 3] == x:
                Diag1_score += 1

            # blocking opponent from completing 4 yellow
            # 3 yellow after each other (4th red on the right)
            if total_string[i + (j * step)] == y and total_string[i + (j * step) + (step * 1) + 1] == y and \
                    total_string[i + (j * step) + (step * 2) + 2] == y and total_string[
                i + (j * step) + (step * 3) + 3] == x:
                Diag1_score += 50

            # 3 yellow after each other (4th red on the left)
            if total_string[i + (j * step)] == x and total_string[i + (j * step) + (step * 1) + 1] == y and \
                    total_string[i + (j * step) + (step * 2) + 2] == y and total_string[
                i + (j * step) + (step * 3) + 3] == y:
                Diag1_score += 50

            # 1 yellow then red then 2 yellow after each other
            if total_string[i + (j * step)] == y and total_string[i + (j * step) + (step * 1) + 1] == x and \
                    total_string[i + (j * step) + (step * 2) + 2] == y and total_string[
                i + (j * step) + (step * 3) + 3] == y:
                Diag1_score += 50

            # 2 yellow after each other then red then 1 yellow after each
            if total_string[i + (j * step)] == y and total_string[i + (j * step) + (step * 1) + 1] == y and \
                    total_string[i + (j * step) + (step * 2) + 2] == x and total_string[
                i + (j * step) + (step * 3) + 3] == y:
                Diag1_score += 50

    return Diag1_score


def FindMatchingDiag2(total_string, x, y):  # -ve diagonal
    Diag2_score = 0
    step = 6
    for j in range(0, Rows - 2):
        for i in range(3, Columns - 1):
            # check 3 able to be 4
            # 3 red after each other (4th empty on the right)
            if total_string[i + (j * step) + (step * 3) - 3] == x and total_string[
                i + (j * step) + (step * 2) - 2] == x and total_string[i + (j * step) + (step * 1) - 1] == x and \
                    total_string[i + (j * step)] == 'e':
                Diag2_score += 3

            # 3 red after each other (4th empty on the left)
            if total_string[i + (j * step) + (step * 3) - 3] == 'e' and total_string[
                i + (j * step) + (step * 2) - 2] == x and total_string[i + (j * step) + (step * 1) - 1] == x and \
                    total_string[i + (j * step)] == x:
                Diag2_score += 3

            # 1 red then empty then 2 red after each other
            if total_string[i + (j * step) + (step * 3) - 3] == x and total_string[
                i + (j * step) + (step * 2) - 2] == 'e' and total_string[i + (j * step) + (step * 1) - 1] == x and \
                    total_string[i + (j * step)] == x:
                Diag2_score += 3

            # 2 red after each other then empty then 1 red after each
            if total_string[i + (j * step) + (step * 3) - 3] == x and total_string[
                i + (j * step) + (step * 2) - 2] == x and total_string[i + (j * step) + (step * 1) - 1] == 'e' and \
                    total_string[i + (j * step)] == x:
                Diag2_score += 3

            # 4 red after each other
            if total_string[i + (j * step) + (step * 3) - 3] == x and total_string[
                i + (j * step) + (step * 2) - 2] == x and total_string[i + (j * step) + (step * 1) - 1] == x and \
                    total_string[i + (j * step)] == x:
                Diag2_score += 60

            # check 2 able to be 4
            # 2 red after each other (2 empty after each other on the right)
            if total_string[i + (j * step) + (step * 3) - 3] == x and total_string[
                i + (j * step) + (step * 2) - 2] == x and total_string[i + (j * step) + (step * 1) - 1] == 'e' and \
                    total_string[i + (j * step)] == 'e':
                Diag2_score += 1

            # 2 red after each other (2 empty after each other on the left)
            if total_string[i + (j * step) + (step * 3) - 3] == 'e' and total_string[
                i + (j * step) + (step * 2) - 2] == 'e' and total_string[i + (j * step) + (step * 1) - 1] == x and \
                    total_string[i + (j * step)] == x:
                Diag2_score += 1

            # 1 red then 1 empty then 1 red then 1 empty
            if total_string[i + (j * step) + (step * 3) - 3] == x and total_string[
                i + (j * step) + (step * 2) - 2] == 'e' and total_string[i + (j * step) + (step * 1) - 1] == x and \
                    total_string[i + (j * step)] == 'e':
                Diag2_score += 1

            # 1 red then 2 empty  after each  other then 1 red
            if total_string[i + (j * step) + (step * 3) - 3] == x and total_string[
                i + (j * step) + (step * 2) - 2] == 'e' and total_string[i + (j * step) + (step * 1) - 1] == 'e' and \
                    total_string[i + (j * step)] == x:
                Diag2_score += 1

            # 1 empty then 2 red  after each  other then 1 empty
            if total_string[i + (j * step) + (step * 3) - 3] == 'e' and total_string[
                i + (j * step) + (step * 2) - 2] == x and total_string[i + (j * step) + (step * 1) - 1] == x and \
                    total_string[i + (j * step)] == 'e':
                Diag2_score += 1

            # 1 empty then 1 red then 1 empty then 1 red
            if total_string[i + (j * step) + (step * 3) - 3] == 'e' and total_string[
                i + (j * step) + (step * 2) - 2] == x and total_string[i + (j * step) + (step * 1) - 1] == 'e' and \
                    total_string[i + (j * step)] == x:
                Diag2_score += 1

            # blocking opponent from completing 4 yellow
            # 3 yellow after each other (4th red on the right)
            if total_string[i + (j * step) + (step * 3) - 3] == y and total_string[
                i + (j * step) + (step * 2) - 2] == y and total_string[i + (j * step) + (step * 1) - 1] == y and \
                    total_string[i + (j * step)] == x:
                Diag2_score += 50

            # 3 yellow after each other (4th red on the left)
            if total_string[i + (j * step) + (step * 3) - 3] == x and total_string[
                i + (j * step) + (step * 2) - 2] == y and total_string[i + (j * step) + (step * 1) - 1] == y and \
                    total_string[i + (j * step)] == y:
                Diag2_score += 50

            # 1 yellow then red then 2 yellow after each other
            if total_string[i + (j * step) + (step * 3) - 3] == y and total_string[
                i + (j * step) + (step * 2) - 2] == x and total_string[i + (j * step) + (step * 1) - 1] == y and \
                    total_string[i + (j * step)] == y:
                Diag2_score += 50

            # 2 yellow after each other then red then 1 yellow after each
            if total_string[i + (j * step) + (step * 3) - 3] == y and total_string[
                i + (j * step) + (step * 2) - 2] == y and total_string[i + (j * step) + (step * 1) - 1] == x and \
                    total_string[i + (j * step)] == y:
                Diag2_score += 50

    return Diag2_score
