from Board import Board
from Player import Player


class Rule:

    def isWinning(self, board: Board, player: Player):
        self.board = board.getBoard()
        sign = player.getSign()
        cell = 0
        row = 0
        while cell < len(self.board):
            if self.__isHorizontalFilledWithPlayerSign(self.board, sign, cell) or self.__isVerticalFilledWithPlayerSign(self.board, sign, row) or self.__isDiagonalFilledWithPlayerSign(self.board, sign, row):
                return True
            row = row+1
            cell = cell + 3

        return False

    def __isHorizontalFilledWithPlayerSign(self, board: Board, sign: str, cell: int) -> bool:
        return self.board[cell] == sign and self.board[cell + 1] == sign and self.board[cell + 2] == sign

    def __isVerticalFilledWithPlayerSign(self, board: Board, sign: str, row: int) -> bool:
        return board[0+row] == sign and board[3+row] == sign and board[6+row] == sign

    def __isDiagonalFilledWithPlayerSign(self, board: Board, sign: str, cell: int) -> bool:
        if cell == 0 or cell == 6:
            return board[0 + cell] == sign and board[4] == sign and board[8 - cell] == sign
        return False
