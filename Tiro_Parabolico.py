from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
score = 0

def tap(x, y):
    #Función que realiza el disparo al hacer click..
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # Modificamos para aumentar la velocidad del proyectil (punto rojo)
        speed.x = (x + 200) / 15
        speed.y = (y + 200) / 15

def inside(xy):
    #Esta función toma un vector xy como argumento y devuelve un valor booleano que indica si el vector está dentro de los límites de la pantalla.
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    #Esta función borra la pantalla y dibuja los objetivos y la pelota en sus posiciones actuales.
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    '''Esta función se ejecuta continuamente y se encarga de actualizar las posiciones de los objetos en pantalla. 
    Si es necesario, genera nuevos objetivos. 
    También actualiza la posición de la pelota disparada por el jugador.
    Si la pelota golpea un objetivo, se elimina de la lista y se suma un punto al puntaje del jugador. '''
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

        # Nueva condición para generar nuevas pelotas
        if not inside(target):
            target.x = 200
            target.y = randrange(-150, 150)

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
        else:
            global score
            score += 1

    draw()

    # Modificamos para hacer que las pelotas se muevan más rápido
    ontimer(move, 10)

    # Agregamos una nueva pelota si no hay suficientes en pantalla
    if len(targets) < 4:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
