from random import randint

from src.classes.Controller import Controller
from src.classes.Cell import Cell

from src.enums.Difficulty import Difficulty
from src.enums.DisplaySize import DisplaySize
from src.classes.Board import Board


def main():
    controller = Controller("https://www.minesweeperonline.com/", Difficulty.INTERMEDIATE, DisplaySize.TWO_HUNDRED)
    board = Board(*controller.getCellDimensions())


if __name__ == '__main__':
    main()
