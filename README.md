# Semana-TEC
Herramientas computacionales: El Arte de la Programación (GPO 201)

Como proyecto, se tuvo que actualizar y hacer ciertas mejoras a 5 códigos, en este caso videojuegos simples principalmente
programados y/o realizados con freegames, en todos los casos las mejoras son para poder tener una mejor experiencia de
jugabilidad, a continuación se enlistarán los juegos con sus correspondientes mejoras.

1. Juego Pintado.
pass
--------------------------------------------------------------------
2. Juego de la Víbora.

    a) La comida podrá moverse al azar un paso a la vez y no deberá de salirse de la ventana.
    Para lograr este punto se efectuó lo siguiente en el código.

    def move_food():
    '''Se añade la función que hace que la comida se mueva un paso a la vez a cierta posición aleatoria'''
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

    b) Cada vez que se corra el juego, la víbora y la comida deberán tener colores diferentes entre sí, pero al azar, de una serie de 5 diferentes colores, excepto el rojo.
    Se añadió lo siguiente al inicio del código.

    #Se importa random
    import random

    #Se utiliza random.randint para poder tener una gama de 5 colores diferentes al empezar el juego.
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

--------------------------------------------------------------------
3. Juego del Packman.
pass
--------------------------------------------------------------------
4. Juego del Tiro Parabólico.
pass
--------------------------------------------------------------------
5. Juego de Memoria

    a) Contar y desplegar el numero de taps
    Se creó una función para ello.
    def update_taps():
        '''FUNCION PARA MOSTRAR LOS TAPS '''
        up()
        goto(-180,200)
        color ('black')
        write('Taps: '+str(taps), font =('Arial', 18, 'normal'))

    b) Detectar cuando todos los cuadros se han destapado

    Dentro de la función draw() se crea un condicional que detecta que no existan valores escondidos.

    if all(item == False for item in hide):
        #se llama a la función message para alertar que se ha terminado el juego
        message("Fin del juego")

    Igualmente una función que despliega un mensaje arriba de la cuadricula para alertar al jugador que el juego ha terminado

    def message(message):
    '''FUNCION PARA MOSTRAR EL MENSAJE ENCIMA DE LA CUADRICULA '''
    up()
    goto(0, 250)
    color('black')
    write('Alerta: '+ message, font=('Arial', 50, 'normal'), align="center")

    c) Centrar el dígito en el cuadro
    
    Dentro de la función draw se añadió y se modificaron los valores de 'x' y 'y' de:

    # Se verifica si hay una ficha seleccionada, y si es así, se muestra la letra en su centro.
    mark = state['mark']
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        #se centran los caractéres correspondientes en el cuadrado
        goto(x + 16, y + 10)
        color('black')
        write(tiles[mark], font=('Arial', 20, 'normal'))

    d) Como un elmento de innovación al juego, podrías utilizar algo diferente a los dígitos para resolver el juego y que al usuario le ayude a tener mejor memoria ?

    Principalmente el juego mostraba digitos del 0 al 31 dos veces para poder obtener los pares, como equipo se decidió mostrar el abecedario y los siguientes caractéres ['@', '#', '$', '%', '&', '*'], ya que tal vez la persona jugando esta menos famirializado con estos mismos y ayudaría a fomentar la mejora de memoria.

    # lista de digitos.
    tiles = list(range(32)) * 2

    #lista de abecedario y caractéres.
    tiles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '@', '#', '$', '%', '&', '*'] * 2

