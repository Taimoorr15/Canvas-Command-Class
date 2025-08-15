from point import Point
from line import Line

class Pen:
    def __init__(self, panel, x=0, y=0):
        self.panel = panel
        self.x = x
        self.y = y

    def moveTo(self, x, y):
        """Move the pen to an absolute position (x, y)."""
        self.x = x
        self.y = y

    def lineTo(self, x, y):
        """Draw a line from current position to (x, y) and update position."""
        start = Point(self.x, self.y)
        end = Point(x, y)
        self.panel._lines.append(Line(start, end))
        print(f"Drawing line from ({self.x}, {self.y}) to ({x}, {y})")
        self.x = x
        self.y = y

    def getPosition(self):
        """Return current pen position."""
        return (self.x, self.y)




