from State import State

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