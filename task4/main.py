import sys

from Robot import Robot
from Parser import Parser

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