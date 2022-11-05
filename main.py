board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currenPlayer = "x"
winner = None
gameRunning = True


def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput(board):
    playerInput = int (input("Enter  a number 1-9"))
    if 1 <= playerInput <= 9 and board[playerInput - 1] == "-":
        board[playerInput-1] = currenPlayer
    else:
        print("NOPE You cant")


printBoard(board)
