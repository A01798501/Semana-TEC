from turtle import *
from freegames import vector

'''Las funciones "line", "square", "circle", "rectangle" y "triangle" se utilizan para dibujar líneas, cuadrados, círculos, rectángulos y triángulos, respectivamente. 
Cada función toma dos argumentos, que representan el punto de inicio y el punto final de la forma a dibujar. 
Dentro de cada función, se utilizan las funciones de Turtle para mover la tortuga a la posición correcta y dibujar la forma.'''

def line(start, end):
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    #función creada
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


def rectangle(start, end):
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

def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
   begin_fill()
   
   for _ in range (3):
       forward(end.x-start.x)
       left(120)
       
       end fill()
'''La función "tap" se utiliza para manejar la entrada del usuario. Si el usuario hace clic en la ventana gráfica
Se guarda la posición del clic como el punto de inicio o se dibuja la forma correspondiente,
dependiendo de si ya hay un punto de inicio almacenado en el estado actual.'''
def tap(x, y):
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

        '''La función "store" se utiliza para almacenar valores en el estado actual.
        El estado actual se almacena como un diccionario llamado "state", que contiene las claves "start" y "shape". 
        La clave "start" almacena el punto de inicio actual y la clave "shape" almacena la función que se utilizará para dibujar la próxima forma.'''
def store(key, value):
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
'''El usuario puede utilizar diferentes teclas para cambiar el color de la línea, deshacer la última forma dibujada y seleccionar la forma a dibujar.
Finalmente, el bucle principal de la biblioteca Turtle se inicia con la función "done()", lo que permite que el usuario interactúe con la ventana gráfica.'''
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
