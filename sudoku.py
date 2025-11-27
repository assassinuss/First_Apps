import random

def print_board(board):
    for i in range(9):
        row = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row += "| "
            row += str(board[i][j]) if board[i][j] != 0 else "."
            row += " "
        print(row)
        if (i + 1) % 3 == 0 and i != 8:
            print("-" * 21)

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def valid(board, num, pos):
    row, col = pos
    for i in range(9):
        if board[row][i] == num and i != col:
            return False
    for i in range(9):
        if board[i][col] == num and i != row:
            return False
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    row, col = find
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

def generate_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        num = random.randint(1, 9)
        while not valid(board, num, (i, i)):
            num = random.randint(1, 9)
        board[i][i] = num
    solve(board)
    for _ in range(40):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        board[x][y] = 0
    return board

def main():
    board = generate_board()
    while True:
        print_board(board)
        guess = input("Enter row col num (e.g. 1 2 3), or 'q' to quit: ")
        if guess.lower() == 'q':
            print("Goodbye!")
            break
        try:
            row, col, num = map(int, guess.strip().split())
            if board[row][col] == 0 and valid(board, num, (row, col)):
                board[row][col] = num
            else:
                print("Invalid move.")
        except Exception:
            print("Invalid input.")
        if not find_empty(board):
            print_board(board)
            print("Congratulations, you solved the puzzle!")
            break


main()
