def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    moves = 0
    while moves < 9:
        print_board(board)
        player = players[moves % 2]
        print(f"Jucatorul {player}, introdu randul si coloana (0, 1 sau 2):")
        try:
            row = int(input("Rand: "))
            col = int(input("Coloana: "))
            if board[row][col] != " ":
                print("Pozitie ocupata! Incearca din nou.")
                continue
        except (ValueError, IndexError):
            print("Pozitie invalida! Incearca din nou.")
            continue
        board[row][col] = player
        if check_winner(board, player):
            print_board(board)
            print(f"Jucatorul {player} a castigat!")
            return
        moves += 1
    print_board(board)
    print("Egalitate!")

tic_tac_toe()