EMPTY_SLOT = '[ ]'
ROWS = 6
COLS = 9

class Logic(object):

    board = [[EMPTY_SLOT for col in range(COLS)] for row in range(ROWS)]   # Global array of game board
    pieceLevels = [5, 5, 5, 5, 5, 5, 5, 5, 5]
    
    def displayBoard(self):
        boardPrint = '\n========GAME BOARD=========\n[1][2][3][4][5][6][7][8][9]\n\n'
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
        if self.checkHorizontal(currentPiece): return True
        if self.checkVertical(currentPiece): return True
        if self.checkDiagonalPositive(currentPiece): return True
        if self.checkDiagonalNegative(currentPiece): return True
        return False

    def checkHorizontal(self, currentPiece):
        for c in range(COLS-4):
            for r in range(ROWS):
                if self.board[r][c] == currentPiece and self.board[r][c+1] == currentPiece and self.board[r][c+2] == currentPiece and self.board[r][c+3] == currentPiece and self.board[r][c+4] == currentPiece:
                    return True

    def checkVertical(self, currentPiece):
        for c in range(COLS):
            for r in range(ROWS-4):
                if self.board[r][c] == currentPiece and self.board[r+1][c] == currentPiece and self.board[r+2][c] == currentPiece and self.board[r+3][c] == currentPiece and self.board[r+4][c] == currentPiece:
                    return True

    def checkDiagonalPositive(self, currentPiece):
        for c in range(COLS-4):
            for r in range(ROWS-4):
                if self.board[r][c] == currentPiece and self.board[r+1][c+1] == currentPiece and self.board[r+2][c+2] == currentPiece and self.board[r+3][c+3] == currentPiece and self.board[r+4][c+4] == currentPiece:
                    return True

    def checkDiagonalNegative(self, currentPiece):
        for c in range(COLS-4):
            for r in range(4, ROWS):
                if self.board[r][c] == currentPiece and self.board[r-1][c+1] == currentPiece and self.board[r-2][c+2] == currentPiece and self.board[r-3][c+3] == currentPiece and self.board[r-4][c+4] == currentPiece:
                    return True