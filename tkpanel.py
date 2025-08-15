from typing import List
from line import Line
from point import Point

class TkPanel:
    def __init__(self, height: float, width: float, length: float, lines: List[Line] = None):
        self._height = height
        self._width = width
        self._length = length
        self._lines = lines if lines is not None else []

    """Creates a line from p1 to p2 and adds it to the canvas."""
    def addline(self, p1: Point, p2: Point):
        ax = p1.x + p2.x
        ay = p1.y + p2.y
        return f"The point after adding {p1} and {p2} is ({ax},{ay})"

    def delete(self):
        """Deletes all lines from the canvas."""
        self._lines.clear()
        return "Canvas cleared."

    def draw(self):
        """Draw all lines (dummy print for now)."""
        for line in self._lines:
            print(f"Drawing line from ({line.p1.x}, {line.p1.y}) to ({line.p2.x}, {line.p2.y})")
        return "All objects drawn."
