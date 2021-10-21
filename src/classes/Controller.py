import os

from selenium import webdriver


# Takes in URL of the Minesweeper game as a parameter
class Controller:
    # Initialises the Controller object by getting the Chrome driver from environment variables and loading URL
    def __init__(self, url):
        self.driver = webdriver.Chrome(os.environ.get('CHROME_DRIVER'))
        self.driver.get(url)

    # Finds all cells, filters out those that are hidden and returns dimensions of the board
    def getCellDimensions(self):
        cells = self.driver.find_elements('class name', 'square')
        cells = list(filter(lambda c: 'display: none' not in c.get_attribute('outerHTML'), cells))
        y, x = tuple([int(x) for x in cells[-1].get_attribute('id').split('_')])
        return x, y
