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

class Command(object):
    def __init__(self, robot):
        self.robot = robot

class Start(Command):
    def apply(self, params):
        self.robot.start()

class Stop(Command):
    def apply(self, params):
        self.robot.stop()

class Set(Command):
    def apply(self, params):
        state = State[params[0].upper()]
        self.robot.set(state)

class Move(Command):
    def apply(self, params):
        dist = int(params[0])
        self.robot.move(dist)

class Turn(Command):
    def apply(self, params):
        angle = int(params[0])
        self.robot.turn(angle)

class Parser(object):

    def __init__(self, robot):
        self.commands = {
            "start": Start(robot),
            "stop": Stop(robot),
            "set": Set(robot),
            "move": Move(robot),
            "turn": Turn(robot)
        }

    def parse(self, line):
        tokens = line.split()
        return self.commands.get(tokens[0]), tokens[1:]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Write path to script')
    path = sys.argv[1]
    robot = Robot()
    parser = Parser(robot)

    with open(path, 'r') as f:
        for line in f:
            cmd, params = parser.parse(line)
            cmd.apply(params)