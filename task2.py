import math

# 3x3 Tic-Tac-Toe board 
board = [' ' for _ in range(9)]  

# Printing the game board
def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

# winner or draw check
def CheckWinner(b, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(b[i] == player for i in condition):
            return True
    return False

def is_draw(b):
    return ' ' not in b

# Minimax algorithm
def minimax(b, depth, is_maximizing):
    if CheckWinner(b, 'O'):
        return 1
    if CheckWinner(b, 'X'):
        return -1
    if is_draw(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score

# AI move
def ai():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

# your move
def you():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("That spot is already taken.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number from 1 to 9.")

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X'. AI is 'O'.")
    print_board()

    while True:
        you()
        print_board()
        if CheckWinner(board, 'X'):
            print("Congratulations! You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        print("AI is making a move...")
        ai()
        print_board()
        if CheckWinner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        if is_draw(board):
            print("It's a draw!")
            break

# Run the game
play_game()
