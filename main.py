from Board import Board
from Rule import Rule

board = Board()
board.printBoard()
rule = Rule()
gameRunning = True

while gameRunning:
    board.playerInput()
    board.printBoard()
    if rule.horizontal(board):
        print(board.currenPlayer, "has won ")
        gameRunning = False
        break
