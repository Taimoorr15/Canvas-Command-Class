from turtlee import Turtle

class Command:
    def execute(self, turtlee: Turtle):
        """Execute a drawing command using the given turtle."""
        raise NotImplementedError("Subclasses must override execute()")

class zigzagCommand(Command):
    def execute(self, turtlee: Turtle):
        for _ in range(3):
            turtlee.forward(50)
            turtlee.turnLeft(45)
            turtlee.forward(50)
            turtlee.turnRight(45)

class squareCommand(Command):
    def execute(self, turtlee: Turtle):
        for _ in range(4):
            turtlee.forward(50)
            turtlee.turnRight(90)
