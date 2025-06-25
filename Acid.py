class Square:
    def __init__(self,side):
        self.side = side
        
    def area(self):
        print("The Area of square is: " ,self.side)

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print("The Area of the circle is: ", 3.14 * self.radius**2)
        
s = Square(7)
c = Circle(7)
for shape in(s,c):
    shape.area()                           