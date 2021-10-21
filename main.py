from src.classes.Controller import Controller
from src.enums.Difficulty import Difficulty
from src.enums.DisplaySize import DisplaySize


def main():
    controller = Controller("https://www.minesweeperonline.com/", Difficulty.INTERMEDIATE, DisplaySize.TWO_HUNDRED)


if __name__ == '__main__':
    main()
