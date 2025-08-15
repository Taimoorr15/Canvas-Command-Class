import math

class Point:
    def __init__(self,x:float,y:float):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self,new_x):
        if new_x != self._x:
            self._x = new_x
        else:
            return self._x
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self,new_y):
        if new_y != self._y:
            self._y = new_y 
        else:
            return self._y

    # Added getter methods for compatibility
    def getx(self):
        return self._x
    
    def gety(self):
        return self._y
        
    def distance(self, other):
        dx = self._x - other.x
        dy = self._y - other.y
        return math.sqrt(dx**2 + dy**2)
    
    def __add__(self, other):
        return Point(self._x + other.x, self._y + other.y)

    def __sub__(self, other):
        return Point(self._x - other.x, self._y - other.y)

    def __str__(self):
        return f"Point({self._x}, {self._y})"


        
