# Tic-Tac-Toe AI using Minimax Algorithm

# Display the board
def display_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


# Check whether a player has won
def check_winner(board, player):

    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


# Check whether board is full
def is_full(board):
    return " " not in board


# Minimax algorithm
def minimax(board, maximizing):

    # AI wins
    if check_winner(board, "O"):
        return 1

    # Human wins
    if check_winner(board, "X"):
        return -1

    # Draw
    if is_full(board):
        return 0

    # AI's turn
    if maximizing:

        best_score = -1000

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(board, False)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    # Human's turn
    else:

        best_score = 1000

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(board, True)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score


# Find the best move for AI
def best_move(board):

    best_score = -1000
    move = None

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(board, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


# Main game
board = [" "] * 9

print("===================================")
print("       TIC-TAC-TOE AI GAME")
print("       Using Minimax Algorithm")
print("===================================")

print("\nPositions:")
print(" 1 | 2 | 3")
print("---+---+---")
print(" 4 | 5 | 6")
print("---+---+---")
print(" 7 | 8 | 9")

print("\nYou are X")
print("AI is O")

while True:

    display_board(board)

    # Human move
    while True:

        try:
            position = int(input("Enter your position (1-9): "))

            position = position - 1

            if position < 0 or position > 8:
                print("Please enter a number between 1 and 9.")

            elif board[position] != " ":
                print("Position already occupied. Choose another.")

            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    board[position] = "X"

    # Check human win
    if check_winner(board, "X"):

        display_board(board)

        print("🎉 You Win!")
        break

    # Check draw
    if is_full(board):

        display_board(board)

        print("🤝 Game Draw!")
        break

    # AI move
    print("AI is thinking...")

    ai_position = best_move(board)

    board[ai_position] = "O"

    print("AI selected position:", ai_position + 1)

    # Check AI win
    if check_winner(board, "O"):

        display_board(board)

        print("🤖 AI Wins!")
        break

    # Check draw
    if is_full(board):

        display_board(board)

        print("🤝 Game Draw!")
        break