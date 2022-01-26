from pure_robot import make, RobotState, WATER, transfer_to_cleaner


def create_robot(x, y, angle, state):
    return RobotState(x, y, angle, state)


def eval(code):
    state = RobotState(0, 0, 0, WATER)
    make(
        transfer_to_cleaner,
        code,
        state
    )

def eval(code, state):
    make(
        transfer_to_cleaner,
        code,
        state
    )
