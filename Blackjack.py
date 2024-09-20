import random
''' Función para la entrega de cartas al azar'''
def tenercartas(): 
    cartasowo = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    return random.choice(cartasowo)

def calcularpuntaje(cartasowo):
    '''Función para calcular el puntaje que se lleva con cada carta que obtienes'''
    valor = sum(cartasowo)
    if valor > 21 and 11 in cartasowo:
        for i in range(len(cartasowo)):
            ''' Aquí se checa si el puntaje es menor a 21 o 11, el as vale 1'''
            if cartasowo[i] == 11:
                cartasowo[i] = 1
                valor = sum(cartasowo)
                break
    return valor

def juego21():
    print("¡Hola! Bienvenido al juego Blackjack ¿estás listo para comenzar?")
    cartasP1 = []
    '''Se repite hasta que el jugador diga que ya no quiere cartas o supere los 21 puntos'''
    while True:
        respuesta = input("¿Quieres una carta? owo -pon 'si' o 'no'- ")

        if respuesta == 'si':
            carta = tenercartas()
            cartasP1.append(carta)
            puntajeP1 = calcularpuntaje (cartasP1)
            print (f"Obtuviste un {carta}.")
            print (f"Tus cartas son: {cartasP1}")
            print (f"Tu puntaje es de: {puntajeP1}")

            if puntajeP1 > 21:
                print("¡Oh no! Superaste los 21 puntos ¡has perdido! :(")
                return
        elif respuesta == 'no':
            break
        else:
            print("Lo que ingresaste es incorrecto, responde 'si' o 'no'")

    '''Esto es para generar el puntaje de la casa'''
    puntajecasa = random.randint(17, 26)
    puntajeP1 = calcularpuntaje(cartasP1)

    '''Aquí dice cuánto puntaje tiene cada uno (jugador y casa)'''
    print(f"Te has detenido al tener un puntaje de {puntajeP1}")
    print(f"La casa tiene un puntaje de {puntajecasa}")

    '''Aquí son las condicionales para saber cuando el jugador pierde, gana o hay empate'''
    if puntajeP1 == 21 and puntajecasa < 21:
        print("¡Enhorabuena! Has ganado con un 21 uwu")
    elif puntajecasa > 21 and puntajeP1 <= 21:
         print("La casa superó los 21 puntos ¡Has ganado! :D")
    elif puntajeP1 <= 21 and puntajeP1 > puntajecasa:
         print("¡Yippieeeeeeee! ¡Ganaste!")
    elif puntajeP1 == puntajecasa:
         if len(cartasP1) < 2: 
            print("¡Ganaste por tener menos cartas!")
         else:
             print("¡Parece que hay un empate!")
    elif puntajeP1 > 21 and puntajecasa > 21:
        print("¡Ambos se pasaron de 21! Es un empate")
    else:
        print("Repámpanos, has perdido :(")

juego21()

