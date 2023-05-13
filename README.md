# Semana-TEC
# Herramientas computacionales: El Arte de la Programación (GPO 201)

Como proyecto, se tuvo que actualizar y hacer ciertas mejoras a 5 códigos, en este caso videojuegos simples principalmente
programados y/o realizados con freegames, en todos los casos las mejoras son para poder tener una mejor experiencia de
jugabilidad, a continuación se enlistarán los juegos con sus correspondientes mejoras.

# Link para el video
https://drive.google.com/file/d/12FyL9_Upumhm3Wr7U45wxaU3VXaY_mrc/view?usp=sharing

# 1. Juego Pintado.
    a) Un color nuevo.
    Para esto solo se uso la sintaxis de los demás colores y se optó por el amarillo
    '''color añadido para poder dibujar con el color amarillo, necesario teclear "Y" en mayus'''
    onkey(lambda: color('yellow'), 'Y')

    b) Dibujar un círculo.
    Para esto se implemento una nueva función basándonos en matématicas básicas y un poco de la sintaxis del programa

    def circle(start, end):
    '''función añadida que dibuja un círculo'''
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

    c) Completar el rectángulo.
    Igualmente se uso la sintaxis del programa pero usando diferentes valores en las direcciones de dibujo.
    
    def rectangle(start, end):
    """Función que dibuja un rectángulo de inicio a fin."""
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

    d) Completar el triángulo

    def triangle(start, end):
    """Función que dibuja un triángulo de principio a fin."""
    up()
    goto(start.x, start.y)
    down()
   begin_fill()
   
   for _ in range (3):
       forward(end.x-start.x)
       left(120)
       
       end fill()
--------------------------------------------------------------------
# 2. Juego de la Víbora.

    a) La comida podrá moverse al azar un paso a la vez y no deberá de salirse de la ventana.
    Para lograr este punto se efectuó lo siguiente en el código.

    def move_food():
    '''Se añade la función que hace que la comida se mueva un paso a la vez a cierta posición aleatoria'''
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    direction = directions[randrange(4)]
    
    #movimiento de la comida un paso a la vez
    food.move(direction)
    
    #condicional que verifica si se encuentra dentro de la ventana
    if not inside(food):
        # se mueve a una posición aleatoria
        food.x = randrange(-19, 19) * 10
        food.y = randrange(-19, 19) * 10
    
    #se mueve la comida con cierto tiempo de espera
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
# 3. Juego del Packman.

    a) Los fantasmas sean más listos.
    Se evaluaron distintas opciones y se llegó a la conclusión que lo más jugable era multiplicar los 
    fantasmas en cierto puntaje 'score',se creó una funciónque crea dos fantasmas, en este caso cuando score = 20, pero puede ser totalmente modificable, posteriormente se llama a la función dentro de un condicional de la función move.

    def add_ghosts():
    '''Se crea una función que añade dos fantasmas al juego'''
    ghosts.append([vector(-100, 160), vector(0, 5)])
    ghosts.append([vector(100, 160), vector(5, 0)])

    def move():
        "Move pacman and all ghosts."
        #Se llama a la función add_ghosts en el momento que score = 20
        global state
        if state['score'] == 20 and len(ghosts) == 4:
            add_ghosts()
        writer.undo()
        writer.write(state['score'])

        clear()

    b) Cambiar tablero.
    Se modificó la matriz, donde los 0´s representan una celda vacía y los 1´s representan una pared, igualmente se cambió 
    el color del mapa al inicio de la función world().

    tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

------------------
def world():
    "Función que dibuja el mapa usando path."
    bgcolor('pink')
    path.color('black')

    c) Hacer que los fantasmas vayan más rápido.
    Para esto simplemente se modificó el valor en ontimer().

    #Si bajamos el numero, los fantasmas van más rapido, si lo subimos, los fantasas se alentan
    ontimer(move, 30)
    
--------------------------------------------------------------------
# 4. Juego del Tiro Parabólico.

    a) La velocidad del movimiento para el proyectil y los balones sea más rápida
    Dentro de la función tap se modificaron los valores de speed.x y speed.y para aumentar la velocidad del proyectil,
    para los balones simplemente se modifico el valor de delay en ontimer().

    def tap(x, y):
    """Función que realiza el disparo al hacer click.."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # Modificamos para aumentar la velocidad del proyectil (punto rojo)
        speed.x = (x + 200) / 15
        speed.y = (y + 200) / 15
    ------
    #Modificamos para hacer que las pelotas se muevan más rápido
    ontimer(move, 10)

    b) Hacer que el juego nunca termine, de manera que los balones al salir de la ventana se re posicionen.
    Se codificaron dos condicionales dentro de la función draw() que se encargaran de verificar si existían balones dentro de la ventana.

        #Nueva condición para generar nuevas pelotas
        if not inside(target):
            target.x = 200
            target.y = randrange(-150, 150)
        -----
        # Agregamos una nueva pelota si no hay suficientes en pantalla
        if len(targets) < 4:
            y = randrange(-150, 150)
            target = vector(200, y)
            targets.append(target)
--------------------------------------------------------------------
# 5. Juego de Memoria

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

    #Se verifica si hay una ficha seleccionada, y si es así, se muestra la letra en su centro.
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

    #lista de digitos.
    tiles = list(range(32)) * 2

    #lista de abecedario y caractéres.
    tiles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '@', '#', '$', '%', '&', '*'] * 2

# Como ejecutar los juegos.

Como primer punto es esencial descargar la librería de freegames, aquí el link de la página del mismo 
https://pypi.org/project/freegames/. En todo caso se puede descargar mediante la terminal con el comando
'pip install freegames', asegurarse de tener instalado pip aunque este viene por defecto en casi todos los equipos
y sistemas operativos.

Hay dos posibles opciones para poder ejecutar nuestros códigos. Si es que estás en un intérprete como Thonny, 
simplemente tienes que descargar el archivo, abrirlo 'ctrl + o' y ejecutar el código 'F5'.

Si es que te encuentras dentro de la terminal, debes asegurarte que te encuentras en el folder o directorio correcto,
para esto se pueden usar los comandos 'cd ..' y 'cd "Location"', una vez dentro de la ubbicación del archivo,
se puede ejecutar usando el comando 'python "file_name"', en todo caso que esto no funcione puedes probar ejecutándolo
con 'python3' a la fecha y versión que se crea este archivo.

image.png

# Como ejecutar los juegos.



