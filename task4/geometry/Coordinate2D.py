from math import sin, cos

class Coordinate2D(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, distance, angle):
        self.x = self.x + distance * cos(angle.get_radians())
        self.y = self.y + distance * sin(angle.get_radians())

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y