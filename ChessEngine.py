# This class going to keep track of the current state of the chess game
# It will determine valid moves at the current state
# It will keep a move log

class GameState():
    def __init__(self):
        # board is an 8x8 2d list, each element has 2 characters.
        # the first character represents the color 'b' or 'w'
        # the second character represents the type: 'K', 'Q', 'B', 'R', 'N', or 'P'
        # '--' represents an empty space
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whiteToMove = True
        self.moveLog = []
        
        
    