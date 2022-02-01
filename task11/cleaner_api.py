import pure_robot


class Monad:
    def __init__(self, state):
        self._state = state

    def bind(self, fn):
        res, state = fn(self._state)
        return Monad(state)


def move(dist):
    def fn(state):
        return 'success', pure_robot.move(pure_robot.transfer_to_cleaner, dist, state)
    return fn


def set(new_state):
    def fn(state):
        return 'success', pure_robot.set_state(pure_robot.transfer_to_cleaner, new_state, state)
    return fn


def turn(angle):
    def fn(state):
        return 'success', pure_robot.turn(pure_robot.transfer_to_cleaner, angle, state)
    return fn


def start():
    def fn(state):
        return 'success', pure_robot.start(pure_robot.transfer_to_cleaner, state)
    return fn


def stop():
    def fn(state):
        return 'success', pure_robot.stop(pure_robot.transfer_to_cleaner, state)
    return fn


def init():
    return Monad(pure_robot.RobotState(0, 0, 0, pure_robot.WATER))
