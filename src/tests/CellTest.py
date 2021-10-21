import unittest
from ..classes.Cell import Cell


class CellTest(unittest.TestCase):
    def setUp(self):
        self.cell = Cell(1, 4)

    def test_get_and_set_value(self):
        self.cell.setValue(2)
        self.assertEqual(self.cell.getValue(), 2)

    def test_get_x(self):
        self.assertEqual(self.cell.getX(), 1)

    def test_get_y(self):
        self.assertEqual(self.cell.getY(), 4)

    def test_get_id(self):
        self.assertEqual(self.cell.getID(), '4_1')


if __name__ == '__main__':
    unittest.main()
