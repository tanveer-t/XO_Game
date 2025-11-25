import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
        (0, 4, 8), (2, 4, 6)             
    ]

    for a, b, c in win_conditions:
        if board[a] == player and board[b] == player and board[c] == player:
            return True
    return False

def is_board_full(board):
    return " " not in board

def get_player_move(board, player):

    while True:
        try:
            move = input(f"Player {player}, enter your move (1-9): ")
            
            if not move.isdigit():
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            move_index = int(move) - 1

            if move_index < 0 or move_index > 8:
                print("Number out of range. Please enter 1-9.")
                continue

            if board[move_index] != " ":
                print("That spot is already taken! Try again.")
                continue

            return move_index

        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 is X and Player 2 is O")
    
    while True:

        board = [" " for _ in range(9)]
        current_player = "X"
        game_over = False

        while not game_over:
            clear_screen()
            print(f"Current Turn: Player {current_player}")
            print_board(board)

            move_index = get_player_move(board, current_player)
            
            board[move_index] = current_player

            if check_winner(board, current_player):
                clear_screen()
                print_board(board)
                print(f"Congratulations! Player {current_player} wins!")
                game_over = True
            
            elif is_board_full(board):
                clear_screen()
                print_board(board)
                print("It's a draw! No one wins.")
                game_over = True
            
            else:
                current_player = "O" if current_player == "X" else "X"

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()