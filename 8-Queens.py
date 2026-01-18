N = 8
board = [-1] * N

def safe(row, col):
    for i in range(row):
        # same column
        if board[i] == col:
            return False
        # diagonal check
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def queens(row):
    if row == N:
        return True

    for col in range(N):
        if safe(row, col):
            board[row] = col
            if queens(row + 1):
                return True
            board[row] = -1   # backtrack

    return False


def print_board():
    for i in range(N):
        for j in range(N):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


queens(0)
print_board()
