from State import State
from geometry.Angle import Angle
from geometry.Coordinate2D import Coordinate2D

class Robot(object):

    def __init__(self):
        self.coordinate = Coordinate2D(0, 0)
        self.angle = Angle(0)
        self.state = State.WATER

    def stop(self):
        print("STOP")

    def start(self):
        print("START WITH {}".format(self.state))

    def turn(self, angle):
        self.angle.plus(angle)
        print("ANGLE {}".format(self.angle.get_degree()))

    def move(self, distance):
        self.coordinate.move(distance, self.angle)
        print("POS {},{}".format(self.coordinate.x, self.coordinate.y))

    def set(self, state):
        self.state = state
        print("STATE {}".format(self.state))