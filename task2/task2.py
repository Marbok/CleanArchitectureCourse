import math

# входная программа управления роботом
code = (
    'move 100',
    'turn -90',
    'set soap',
    'start',
    'move 50',
    'stop'
)

# режимы работы устройства очистки
WATER = 1 # полив водой
SOAP  = 2 # полив мыльной пеной
BRUSH = 3 # чистка метлой
 
def move(x, y, angle, dist):
    angle_rads = angle * (math.pi/180.0)
    new_x = x + dist * math.cos(angle_rads)
    new_y = y + dist * math.sin(angle_rads)
    return new_x, new_y

def turn(angle, delta):
    return (angle + delta) % 360

def mapState(sState):
    if sState == 'water':
        return WATER  
    elif sState == 'soap':
        return SOAP
    elif sState == 'brush':
        return BRUSH

def exec(commands):
    x = 0.0
    y = 0.0
    angle = 0
    state = WATER
    for command in commands:
        cmd = command.split(' ')
        if cmd[0]=='move':
            dist = int(cmd[1])
            x, y = move(x, y, angle, dist) 
            print ('POS(',x,',',y,')')

        elif cmd[0]=='turn':
            delta = int(cmd[1])
            angle = turn(angle, delta)
            print ('ANGLE', angle)

        elif cmd[0]=='set':
            state = mapState(cmd[1])
            print ('STATE',state)

        elif cmd[0]=='start':
            print ('START WITH',state)

        elif cmd[0]=='stop':
            print ('STOP')

# главная программа
if __name__ == '__main__':
    exec(code)