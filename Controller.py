from Board import Board
from Player import Player
from Rule import Rule


class Controller:
    rule = Rule()
    gameRunning = True
    playerX = Player("x")
    playerO = Player("o")

    def validInput(self, playerInput, board):
        invalid = True
        if 1 <= playerInput <= 9 and board[playerInput - 1] == "-":
            return True
        else:
            return False

    def changePlayer(self, currenPlayer: Player):
        if currenPlayer.getSign().__eq__("x"):
            return self.playerO
        else:
            return self.playerX

    def gameStarter(self, boardTicTacToe: Board):
        rule = self.rule
        board = boardTicTacToe.getBoard()
        currentPlayer = self.playerX
        while self.gameRunning:
            boardTicTacToe.printBoard()
            playerInput = int(input("Enter  a number 1-9"))
            if self.validInput(playerInput, board):
                boardTicTacToe.setSign(playerInput, currentPlayer)
                self.showWinningWhenWon(boardTicTacToe, currentPlayer)
                currentPlayer = self.changePlayer(currentPlayer)
            else:
                print("NOPE You cant")

    def showWinningWhenWon(self, boardTicTacToe: Board, currentPlayer: Player):
        if self.rule.isWinning(boardTicTacToe, currentPlayer):
            self.createWinnerText(currentPlayer)
            self.gameRunning = False

    def createWinnerText(self, currentPlayer: Player):
        print(currentPlayer.getSign(), "has won ")
