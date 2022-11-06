class Board:
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    currenPlayer = "x"
    winner = None
    gameRunning = True

    def printBoard(self):
        print()
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("---------")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("---------")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def playerInput(self):
        playerInput = int(input("Enter  a number 1-9"))
        validInput = False
        while validInput:
            if 1 <= playerInput <= 9 and self.board[playerInput - 1] == "-":
                self.board[playerInput - 1] = self.currenPlayer
                self.changePlayer()
                validInput = True
                break
            else:
                print("NOPE You cant")

    def changePlayer(self):
        if self.currenPlayer.__eq__("x"):

            self.currenPlayer = "o"
        else:
            self.currenPlayer = "x"

    def getBoard(self):
        return self.board
