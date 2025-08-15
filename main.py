# main.py
from tkpanel import TkPanel
from pen import Pen
from turtlee import Turtle
from command import zigzagCommand, squareCommand
import turtle as _t  # to keep window open

# Canvas / panel
canvas = TkPanel(height=400, width=400, length=0)

# Pen linked to canvas (Pen prints lines; also appends Line objects if your Pen was updated to do so)
pen = Pen(canvas, 0, 0)  # if your Pen __init__ doesn't accept canvas, use: Pen(0, 0)

# Turtle that uses the Pen
t = Turtle(pen)

print("=== Running Zigzag Command ===")
zig = zigzagCommand()
zig.execute(t)
print("Zigzag complete.\n")

print("=== Running Square Command ===")
sq = squareCommand()
sq.execute(t)
print("Square complete.\n")

# Dump whatever the panel stored (if your Pen appends to panel._lines)
print("=== Canvas Contents ===")
canvas.draw()

# Keep the turtle graphics window open
_screen = _t.Screen()
_screen.exitonclick()



