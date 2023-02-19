from Player import Player


class View:
    def wellcomeText(self):
        print("\n")
        print(",--------. ,--.              ,--.                         ,--.   ")
        print("'--.  .--' `--'  ,---.     ,-'  '-.  ,--,--.  ,---.     ,-'  '-.  ,---.   ,---. ")
        print("   |  |    ,--. | .--'     '-.  .-' ' ,-.  | | .--'     '-.  .-' | .-. | | .-. :")
        print("   |  |    |  | \ `--.       |  |   \ '-'  | \ `--.       |  |   ' '-' ' \   --.")
        print("   `--'    `--'  `---'       `--'    `--`--'  `---'       `--'    `---'   `----'")
        print("\n")

    def createWinnerText(self, currentPlayer: Player):
        print(currentPlayer.getSign(), "has won ")
