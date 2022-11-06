from Board import Board


class Rule:

    def horizontal(self, boardTicTacToe: Board):
        board = boardTicTacToe.getBoard()
        player = boardTicTacToe.currenPlayer
        cell = 0
        while cell < len(board):
            if board[cell] == player and board[cell + 1] == player and board[cell + 2] == player:
                return True
            cell = cell + 3
            print(cell)

        return False

    def vertical(self, boardTicTacToe: Board):
        board = boardTicTacToe.getBoard()
        player = boardTicTacToe.currenPlayer
        cell = 0
        while cell < len(board):
            if board[0 + cell] == player and board[3 + cell] == player and board[6 + cell] == player:
                return True

            cell = cell + 3
            print(cell)

        return False

    def diagonal(self, boardTicTacToe: Board):
        board = boardTicTacToe.getBoard()
        player = boardTicTacToe.currenPlayer
        cell = 0
        while cell < len(board):
            if board[0 + cell] == player and board[4] == player and board[8 - cell] == player:
                return True
            if cell == 6:
                return False
            cell = 6
            print(cell)

        return False
