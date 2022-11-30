from copy import deepcopy


def apply_operand(a, b, operand):
    if operand == '+':
        return a + b
    if operand == '-':
        return a - b
    raise Exception('Invalid operand')


def update_used(N, i, j, used, increment):
    update = [[False]*N for _ in range(N)]

    # Vertical
    for y in range(N):
        update[y][j] = True

    # Horizontal
    for x in range(N):
        update[i][x] = True

    # Diagonals
    for operand1 in ['-', '+']:
        for operand2 in ['-', '+']:
            y = i
            x = j
            while 0 <= x < N and 0 <= y < N:
                update[y][x] = True
                y = apply_operand(y, 1, operand2)
                x = apply_operand(x, 1, operand1)


    # Update used only once
    for y in range(N):
        for x in range(N):
            if update[y][x]:
                used[y][x] += increment


def helper(N, matrices, matrix, used, i):
    # Solution found
    if i == N:
        matrices.append(deepcopy(matrix))
        return

    # Try adding Q to each cell
    for j in range(N):
        if used[i][j] == 0:
            matrix[i][j] = 'Q'
            update_used(N, i, j, used, 1)
            helper(N, matrices, matrix, used, i + 1)
            update_used(N, i, j, used, -1)
            matrix[i][j] = '.'


def flatten_matrices(matrices):
    flattened = []
    for matrix in matrices:
        rows = []
        for row in matrix:
            flat = ''
            for cell in row:
                flat += cell
            rows.append(flat)
        flattened.append(rows)

    return flattened


def solveNQueens(N):
    matrices = []
    matrix = [['.'] * N for _ in range(N)]
    used = [[0] * N for _ in range(N)]
    helper(N, matrices, matrix, used, 0)
    return flatten_matrices(matrices)


if __name__ == '__main__':
    print(solveNQueens(4))
