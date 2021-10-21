import unittest
from ..classes.Controller import Controller


class ControllerTest(unittest.TestCase):
    def setUp(self):
        self.controller = Controller("https://www.minesweeperonline.com/")

    def test_get_cell_dimensions(self):
        self.assertEqual(self.controller.getCellDimensions(), (30, 16))


if __name__ == '__main__':
    unittest.main()
