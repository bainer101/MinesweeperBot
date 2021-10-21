from src.classes.Controller import Controller


def main():
    controller = Controller("https://www.minesweeperonline.com/")
    print(controller.getCellDimensions())  # Test to print board dimensions, please remove


if __name__ == '__main__':
    main()
