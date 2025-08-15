from point import Point

class Line(Point):
    def __init__(self, p1, p2):
        if not isinstance(p1, Point) or not isinstance(p2, Point):
            raise TypeError("p1 and p2 must be Point objects")
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return ((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2) ** 0.5

    def __str__(self):
        return f"Line from {self.p1} to {self.p2}"

