import unittest
from ..classes.Board import Board


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board(2, 5)

    def test_constructor_and_get_board(self):
        self.assertEqual(self.board.getBoard(), [[None, None], [None, None], [None, None], [None, None], [None, None]])

    def test_get_board_size(self):
        self.assertEqual(self.board.getBoardSize(), (2, 5))

    def test_change_dimensions(self):
        self.board.changeDimensions(5, 2)
        self.assertEqual(self.board.getBoard(), [[None, None, None, None, None], [None, None, None, None, None]])


if __name__ == '__main__':
    unittest.main()
