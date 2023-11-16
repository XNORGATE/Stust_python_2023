
import math

class MyShape:
    def __init__(self, square_side, length, width, radius):
        self.square_side = square_side
        self.length = length
        self.width = width
        self.radius = radius
    
    def getSquareArea(self):
        return self.square_side ** 2
    
    def getRectangleArea(self):
        return self.length * self.width
    
    def getCircleArea(self):
        return math.pi * self.radius ** 2

# Create objects and call class methods
square = MyShape(5, 0, 0, 0)
rectangle = MyShape(0, 6, 8, 0)
circle = MyShape(0, 0, 0, 4)

print(square.getSquareArea()) # Output: 25
print(rectangle.getRectangleArea()) # Output: 48
print(circle.getCircleArea()) # Output: 50.26548245743669
