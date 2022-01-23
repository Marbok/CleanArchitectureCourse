from math import radians

class Angle(object):

    def __init__(self, degree):
        self.degree = degree
        self.radians = radians(degree)

    def get_degree(self):
        return self.degree

    def get_radians(self):
        return self.radians

    def plus(self, degree):
        self.degree = (self.degree + degree) % 360
        self.radians = radians(self.degree)