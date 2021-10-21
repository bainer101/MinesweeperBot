from src.classes.Controller import Controller
from src.enums.Difficulty import Difficulty


def main():
    controller = Controller("https://www.minesweeperonline.com/")
    controller.changeDifficulty(Difficulty.CUSTOM, (50, 20, 998))


if __name__ == '__main__':
    main()
