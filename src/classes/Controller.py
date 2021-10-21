import os

from selenium import webdriver
from selenium.webdriver import Keys


# Takes in URL of the Minesweeper game as a parameter
class Controller:
    # Initialises the Controller object by getting the Chrome driver from environment variables and loading URL
    def __init__(self, url):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        self.driver = webdriver.Chrome(os.environ.get('CHROME_DRIVER'), options=options)
        self.driver.get(url)

    # Finds all cells, filters out those that are hidden and returns dimensions of the board
    def getCellDimensions(self):
        cells = self.driver.find_elements('class name', 'square')
        cells = list(filter(lambda c: 'display: none' not in c.get_attribute('outerHTML'), cells))
        y, x = tuple([int(x) for x in cells[-1].get_attribute('id').split('_')])
        return x, y

    # Changes difficulty depending on user's preference
    def changeDifficulty(self, difficulty, settings=None):
        self.driver.find_element('id', 'options-link').click()
        self.driver.find_element('id', difficulty.value).click()

        if difficulty.value == "custom":
            ids = [self.driver.find_element('id', x) for x in ['custom_' + x for x in ['height', 'width', 'mines']]]
            for i, x in enumerate(ids):
                x.click()
                x.clear()
                x.send_keys(str(settings[i]))

        self.driver.find_element('css selector', '#options > tbody > tr:nth-child(7) > td:nth-child(1) > input').click()
