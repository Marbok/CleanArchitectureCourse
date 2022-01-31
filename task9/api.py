import pure_robot


class RobotApi(object):

    def setup(self, cmd_factory):
        self._cmd_factory = cmd_factory

    def make(self, command):
        if not hasattr(self, 'cleaner_state'):
            self.cleaner_state = pure_robot.RobotState(
                0, 0, 0, pure_robot.WATER)

        cmd = command.split(' ')

        self.cleaner_state = self._cmd_factory(cmd[0], self.cleaner_state)(cmd[1:])

        return self.cleaner_state

    def __call__(self, command):
        return self.make(command)


api = RobotApi()
def cmd_factory(cmd, state):
    if cmd == 'move':
        return lambda params: pure_robot.move(pure_robot.transfer_to_cleaner, int(params[0]), state)
    if cmd == 'stop':
        return lambda params: pure_robot.stop(pure_robot.transfer_to_cleaner, state)
    if cmd == 'turn':
        return lambda params: pure_robot.turn(pure_robot.transfer_to_cleaner, int(params[0]), state)
    if cmd == 'start':
        return lambda params: pure_robot.start(pure_robot.transfer_to_cleaner, state)
    if cmd == 'set':
        return lambda params: pure_robot.set_state(pure_robot.transfer_to_cleaner, params[0], state)
    return lambda params: print('Unexpected function', cmd)
api.setup(cmd_factory)
