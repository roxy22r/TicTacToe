from Board import Board
from Player import Player


class Rule:

    def isWinning(self, boardTicTacToe: Board, currentPlayer: Player) -> bool:
        return self.__horizontal(boardTicTacToe, currentPlayer) or self.__vertical(boardTicTacToe, currentPlayer) or self.__diagonal(boardTicTacToe,currentPlayer)

    def __horizontal(self, board: Board, plyer: Player):
        self.board = board.getBoard()
        sign = plyer.getSign()
        cell = 0
        while cell < len(self.board):
            if self.board[cell] == sign and self.board[cell + 1] == sign and self.board[cell + 2] == sign:
                return True
            cell = cell + 3
            print(cell)

        return False

    def __vertical(self, boardTicTacToe: Board, currentPlayer: Player):
        board = boardTicTacToe.getBoard()
        sign = currentPlayer.getSign()
        cell = 0
        while cell < len(board):
            if board[0 + cell] == sign and board[3 + cell] == sign and board[6 + cell] == sign:
                return True

            cell = cell + 3

        return False

    def __diagonal(self, boardTicTacToe: Board, currentPlayer: Player):
        board = boardTicTacToe.getBoard()
        sign = currentPlayer.getSign()
        cell = 0
        while cell < len(board):
            if board[0 + cell] == sign and board[4] == sign and board[8 - cell] == sign:
                return True
            if cell == 6:
                return False
            cell = 6

        return False
