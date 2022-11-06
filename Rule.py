from Board import Board
from Player import Player


class Rule:

    def horizontal(self, boardTicTacToe: Board, currentPlayer: Player):
        board = boardTicTacToe.getBoard()
        sign = currentPlayer.getSign()
        cell = 0
        while cell < len(board):
            if board[cell] == sign and board[cell + 1] == sign and board[cell + 2] == sign:
                return True
            cell = cell + 3
            print(cell)

        return False

    def vertical(self, boardTicTacToe: Board, currentPlayer: Player):
        board = boardTicTacToe.getBoard()
        sign = currentPlayer.getSign()
        cell = 0
        while cell < len(board):
            if board[0 + cell] == sign and board[3 + cell] == sign and board[6 + cell] == sign:
                return True

            cell = cell + 3
            print(cell)

        return False

    def diagonal(self, boardTicTacToe: Board,currentPlayer: Player):
        board = boardTicTacToe.getBoard()
        sign = currentPlayer.getSign()
        cell = 0
        while cell < len(board):
            if board[0 + cell] == sign and board[4] == sign and board[8 - cell] == sign:
                return True
            if cell == 6:
                return False
            cell = 6
            print(cell)

        return False
