#Se importan librerías
from random import randrange
from turtle import *

from freegames import square, vector

'''Se crea el vector 'food' con las coordenadas (0, 0)
 que será la posición inicial de la comida,
 se crea la serpiente, con un solo segmento de longitud 10, 
 en la posición inicial (10, 0), se inicializa la variable 'aim' 
 que contiene la dirección en la que se moverá la serpiente
 '''
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
color1 = random.randint(1,5)
color2 = random.randint(1,5)
#if para los 5 colores aleatorios
if color1 != color2:
    if color1==1:
        color1='orange'
    if color1==2:
        color1='yellow'
    if color1==3:
        color1='blue'
    if color1==4:
        color1='pink'
    if color1==5:
        color1='green'
        
    if color2==1:
        color2='orange'
    if color2==2:
        color2='yellow'
    if color2==3:
        color2='blue'
    if color2==4:
        color2='pink'
    if color2==5:
        color2='green'
else:
    color1='blue'
    color2='magenta'


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

'''Se añade la función que hace que la comida se mueva un paso a la vez a cierta posición aleatoria'''
def move_food():
    """Move food one segment in a random direction."""
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    direction = directions[randrange(4)]
    
    # movimiento de la comida un paso a la vez
    food.move(direction)
    
    # condicional que verifica si se encuentra dentro de la ventana
    if not inside(food):
        # se mueve a una posición aleatoria
        food.x = randrange(-19, 19) * 10
        food.y = randrange(-19, 19) * 10
    
    # se mueve la comida con cierto tiempo de espera
    ontimer(move_food, 500)


def move():
    """Move snake forward one segment."""
    #se copia el ultimo segmento de la serpiente para convertirlo en la nueva cabeza
    head = snake[-1].copy()
    head.move(aim)
    
    #si la cabeza choca con un limite se termina el juego y se crea un cuadrado rojo
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    #se agrega la nueva cabeza a la lista 'snake'
    snake.append(head)

    #si la cabeza y la comida estan en el mismo segmento, 
    #se le agrega un segmento a la serpiente y aparece una 
    #nueva comida aleatoriamente
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-19, 19) * 10
        food.y = randrange(-19, 19) * 10
    else:
        snake.pop(0)

    #se limpia la pantalla
    clear()

    #se crean los segmentos de la serpiente
    for body in snake:
        square(body.x, body.y, 9, color1)

    #se crea la comida
    square(food.x, food.y, 9, color2)
    update()

    #tiempo de delay del movimiento de la serpiente
    ontimer(move, 100)


setup(420, 420, 370, 0)  #limites de la ventana
hideturtle()  #se oculta el cursor de turtle
tracer(False)  
listen()

#entrada de teclado para poder mover la serpiente
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

#se comienza a mover la comida
move_food()

#se comienza a mover la serpiente
move()

done()
