from Board import Board
from Player import Player
from Rule import Rule
from View import View


class Controller:
    view = View()
    boardTicTacToe = Board()
    rule = Rule()
    gameRunning = True
    playerX = Player("x")
    playerO = Player("o")

    def __validInput(self, playerInput: int):
        return 1 <= playerInput <= 9 and self.boardTicTacToe.isFieldFree(playerInput)

    def changePlayer(self, currendPlayer: Player):
        return self.playerO if currendPlayer.getSign().__eq__("x") else self.playerX

    def __gameStarter(self):
        rule = self.rule
        currentPlayer = self.playerX
        while self.gameRunning:
            print("It is turn of player", currentPlayer.getSign(), "\n")
            self.boardTicTacToe.printBoard()
            playerInput: int = self.__playerInput()
            if self.__validInput(playerInput):
                self.boardTicTacToe.setSign(playerInput, currentPlayer)
                self.__showWinningWhenWon(self.boardTicTacToe, currentPlayer)
                currentPlayer = self.changePlayer(currentPlayer)
            else:
                print("NOPE You cant")

    def __playerInput(self) -> int:
        try:
            return int(input("Enter  a number 1-9"))
        except:
            return self.__playerInput()

    def __showWinningWhenWon(self, boardTicTacToe: Board, currentPlayer: Player):
        if self.rule.isWinning(boardTicTacToe, currentPlayer):
            self.boardTicTacToe.printBoard()
            self.view.createWinnerText(currentPlayer)
            self.gameRunning = False
            self.__restart()

    def play(self):
        self.view.wellcomeText()
        try:
            playerInput = int(input("To Play press 1"))
            if playerInput == 1:
                print("Player x starts")
                self.__gameStarter()
        except:
            self.play()

    def __restart(self):
        try:
            playerInput: int = int(input("Do you want to restart the game enter 1 else 2 to end it"))
            if playerInput == 1:
                self.__gameStarter()
            else:
                self.play()
        except:
            self.__restart()
