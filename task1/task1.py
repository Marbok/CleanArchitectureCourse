import sys
from enum import Enum
from math import cos, sin, radians 

class State(Enum):
    WATER = 1,
    SOAP = 2,
    BRUSH = 3

class Coordinate(object):

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

class Robot(object):

    def __init__(self):
        self.coordinate = Coordinate(0, 0)
        self.angle = Angle(0)
        self.state = State.WATER

    def stop(self):
        print("Stop")

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

def start(robot, params):
    robot.start()

def stop(robot, params):
    robot.stop()

def set(robot, params):
    state = State[params[0].upper()]
    robot.set(state)

def turn(robot, params):
    angle = int(params[0])
    robot.turn(angle)

def move(robot, params):
    dist = int(params[0])
    robot.move(dist)

commands = {
    "start": start,
    "stop": stop,
    "set": set,
    "move": move,
    "turn": turn
}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Write path to script')
    path = sys.argv[1]
    robot = Robot()
    with open(path, 'r') as f:
        for line in f:
            tokens = line.split()
            command = commands.get(tokens[0])
            command(robot, tokens[1:])