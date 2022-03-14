"""
- storing information about the current state
- determining valid moves at the current state
- keeping a move log
"""

class GameState():
    def __init__(self):
        # board is 8x8 2D list, each element of the list has 2 characters
        # first character represents the color (black, white)
        # second character represents the type of piece
        # "--" represents an empty space with no piece
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.whiteToMove = True
        self.moveLog = []

class Move():
    def __init__(self, start_sq, end_sq, board):
        # to be implemented later
        pass
