# This class going to keep track of the current state of the chess game
# It will determine valid moves at the current state
# It will keep a move log

from string import whitespace
from time import sleep


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
        
    def make_move(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move) #logging the moves 
        self.whiteToMove = not self.whiteToMove #swap players
    
    #Undo the last move
    def undo_move(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove
            
    #All moves considering checks
    def get_valid_moves(self):
        return self.get_all_possible_moves() #not going to worry about checks atm
    
    #All moves without considering checks
    def get_all_possible_moves(self):
        moves = []
        for r in range(len(self.board)): #number of rows
            for c in range(len(self.board[r])): #number of cols in a given row
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteToMove) and (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece == 'P':
                        self.get_pawn_moves(r, c, moves)
                    elif piece == 'R':
                        self.get_rook_moves(r, c, moves)
        return moves
    
    
    #get all pawn moves 
    def get_pawn_moves(self, r, c, moves):
        pass
    
    #get all rook moves
    def get_rook_moves(self, r, c, moves):
        pass                
            
    
        
#Takes a Move as a parameter and executes it(this will not work for castling, en-passant, and pawn promotion)        
class Move():
    # maps keys to values
    # key : value
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v:k for k, v in filesToCols.items()}
    
    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol
        print(self.moveID)
        
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False
        
    def get_chess_notation(self):
        return self.get_rank_file(self.startRow, self.startCol) + self.get_rank_file(self.endRow, self.endCol)
    
    def get_rank_file(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
    