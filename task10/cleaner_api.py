import pure_robot
from collections import deque


class RobotApi:

    def __init__(self):
        self.stack = deque()
        self.state = pure_robot.RobotState(0, 0, 0, pure_robot.WATER)
        self.transfer = pure_robot.transfer_to_cleaner

    def make(self, command):
        if command == 'move':
            self.state = pure_robot.move(self.transfer, int(self.stack.pop()), self.state)
        elif command == 'turn':
            self.state = pure_robot.turn(self.transfer, int(self.stack.pop()), self.state)
        elif command == 'set':
            self.state = pure_robot.set_state(self.transfer, self.stack.pop(), self.state)
        elif command == 'start':
            self.state = pure_robot.start(self.transfer, self.state)
        elif command == 'stop':
            self.state = pure_robot.stop(self.transfer, self.state)
        else:
            self.stack.append(command)

    def __call__(self, command):
        return self.make(command)


api = RobotApi()
