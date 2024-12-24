import tkinter as tk
from tkinter import messagebox
from tictactoe import TicTacToe # type: ignore

class TicTacToeGUI:
    def __init__(self):
        # Initialize the game logic and GUI
        self.game = TicTacToe()
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        """Create the main game interface."""
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        # Display current player's turn
        self.status_label = tk.Label(self.root, text="Player X's Turn", font=('Arial', 14))
        self.status_label.pack()

        # Button for restarting the game
        self.restart_button = tk.Button(self.root, text="Restart", command=self.reset_game, font=('Arial', 12))
        self.restart_button.pack(side=tk.LEFT, padx=20)

        # Button for quitting the game
        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit_game, font=('Arial', 12))
        self.quit_button.pack(side=tk.RIGHT, padx=20)

        # Create buttons for the game grid
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.frame, text=" ", font=('Arial', 20), width=5, height=2,
                    command=lambda r=row, c=col: self.handle_click(r, c)
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def handle_click(self, row, col):
        """Handle a button click by the player or AI."""
        if self.game.make_move(row, col, self.game.current_player):
            self.buttons[row][col].config(text=self.game.current_player)
            if self.game.is_winner(self.game.current_player):
                self.game_over(f"Player {self.game.current_player} Wins!")
            elif self.game.is_tie():
                self.game_over("It's a Tie!")
            else:
                self.switch_turn()
                if self.game.current_player == 'O':  # AI's turn
                    self.ai_move()

    def ai_move(self):
        """Make a move for the AI."""
        move = self.game.best_move()
        if move:
            self.handle_click(move[0], move[1])

    def switch_turn(self):
        """Switch to the next player's turn."""
        self.game.current_player = 'O' if self.game.current_player == 'X' else 'X'
        self.status_label.config(text=f"Player {self.game.current_player}'s Turn")

    def game_over(self, message):
        """Handle the end of the game."""
        messagebox.showinfo("Game Over", message)
        self.reset_game()

    def reset_game(self):
        """Reset the game to its initial state."""
        self.game.reset_board()
        self.game.current_player = 'X'
        self.status_label.config(text="Player X's Turn")
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ")

    def quit_game(self):
        """Handle the Quit button with an option to leave or continue."""
        # Prompt the user with a choice to quit or continue
        response = messagebox.askquestion(
            "Quit Game", "Are you sure you want to quit?",
            icon="warning", type=messagebox.YESNO
        )
        if response == 'yes':  # If user chooses "Leave"
            self.root.destroy()  # Quit the application
        # If user chooses "No", the game continues without interruption

def main():
    """Run the main game loop."""
    app = TicTacToeGUI()
    app.root.mainloop()

if __name__ == "__main__":
    main()
