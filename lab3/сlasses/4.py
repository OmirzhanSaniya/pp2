class Point():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def show(self):
        return (self.a, self.b)
    def move(self, new_a, new_b):
        self.a += new_a
        self.b += new_b 
    def dist(self, other_point):
        return ((self.a - other_point.a)**2 + (self.b - other_point.b)**2)**0.5

p1 = Point(int(input()), int(input()))

print(p1.show())

p1.move(int(input()), int(input()))

print(p1.show())

p2 = Point(int(input()), int(input()))

print(p1.dist(p2))