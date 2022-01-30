# класс Чистильщик API
class CleanerApi:

    # конструктор
    def __init__(self, state, action, move, turn, set_state, start, stop):
        self.cleaner_state = state
        self.transfer_to_cleaner = action
        self._move = move
        self._turn = turn
        self._set_state = set_state
        self._start = start
        self._stop = stop

    def get_x(self):
        return self.cleaner_state.x

    def get_y(self):
        return self.cleaner_state.y

    def get_angle(self):
        return self.cleaner_state.angle

    def get_state(self):
        return self.cleaner_state.state

    def activate_cleaner(self, code):
        for command in code:
            cmd = command.split(' ')
            if cmd[0] == 'move':
                self.cleaner_state = self._move(self.transfer_to_cleaner,
                                                int(cmd[1]), self.cleaner_state)
            elif cmd[0] == 'turn':
                self.cleaner_state = self._turn(self.transfer_to_cleaner,
                                                int(cmd[1]), self.cleaner_state)
            elif cmd[0] == 'set':
                self.cleaner_state = self._set_state(self.transfer_to_cleaner,
                                                     cmd[1], self.cleaner_state)
            elif cmd[0] == 'start':
                self.cleaner_state = self._start(self.transfer_to_cleaner,
                                                 self.cleaner_state)
            elif cmd[0] == 'stop':
                self.cleaner_state = self._stop(self.transfer_to_cleaner,
                                                self.cleaner_state)
