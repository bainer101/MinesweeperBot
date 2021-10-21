class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getID(self):
        return str(self.y) + '_' + str(self.x)
