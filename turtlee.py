# turtlee.py
import turtle as _t

class Turtle:
    def __init__(self, pen):
        # Basic duck-typing guard
        if not hasattr(pen, "getPosition") or not hasattr(pen, "lineTo"):
            raise TypeError("Turtle expects a Pen-like object with getPosition() and lineTo(x, y).")

        self.pen = pen
        self.turtle = _t.Turtle()
        self.turtle.speed(0)  # fastest

        # Start at the Pen’s current position
        x, y = self.pen.getPosition()
        self.turtle.penup()
        self.turtle.goto(float(x), float(y))
        self.turtle.pendown()

    def forward(self, distance: float):
        # Move the on-screen turtle
        self.turtle.forward(distance)
        # Sync the Pen’s stored position to the on-screen position
        sx, sy = self.turtle.position()
        self.pen.lineTo(float(sx), float(sy))

    def turnLeft(self, angle: float):
        self.turtle.left(angle)

    def turnRight(self, angle: float):
        self.turtle.right(angle)

    def getPos(self):
        return self.pen.getPosition()


