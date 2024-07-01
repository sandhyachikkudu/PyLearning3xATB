class shape:
    def area(self):
        print("area of the shape")

class rectangle(shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius * self.radius


shape1 = rectangle(5,5)
print(shape1.area())

shape2 = circle(5)
print(shape2.area())
shape3 = shape()
print(shape3.area())