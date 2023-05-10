from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

'''función añadida que dibuja un círculo'''
def circle(start, end):
    "Draw circle from start to end."
    rad = math.sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2)
    center_x = start.x + (end.x - start.x) / 2
    center_y = start.y + (end.y - start.y) / 2
    center = vector (center_x, center_y)
    
    up()
    goto (center.x, center.y - rad)
    down ()
    circle = 2 * math.pi * rad
    begin_fill()
    
    for i in range (360):
        forward (circle / 360)
        left(1)
    end_fill()

#funcion rectangulo
def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for i in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()

#FUNCION TRIANGULO
def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
   begin_fill()
   
   for _ in range (3):
       forward(end.x-start.x)
       left(120)
       
       end fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
'''color añadido para poder dibujar con el color amarillo, necesario teclear "Y" en mayus'''
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()