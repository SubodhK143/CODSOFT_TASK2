import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


# Function to initialize a 3x3 empty board
def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Function to check if a player has won
def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

# Function to check if a move is valid
def is_valid_move(board, row, col):
    return board[row][col] == " "

# Minimax algorithm function
def minimax(board, depth, maximizing_player):
    if is_winner(board, "X"):
        return 1
    if is_winner(board, "O"):
        return -1
    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to get the AI's optimal move using Minimax
def get_ai_move(board):
    best_move = None
    best_eval = -math.inf

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                eval = minimax(board, 0, False)
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)

    return best_move

# Main game loop
def play_game():
    board = initialize_board()
    current_player = "X"

    while True:
        print_board(board)

        if current_player == "X":  # AI's turn
            print("AI's turn (X):")
            row, col = get_ai_move(board)
        else:  # Human player's turn
            print("Your turn (O):")
            while True:
                try:
                    row = int(input("Enter row (0, 1, 2): "))
                    col = int(input("Enter column (0, 1, 2): "))
                    if is_valid_move(board, row, col):
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        if is_valid_move(board, row, col):
            board[row][col] = current_player
            if is_winner(board, current_player):
                print_board(board)
                print(f"{current_player} wins!")
                break
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_game()
