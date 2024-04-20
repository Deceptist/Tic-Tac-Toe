# A tic-tac-toe engine supported by the game
class Board:
    
    def __init__(self, turn: int = 1):
        self.turn = turn
        self.board = [
            None, None, None,
            None, None, None,
            None, None, None
        ]
    

    def move(self, square: int) -> int:
        # Create a move on the board according to the turn
        square -= 1
        if square < 0 or square > 8:
            return 1 # Code 1 for invalid square index error
        
        elif self.board[square] is not None:
            return 2 # Code 2 for square already filled error
        
        else:
            self.board[square] = self.turn
            self.turn = (0 if self.turn == 1 else 1)
            return 0 # Code 0 for successful execution
    

    def check_win(self) -> int:
        win_patterns = [
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
            [0, 4, 8], [2, 4, 6] # Diagonal
        ]

        for pattern in win_patterns:
            # If X won
            if self.board[pattern[0]] == 1 and self.board[pattern[1]] == 1 and self.board[pattern[2]] == 1:
                return 1 # Code 1 for X winning
            
            # If O won
            elif self.board[pattern[0]] == 0 and self.board[pattern[1]] == 0 and self.board[pattern[2]] == 0:
                return 0 # Code 0 for O winning
            
            else: pass
        
        # Checking if its a tie
        if None not in self.board:
            return 2 # Code 2 for tie
        

    def reset(self, turn: int = 1):
        self.turn = turn
        self.board = [
            None, None, None,
            None, None, None,
            None, None, None
        ]
