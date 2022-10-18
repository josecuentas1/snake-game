# Importamos las librerias necesarias.
import turtle
import time
import random

# Inicializamos algunas variables básicas del juego.
delay = 0.1  # Para que el movimiento de la serpiente sea más pausado.
score = 0
high_score = 0

# Creamos un ventana con la librería turtle.
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")

# Configuramos el ancho y el alto de la ventana.
wn.setup(width=600, height=600)
wn.tracer(0)    # Hace las animaciones más cómodas a la vista.

# Dibujamos la cabeza de la serpiente.
cabeza = turtle.Turtle()
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()  # No dibuja el rastro que tienen los objetos.
cabeza.goto(0, 0)   # Lo posiciona al centro del plano cartesiano.
cabeza.direccion = "stop"   # Estado inicial de la cabeza de la serpiente.

# Dibujamos la comida de la serpiente.
comida = turtle.Turtle()
comida.speed(0)  # Que se dibuje incluso antes de que se actualice la ventana
comida.shape("circle")
comida.color("red")
comida.penup()  # No dibuja el rastro que tienen los objetos.
comida.goto(0, 100) # Lo posiciona al centro del Eje X y 100 px en el Eje Y del plano cartesiano.

# Dibujamos la info respecto a la puntuacion del jugador.
caja_texto = turtle.Turtle()
caja_texto.speed(0) # Que se dibuje incluso antes de que se actualice la ventana
caja_texto.shape("square")
caja_texto.color("white")
caja_texto.penup()
caja_texto.hideturtle()  # Escondemos la forma y el fondo del objeto.
caja_texto.goto(0, 250) # Lo posiciona al centro del Eje X y 250 px en el Eje Y del plano cartesiano.
caja_texto.write("Score : 0  High Score : 0", align="center",
                 font=("candara", 24, "bold"))

# Asignamos las teclas Up, Down, Left y Right (flechas) a los movimientos de la serpiente.
def goup():
    if cabeza.direccion != "abajo":  # Antes de ir hacia arriba primero tiene que girar a la derecha o izquierda.
        cabeza.direccion = "arriba"


def godown():
    if cabeza.direccion != "arriba":    # Antes de ir hacia abajo primero tiene que girar a la derecha o izquierda.
        cabeza.direccion = "abajo"


def goleft():
    if cabeza.direccion != "derecha": # Antes de ir hacia la izquierda primero tiene que girar hacia arriba o abajo.
        cabeza.direccion = "izquierda"


def goright():
    if cabeza.direccion != "izquierda":  # Antes de ir hacia la derecha primero tiene que girar hacia arriba o abajo.
        cabeza.direccion = "derecha"


def move():
    if cabeza.direccion == "arriba":
        y = cabeza.ycor() # Obtenemos la Coordenada Y de la cabeza, y la guardamos en la variable y.
        cabeza.sety(y+20)   # Seteamos el nuevo valor de la Coordenada Y .
    if cabeza.direccion == "abajo":
        y = cabeza.ycor()   
        cabeza.sety(y-20)
    if cabeza.direccion == "izquierda":
        x = cabeza.xcor() # Obtenemos la Coordenada X de la cabeza, y la guardamos en la variable x.
        cabeza.setx(x-20)   # Seteamos el nuevo valor de la Coordenada X. 
    if cabeza.direccion == "derecha":
        x = cabeza.xcor()
        cabeza.setx(x+20)


wn.listen() # La ventana ahora está atenta a los eventos
wn.onkeypress(goup, "Up")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")

segmentos = [] # Lista para las partes del cuerpo de la serpiente

# Ejecucion del juego
while True: # Que ejecute siempre hasta que indiquemos lo contrario
    wn.update() # Que la ventana se actualice con los nuevos eventos y movimientos

    # Verificacion si la cabeza colisiona con los bordes de la ventana
    if cabeza.xcor() > 290 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        time.sleep(1) # Pequeña pausa antes de reiniciar el juego.
        cabeza.goto(0, 0) # La cabeza regresa al centro de la ventana
        cabeza.direccion = "stop" # Se indica el nuevo estado de la cabeza
        # Manda cada uno de los segmentos fuera de la ventana
        for segmento in segmentos: 
            segmento.goto(1000, 1000) 
        segmentos.clear() # Borra los segmentos de la lista

        score = 0   # Reinicia la puntacion actual

        # Refresca el contenido de la puntuacion
        caja_texto.clear()
        caja_texto.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))

    # Verificacion si la cabeza colisiona con la comida (la serpiente come)        
    if cabeza.distance(comida) < 20:
        # Crea una nueva comida con coordenadas random
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        comida.goto(x, y) 

        # Agrega un segmento a la cola de la serpiente
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0) # Que no se demore nada en dibujarlo
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")  # Color de la serpiente
        nuevo_segmento.penup() # Dibujar sin 'arrastar el lapiz'
        segmentos.append(nuevo_segmento) # Agrega un nuevo segmento al listado de segmentos
        
        score += 10 # Suma 10 puntos a la puntacion actual

        # Si la puntuacion actual supera a la puntuacion maxima, la actualiza.
        if score > high_score:
            high_score = score
        caja_texto.clear()
        caja_texto.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))

    # Para que los segmentos sigan a la cabeza en su movimiento
    for index in range(len(segmentos)-1, 0, -1):
        x = segmentos[index-1].xcor()
        y = segmentos[index-1].ycor()
        segmentos[index].goto(x, y)

    if len(segmentos) > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    # La cabeza de la serpiente se mueve
    move()

    # Verificacion de colisiones entre la cabeza y los segmentos del cuerpo de la serpiente
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20: # Si cumple significa que colisionó
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direccion = "stop"
            for segmento in segmentos:
                segmento.goto(1000, 1000)
            segmento.clear()

            score = 0
            caja_texto.clear()
            caja_texto.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))

    time.sleep(delay)
