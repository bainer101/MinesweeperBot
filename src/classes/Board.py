# Takes in the size of the board as parameters
class Board:

    # Initialised the board object and calls setBoard
    def __init__(self, x, y):
        self.board = []
        self.x = x
        self.y = y
        self.setBoard()

    # Sets the size of the board based on the x and y
    def setBoard(self):
        for y in range(self.y):
            self.board.append([])
            for x in range(self.x):
                self.board[y].append(None)

    # Returns the size of the board
    def getBoardSize(self):
        return self.x, self.y

    def getBoard(self):
        return self.board

    # Changes the size of the board
    def changeDimensions(self, new_x, new_y):
        self.board = []
        self.x = new_x
        self.y = new_y
        for y in range(self.y):
            self.board.append([])
            for x in range(self.x):
                self.board[y].append(None)
