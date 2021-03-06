import unittest
from random import randint
from ..classes.Controller import Controller
from ..classes.Cell import Cell
from ..enums.Difficulty import Difficulty
from ..enums.DisplaySize import DisplaySize


class ControllerTest(unittest.TestCase):
    def setUp(self):
        self.controller = Controller("https://www.minesweeperonline.com/", Difficulty.EXPERT, DisplaySize.TWO_HUNDRED)

    def test_get_cell_dimensions(self):
        self.assertEqual(self.controller.getCellDimensions(), (30, 16))

    def test_change_difficulty(self):
        with self.subTest():
            self.controller.changeDifficulty(Difficulty.BEGINNER)
            self.assertEqual(self.controller.getCellDimensions(), (9, 9))
        with self.subTest():
            self.controller.changeDifficulty(Difficulty.INTERMEDIATE)
            self.assertEqual(self.controller.getCellDimensions(), (16, 16))
        with self.subTest():
            self.controller.changeDifficulty(Difficulty.CUSTOM, (50, 25, 100))
            self.assertEqual(self.controller.getCellDimensions(), (50, 25))

    def test_change_display_size(self):
        with self.subTest():
            self.assertEqual(self.controller.getDisplaySize(), DisplaySize.TWO_HUNDRED)
        with self.subTest():
            self.controller.setDisplaySize(DisplaySize.ONE_HUNDRED)
            self.assertEqual(self.controller.getDisplaySize(), DisplaySize.ONE_HUNDRED)
        with self.subTest():
            self.controller.setDisplaySize(DisplaySize.ONE_HUNDRED_FIFTY)
            self.assertEqual(self.controller.getDisplaySize(), DisplaySize.ONE_HUNDRED_FIFTY)

    def test_click_and_read(self):
        for x in range(10):
            x = randint(1, self.controller.getCellDimensions()[0])
            y = randint(1, self.controller.getCellDimensions()[1])
            cell = Cell(x, y)
            self.controller.clickCell(cell)
            self.assertIn(self.controller.readCell(cell), [None, 'Flag']+list(range(-1, 9)))


if __name__ == '__main__':
    unittest.main()
