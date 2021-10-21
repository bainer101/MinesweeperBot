
#Takes in the size of the board as parameters
class Board:

    #Initalised the board object and calls setBoard
    def __init__(self, x, y):
        self.board = []
        self.x = x
        self.y = y
        self.setBoard()

    # Sets the size of the board based on the x and y
    def setBoard(self):
        for x in range(self.x):
            self.board.append([])
            for y in range(self.y):
                self.board[x].append(0)


    # Returns the size of the board
    def getBoardSize(self):
        return self.x, self.y

    def getBoard(self):
        for row in self.board:
            if(row == None):
                print('HELLO')
            else:
                print(row)
    
    # Changes the size of the board
    def changeDimensions(self, newX, newY):
        self.board = []
        self.x = newX
        self.y = newY
        for x in range(self.x):
            self.board.append([])
            for y in range(self.y):
                self.board[x].append(0)
    
