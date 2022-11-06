from Board import Board


class Rule:

    def horizontal(self, boardTicTacToe: Board):
        board = boardTicTacToe.getBoard()
        player = boardTicTacToe.currenPlayer
        for cell in range(len(board)):
            if board[cell] == player and board[cell + 1] == player and board[cell + 2] == player:
                return True
            cell += 3

        return False
