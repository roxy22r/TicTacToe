from Board import Board
from Player import Player


class Rule:

    def isWinning(self, board: Board, player: Player):
        board = board.getBoard()
        sign = player.getSign()
        cell = 0
        row = 0
        while cell < len(board):
            if self.__isHorizontalFilledWithPlayerSign(board, sign, cell) or self.__isVerticalFilledWithPlayerSign(
                    board, sign, row) or self.__isDiagonalFilledWithPlayerSign(board, sign, row):
                return True
            row = row + 1
            cell = cell + 3

        return False

    def __isHorizontalFilledWithPlayerSign(self, board: Board, sign: str, cell: int) -> bool:
        return board[cell].__eq__(sign) and board[cell + 1].__eq__(sign) and board[cell + 2].__eq__(sign)

    def __isVerticalFilledWithPlayerSign(self, board: Board, sign: str, row: int) -> bool:
        return board[0 + row].__eq__(sign) and board[3 + row].__eq__(sign) and board[6 + row].__eq__(sign)

    def __isDiagonalFilledWithPlayerSign(self, board: Board, sign: str, cell: int) -> bool:
        if cell == 0 or cell == 6:
            return board[0 + cell].__eq__(sign) and board[4].__eq__(sign) and board[8 - cell].__eq__(sign)
        return False
