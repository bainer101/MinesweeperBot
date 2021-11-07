import os

from selenium import webdriver

from .Cell import Cell

from ..enums.Difficulty import Difficulty
from ..enums.DisplaySize import DisplaySize


# Takes in URL of the Minesweeper game as a parameter
class Controller:
    # Initialises the Controller object by getting the Chrome driver from environment variables and loading URL
    def __init__(self, url, difficulty, size, settings=(None, None, None)):
        self.url = url
        self.difficulty = difficulty
        self.size = size
        self.settings = settings

        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        self.driver = webdriver.Chrome(os.environ.get('CHROME_DRIVER'), options=options)
        self.driver.get(self.url)

        self.setDisplaySize(self.size)
        self.changeDifficulty(self.difficulty, self.settings)

    # Returns dimensions of the board from the difficulty
    def getCellDimensions(self):
        dimensions = {
            Difficulty.BEGINNER: (9, 9),
            Difficulty.INTERMEDIATE: (16, 16),
            Difficulty.EXPERT: (30, 16),
            Difficulty.CUSTOM: tuple(self.settings[0:2])
        }

        return dimensions[self.difficulty]

    # Changes difficulty depending on user's preference
    def changeDifficulty(self, difficulty, settings=(None, None, None)):
        self.difficulty = difficulty
        self.settings = settings
        self.driver.find_element('id', 'options-link').click()
        self.driver.find_element('id', difficulty.value).click()

        if difficulty.value == "custom":
            ids = [self.driver.find_element('id', x) for x in ['custom_' + x for x in ['height', 'width', 'mines']]]
            for i, x in enumerate(ids):
                x.click()
                x.clear()
                x.send_keys(str(settings[i]))

        self.driver.find_element('css selector', '#options > tbody > tr:nth-child(7) > td:nth-child(1) > input').click()

    # Increases the display size to 200%
    def setDisplaySize(self, size):
        self.driver.find_element('id', 'display-link').click()
        self.driver.find_element('id', size.value).click()
        self.driver.find_element('id', 'display-link').click()

    # Gets the current display size
    def getDisplaySize(self):
        self.driver.find_element('id', 'display-link').click()

        out = None
        for size in DisplaySize:
            if self.driver.find_element('id', size.value).is_selected():
                out = size
                break

        self.driver.find_element('id', 'display-link').click()
        return out

    # Reads the given cell's value from the game
    def readCell(self, cell: Cell):
        val = self.driver.find_element('id', cell.getID()).get_attribute('class').split(' ')[1]

        if val == 'blank':
            return None
        if "bomb" in val:
            return -1
        else:
            return int(val[-1])

    # Click on a given cell
    def clickCell(self, cell: Cell):
        self.driver.find_element('id', cell.getID()).click()
