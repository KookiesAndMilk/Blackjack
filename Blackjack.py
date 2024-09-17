import random
def tenercartas():
    cartasowo = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    return random.choice(cartasowo)

def calcularpuntaje(cartasowo):
    valor = sum(cartasowo)
    if valor > 21 and 11 in cartasowo:
        for i in range(len(cartasowo)):
            if cartasowo[i] == 11:
                cartasowo[i] = 1
                valor = sum(cartasowo)
                break
    return valor

def juego21():
    print("¡Hola! Bienvenido al juego Blackjack ¿estás listo para comenzar?")
    cartasP1 = []
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

    puntajecasa = random.randint(17, 26)
    puntajeP1 = calcularpuntaje(cartasP1)

    print(f"Te has detenido al tener un puntaje de {puntajeP1}")
    print(f"La casa tiene un puntaje de {puntajecasa}")

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


''' Aun no lo termino, me falta el readme y quiero acompletarlo con lo de hacer 
las funciones a parte y otras cositas, también el explicar todo :('''

