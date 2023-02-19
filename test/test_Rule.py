from unittest import TestCase

from Board import Board
from Player import Player
from Rule import Rule


class TestRule(TestCase):

    def test_isWinning_firstRowIsSetWithPlayerXSign_true(self):
        self.player = Player("X")
        self.board = Board()
        self.board.setSign(1, self.player)
        self.board.setSign(2, self.player)
        self.board.setSign(3, self.player)
        self.rule = Rule()
        result = self.rule.isWinning(self.board, self.player)
        self.assertTrue(result)

    def test_isWinning_firstRowTwoTimesPlayerXWasSet_false(self):
        self.player = Player("X")
        self.board = Board()
        self.board.setSign(1, self.player)
        self.board.setSign(2, self.player)
        self.rule = Rule()
        result = self.rule.isWinning(self.board, self.player)
        self.assertFalse(result)

    def test_isWinning_firstRowTwoTimesPlayerXWasSetAndLastInRowWithPlayerO_false(self):
        self.playerX = Player("X")
        self.playerO = Player("O")
        self.board = Board()
        self.board.setSign(1, self.playerX)
        self.board.setSign(2, self.playerX)
        self.board.setSign(3, self.playerO)
        self.rule = Rule()
        result = self.rule.isWinning(self.board, self.playerX)
        self.assertFalse(result)

    def test_isWinning_playerXSetInFirstCollOfAllRows_true(self):
        self.player = Player("X")
        self.board = Board()
        self.board.setSign(1, self.player)
        self.board.setSign(4, self.player)
        self.board.setSign(7, self.player)
        self.rule = Rule()
        result = self.rule.isWinning(self.board, self.player)
        self.assertTrue(result)

    def test_isWinning_playerXSetInFirstCollInTwoCollAndLastWithPlayerO_false(self):
        self.playerX = Player("X")
        self.playerO = Player("O")
        self.board = Board()
        self.board.setSign(1, self.playerX)
        self.board.setSign(4, self.playerX)
        self.board.setSign(7, self.playerO)
        self.rule = Rule()
        result = self.rule.isWinning(self.board, self.playerX)
        self.assertFalse(result)

    def test_isWinning_playerXSignSetDiagonal_true(self):
        self.player = Player("X")
        self.board = Board()
        self.board.setSign(1, self.player)
        self.board.setSign(5, self.player)
        self.board.setSign(9, self.player)
        self.rule = Rule()
        result = self.rule.isWinning(self.board, self.player)
        self.assertTrue(result)


