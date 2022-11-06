from Board import Board
from Rule import Rule

board = Board()
rule = Rule()
gameRunning = True

while gameRunning:
    board.printBoard()
    board.playerInput()
    if rule.horizontal(board) or rule.vertical(board) or rule.diagonal(board):
        print(board.currenPlayer, "has won ")
        gameRunning = False
        break
