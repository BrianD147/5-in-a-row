import numpy as np

EMPTY_SLOT = '[ ]'

class Logic(object):

    board = [[EMPTY_SLOT for col in range(9)] for row in range(6)]   # Global array of game board
    pieceLevels = np.array([5, 5, 5, 5, 5, 5, 5, 5, 5])
    
    def displayBoard(self):
        boardPrint = '\n========GAME BOARD=========\n'
        for i in range(len(self.board)):
            boardPrint += ''.join(self.board[i])
            boardPrint += '\n'
        return boardPrint

    def placePiece(self, pos):
        self.board[self.pieceLevels[pos]][pos-1] = '[\u25CF]'
        self.pieceLevels[pos] -= 1