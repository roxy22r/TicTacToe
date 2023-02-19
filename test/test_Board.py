import unittest

from Board import Board
from Player import Player


class TestBoard(unittest.TestCase):

    def test_isFieldFree_posFreeFiledSetPlayerX_True(self):
        self.board = Board()
        isFree = self.board.isFieldFree(1)
        self.assertTrue(isFree)

    def test_isFieldFree_posNotFreeSetPlayerX_False(self):
        self.player = Player("X")
        self.board = Board()
        self.board.setSign(1, self.player)
        isFree = self.board.isFieldFree(1)
        self.assertFalse(isFree)
