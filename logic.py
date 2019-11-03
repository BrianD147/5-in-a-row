import numpy as np

EMPTY_SLOT = '[ ]'

class Logic(object):

    board = [[EMPTY_SLOT for col in range(9)] for row in range(6)]   # Global array of game board
    pieceLevels = [5, 5, 5, 5, 5, 5, 5, 5, 5]
    
    def displayBoard(self):
        boardPrint = '\n========GAME BOARD=========\n'
        for i in range(len(self.board)):
            boardPrint += ''.join(self.board[i])
            boardPrint += '\n'
        return boardPrint

    def placePiece(self, counter, pos):
        pos -= 1
        if(counter == 0):
            currentPiece = '[\u25CF]'
        else:
            currentPiece = '[o]'
        self.board[self.pieceLevels[pos]][pos] = currentPiece
        self.pieceLevels[pos] -= 1

        hasWon = self.checkForWin(currentPiece)
        return hasWon

    def checkForWin(self, currentPiece):
        hasWon = self.checkHorizontal(currentPiece)
        return hasWon

    def checkHorizontal(self, currentPiece):
        for c in range(5):
            for r in range(6):
                if self.board[r][c] == currentPiece and self.board[r][c+1] == currentPiece and self.board[r][c+2] == currentPiece and self.board[r][c+3] == currentPiece and self.board[r][c+4] == currentPiece:
                    return True