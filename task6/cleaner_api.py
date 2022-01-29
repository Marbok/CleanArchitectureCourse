import pure_robot

# класс Чистильщик API
class CleanerApi:


    # взаимодействие с роботом вынесено в отдельную функцию
    def transfer_to_cleaner(self,message):
        print (message)


    def _handle_cmd(self, command, state):
        cmd = command.split(' ')
        if cmd[0]=='move':
            return pure_robot.move(self.transfer_to_cleaner, int(cmd[1]), state) 
        elif cmd[0]=='turn':
            return pure_robot.turn(self.transfer_to_cleaner, int(cmd[1]), state)
        elif cmd[0]=='set':
            return pure_robot.set_state(self.transfer_to_cleaner, cmd[1], state) 
        elif cmd[0]=='start':
            return pure_robot.start(self.transfer_to_cleaner, state)
        elif cmd[0]=='stop':
            return pure_robot.stop(self.transfer_to_cleaner, state)

    def _handle(self, code, state):
        if (len(code) == 0):
            return state
        new_state = self._handle_cmd(code[0], state)
        return self._handle(code[1:], new_state)

    # используем рекурсию и не создаем промежуточное состояние вычислений
    def activate_cleaner(self, code):
        init_state = pure_robot.RobotState(0.0, 0.0, 0, pure_robot.WATER)
        return self._handle(code, init_state)
