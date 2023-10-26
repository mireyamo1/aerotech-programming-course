class Coordinate:
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return float(self._x)
    @x.setter
    def x(self, xval):
        if not isinstance(xval, int) and not isinstance(xval, float):
            raise TypeError("The value must be a `int` or 'float' type.")
    @property
    def y(self):
        return float(self._y)
    @y.setter
    def y(self, yval):
        if not isinstance(yval, int) and not isinstance(yval, float):
            raise TypeError("The value must be a `int` or 'float' type.")

    # Distance to origin
    def distance_to_origin(self):
        return (self.x**2+self.y**2)**0.5
    def __add__(self, val2):
        return Coordinate(self.x + val2.x, self.y + val2.y)
    
    def __sub__(self, val2):
        return Coordinate(self.x - val2.x, self.y - val2.y)
    
    
