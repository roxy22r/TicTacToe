from Player import Player


class Board:
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    winner = None
    gameRunning = True

    def printBoard(self):
        print()
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("---------")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("---------")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def setSign(self, position: int, currenPlayer: Player):
        self.board[position - 1] = currenPlayer.getSign()

    def getBoard(self):
        return self.board

    def isFieldFree(self, pos: int) -> bool:
        return self.board[pos - 1].__eq__("-")
