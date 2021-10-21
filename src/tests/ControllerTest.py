import unittest
from ..classes.Controller import Controller
from ..enums.Difficulty import Difficulty


class ControllerTest(unittest.TestCase):
    def setUp(self):
        self.controller = Controller("https://www.minesweeperonline.com/")

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
            self.assertEqual(self.controller.getCellDimensions(), (25, 50))


if __name__ == '__main__':
    unittest.main()
