from src.classes.Board import Board

b1 = Board(10, 10)
print(b1.x)
print(b1.y)
print(b1.getBoard())
b1.changeDimensions(12, 12)
print(b1.getBoard())