import random

class TicTacToe:
    def __init__(self):
        # Initialize the game board and set the starting player
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def reset_board(self):
        """Reset the game board for a new game."""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def is_winner(self, player):
        """Check if a player has won the game."""
        # Check rows for a win
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        # Check columns for a win
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        # Check diagonals for a win
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_tie(self):
        """Check if the game is a tie (no moves left)."""
        return all(self.board[row][col] != ' ' for row in range(3) for col in range(3))

    def make_move(self, row, col, player):
        """Make a move on the board if the cell is empty."""
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False

    def available_moves(self):
        """Get a list of all available moves on the board."""
        return [(row, col) for row in range(3) for col in range(3) if self.board[row][col] == ' ']

    def minimax(self, is_maximizing, alpha=-float('inf'), beta=float('inf')):
        """Use the Minimax algorithm with Alpha-Beta Pruning to calculate the best move."""
        # Check for terminal states
        if self.is_winner('X'):
            return -10
        if self.is_winner('O'):
            return 10
        if self.is_tie():
            return 0

        if is_maximizing:
            max_eval = -float('inf')
            for move in self.available_moves():
                self.board[move[0]][move[1]] = 'O'
                eval = self.minimax(False, alpha, beta)
                self.board[move[0]][move[1]] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Prune remaining branches
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.available_moves():
                self.board[move[0]][move[1]] = 'X'
                eval = self.minimax(True, alpha, beta)
                self.board[move[0]][move[1]] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Prune remaining branches
            return min_eval

    def best_move(self):
        """Determine the best move for the AI using the Minimax algorithm."""
        best_val = -float('inf')
        best_move = None
        for move in self.available_moves():
            self.board[move[0]][move[1]] = 'O'
            move_val = self.minimax(False)
            self.board[move[0]][move[1]] = ' '
            if move_val > best_val:
                best_val = move_val
                best_move = move
        return best_move
