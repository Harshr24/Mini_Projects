'''
from random import choice

# Function to display the Tic-Tac-Toe board with colored and bold 'X's and 'O's
def display_board(board):
    def colored_symbol(symbol):
        if symbol == 'X':
            return "\x1b[1m\x1b[34m" + symbol + "\x1b[0m"  # Bold and dark blue color for X
        elif symbol == 'O':
            return "\x1b[1m\x1b[31m" + symbol + "\x1b[0m"  # Bold and red color for O
        else:
            return symbol

    # Printing the board using nested loops
    print("+-------+-------+-------+")
    for row in range(3):
        print("|       |       |       |")
        # Displaying each cell of the board with colored and bold symbols
        print("|  ", colored_symbol(board[row][0]), "  |  ", colored_symbol(board[row][1]), "  |  ", colored_symbol(board[row][2]), "  |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

# Function to update the board with the player's move
def enter_move(board, move, symbol):
    board[move // 3][move % 3] = symbol

# Function to generate a list of free fields on the board
def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free.append(row * 3 + col + 1)
    return free

# Function to check for victory conditions based on the sign ('X' or 'O')
def victory_for(board, sign):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == sign:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

# Function to initialize the game by getting user preferences (side and first move)
def initialize_game():
    user_side = input("Choose 'X' or 'O': ").upper()
    while user_side not in ['X', 'O']:
        print("Invalid choice. Please choose 'X' or 'O'.")
        user_side = input("Choose 'X' or 'O': ").upper()

    first_turn = input("Do you want to make the first move? (yes/no): ").lower()
    while first_turn not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        first_turn = input("Do you want to make the first move? (yes/no): ").lower()

    return user_side, first_turn == 'yes'

# Main game function that orchestrates the game flow
def main():
    # Initialize game settings
    user_side, user_first = initialize_game()
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    # Determine computer's side based on user's side selection
    if user_side == 'X':
        computer_side = 'O'
    else:
        computer_side = 'X'

    # Display the initial board
    display_board(board)

    # Game loop that runs for a maximum of 9 turns (board size)
    for turn in range(9):
        if (turn % 2 == 0 and user_first) or (turn % 2 != 0 and not user_first):
            # User's turn
            move = int(input("Enter your move (1-9): ")) - 1
            while move < 0 or move > 8 or str(board[move // 3][move % 3]) in ['X', 'O']:
                print("Invalid move. Please choose an empty cell (1-9): ")
                move = int(input("Enter your move (1-9): ")) - 1
            enter_move(board, move, user_side)
        else:
            # Computer's turn
            free_fields = make_list_of_free_fields(board)
            computer_move = choice(free_fields)
            enter_move(board, computer_move - 1, computer_side)
            print("Updated board after computer's move:")  # Statement added here

        # Display the current state of the board
        display_board(board)
        
        # Check for victory or draw conditions
        if turn >= 4:
            if victory_for(board, user_side):
                print("You won!")
                break
            elif victory_for(board, computer_side):
                print("Computer won!")
                break
        if turn == 8:
            print("It's a tie!")
            break

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
'''

import tkinter as tk
from tkinter import messagebox
from random import choice

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.user_side = ''
        self.user_first = False
        self.computer_side = ''
        self.board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.buttons = []
        
        self.initialize_game()
        self.create_board()
    
    def initialize_game(self):
        self.user_side = self.get_user_side()
        print("Make your first move!")

        # No longer asking the user for the first move
        # self.user_first = self.ask_first_move()
        self.user_first = True  # Assuming the user always goes first
        self.computer_side = 'O' if self.user_side == 'X' else 'X'
        
    def get_user_side(self):
        user_side = ''
        while user_side not in ['X', 'O']:
            user_side = input("Choose 'X' or 'O': ").upper()
        return user_side
    
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text=self.board[i][j], font=('Arial', 20), width=5, height=2,
                                   command=lambda i=i, j=j: self.handle_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
    
    def handle_click(self, row, col):
        if self.board[row][col] not in ['X', 'O']:
            self.enter_move(row * 3 + col, self.user_side)
            self.update_board()
            if self.check_winner(self.user_side):
                self.game_over("You won!")
            elif self.is_board_full():
                self.game_over("It's a tie!")
            else:
                self.computer_move()
                self.update_board()
                if self.check_winner(self.computer_side):
                    self.game_over("Computer won!")
                elif self.is_board_full():
                    self.game_over("It's a tie!")
    
    def enter_move(self, move, symbol):
        self.board[move // 3][move % 3] = symbol
        
    def update_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = self.board[i][j]
    
    def computer_move(self):
        free_fields = self.make_list_of_free_fields()
        computer_move = choice(free_fields)
        self.enter_move(computer_move - 1, self.computer_side)
    
    def make_list_of_free_fields(self):
        free = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] not in ['O', 'X']:
                    free.append(row * 3 + col + 1)
        return free
    
    def check_winner(self, sign):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == sign:
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == sign:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == sign:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == sign:
            return True
        return False
    
    def is_board_full(self):
        for row in self.board:
            if any(cell not in ['X', 'O'] for cell in row):
                return False
        return True
    
    def game_over(self, message):
        messagebox.showinfo("Game Over", message)
        self.root.quit()

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()


from random import choice

# Function to display the Tic-Tac-Toe board with colored and bold 'X's and 'O's
def display_board(board):
    def colored_symbol(symbol):
        if symbol == 'X':
            return "\x1b[1m\x1b[34m" + symbol + "\x1b[0m"  # Bold and dark blue color for X
        elif symbol == 'O':
            return "\x1b[1m\x1b[31m" + symbol + "\x1b[0m"  # Bold and red color for O
        else:
            return symbol

    # Printing the board using nested loops
    print("+-------+-------+-------+")
    for row in range(3):
        print("|       |       |       |")
        # Displaying each cell of the board with colored and bold symbols
        print("|  ", colored_symbol(board[row][0]), "  |  ", colored_symbol(board[row][1]), "  |  ", colored_symbol(board[row][2]), "  |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

# Function to update the board with the player's move
def enter_move(board, move, symbol):
    board[move // 3][move % 3] = symbol

# Function to generate a list of free fields on the board
def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free.append(row * 3 + col + 1)
    return free

# Function to check for victory conditions based on the sign ('X' or 'O')
def victory_for(board, sign):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == sign:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

# Function to initialize the game by getting user preferences (side and first move)
def initialize_game():
    user_side = input("Choose 'X' or 'O': ").upper()
    while user_side not in ['X', 'O']:
        print("Invalid choice. Please choose 'X' or 'O'.")
        user_side = input("Choose 'X' or 'O': ").upper()

    first_turn = input("Do you want to make the first move? (yes/no): ").lower()
    while first_turn not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        first_turn = input("Do you want to make the first move? (yes/no): ").lower()

    return user_side, first_turn == 'yes'

# Main game function that orchestrates the game flow
def main():
    # Initialize game settings
    user_side, user_first = initialize_game()
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    # Determine computer's side based on user's side selection
    if user_side == 'X':
        computer_side = 'O'
    else:
        computer_side = 'X'

    # Display the initial board
    display_board(board)

    # Game loop that runs for a maximum of 9 turns (board size)
    for turn in range(9):
        if (turn % 2 == 0 and user_first) or (turn % 2 != 0 and not user_first):
            # User's turn
            move = int(input("Enter your move (1-9): ")) - 1
            while move < 0 or move > 8 or str(board[move // 3][move % 3]) in ['X', 'O']:
                print("Invalid move. Please choose an empty cell (1-9): ")
                move = int(input("Enter your move (1-9): ")) - 1
            enter_move(board, move, user_side)
        else:
            # Computer's turn
            free_fields = make_list_of_free_fields(board)
            computer_move = choice(free_fields)
            enter_move(board, computer_move - 1, computer_side)
            print("Updated board after computer's move:")  # Statement added here

        # Display the current state of the board
        display_board(board)
        
        # Check for victory or draw conditions
        if turn >= 4:
            if victory_for(board, user_side):
                print("You won!")
                break
            elif victory_for(board, computer_side):
                print("Computer won!")
                break
        if turn == 8:
            print("It's a tie!")
            break

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()