import math

# Tic-Tac-Toe board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Function to print the board
def print_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check if there are empty cells
def is_moves_left():
    for row in board:
        for cell in row:
            if cell == " ":
                return True
    return False

# Check for a winner
def evaluate():
    # Check rows, columns, and diagonals
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != " ":
            return 10 if board[row][0] == "O" else -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return 10 if board[0][col] == "O" else -10

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return 10 if board[0][0] == "O" else -10

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return 10 if board[0][2] == "O" else -10

    return 0  # No winner yet

# Minimax function
def minimax(depth, is_max):
    score = evaluate()

    if score == 10:
        return score - depth  # AI wins
    if score == -10:
        return score + depth  # Human wins
    if not is_moves_left():
        return 0  # Draw

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = max(best, minimax(depth + 1, False))
                    board[i][j] = " "
        return best

    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = min(best, minimax(depth + 1, True))
                    board[i][j] = " "
        return best

# Find the best move for AI
def find_best_move():
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Main game loop
def play_game():
    print("Tic-Tac-Toe (You: X, AI: O)")
    print_board()

    while True:
        # Human's turn
        while True:
            try:
                row, col = map(int, input("Enter row and column (0-2, space separated): ").split())
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell is occupied! Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Enter numbers between 0 and 2.")

        print_board()

        if evaluate() == -10:
            print("You win!")
            break
        if not is_moves_left():
            print("It's a draw!")
            break

        # AI's turn
        print("AI is thinking...")
        ai_move = find_best_move()
        board[ai_move[0]][ai_move[1]] = "O"
        print_board()

        if evaluate() == 10:
            print("AI wins!")
            break
        if not is_moves_left():
            print("It's a draw!")
            break

# Run the game
if _name_ == "_main_":
    play_game()
