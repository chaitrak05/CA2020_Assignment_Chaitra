# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Bth classes have an area function which can print the area of the shape where Shape’s area is 0 by default.
class Shape:
    area = 0
    length = 0

    def area(self):
        area = self.length * self.length


class Square(Shape):

    def __init__(self, length):
        Shape.length = length

    def area(self):
        area = self.length * self.length
        print("Area of the square is:", area )


s = Square(2)
s.area()
