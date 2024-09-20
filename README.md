# Blackjack
# Juego de Blackjack en Python

Este es un simple juego de Blackjack que se ejecuta en la consola, donde el jugador compite contra la casa. El jugador puede solicitar cartas hasta que decida detenerse o hasta que se pase de 21.

## Reglas del Juego

1. El jugador comienza con un conjunto de cartas vacío.
2. Se le pregunta al jugador si desea quedarse con las cartas que tiene o si solicita una nueva carta.
3. Si el jugador solicita una carta, se genera aleatoriamente una carta de una baraja y se agrega a su conjunto.
4. Después de cada nueva carta, se muestra el valor total de las cartas del jugador.
   - Las cartas numéricas tienen su valor correspondiente.
   - J, Q, K valen 10 puntos.
   - El As (A) vale 11, pero si el jugador se pasa de 21, el As puede contar como 1.
5. El jugador sigue solicitando cartas hasta que decida detenerse o se pase de 21.
6. Una vez que el jugador se detiene, se genera un número aleatorio entre 17 y 26 que representa el valor de la casa.
7. El jugador gana si:
   - Obtiene un 21 y la casa tiene un número menor.
   - La casa se pasa de 21 y el jugador tiene un número menor o igual a 21.
   - Ambos tienen un número menor o igual a 21, pero el jugador tiene un número más alto.
8. El jugador pierde si:
   - Se pasa de 21.
   - La casa tiene un valor mayor y menor o igual a 21.
9. En caso de empate:
   - Si ambos tienen el mismo valor y menos de 21, gana quien tenga menos cartas.
   - Si ambos se pasan de 21, es un empate.

### Forma de definir al ganador
_El jugador gana cuando:_
* El jugador obtiene un 21 y la casa obtiene un número menor.
* La casa obtiene un número mayor a 21 y el jugador obtiene un número menor o igual que 21.
* El jugador y la casa obtienen un número menor o igual a 21, pero el jugador obtiene un número más alto.
* El jugador y la casa obtienen el mismo número, siendo este un número menor o igual a 21, pero el jugador lo hace con menos cartas.

_Hay empate cuando:_
* Ambos obtienen un número mayor a 21
* Ambos obtienen un número menor o igual a 21, con el mismo número de cartas
En caso contrario a los anteriores, el jugador pierde.

### Estructura del código

_El código se compone de las siguientes funciones:_
 tenercartas() : Genera una carta aleatoria de un mazo y la retorna.
calcularpuntaje(cartasowo): Calcula el puntaje total de las cartas del jugador, ajustando el valor del As si es necesario.
juego21(): Función principal que controla la lógica del juego.

### Notas adicionales
* El valor de las cartas de la casa se genera aleatoriamente entre 17 y 26, simulando el comportamiento de la banca en el Blackjack.
* El juego está diseñado para ser simple y didáctico, ideal para quienes están aprendiendo a programar en Python y desean implementar un proyecto divertido.

_Ejemplificación de la partida en ejecución._
* La manera en la que se muestra una partida es la siguiente:

´´´
¡Hola! Bienvenido al juego Blackjack ¿estás listo para comenzar?
¿Quieres una carta? owo -pon 'si' o 'no'- sí
Lo que ingresaste es incorrecto, responde 'si' o 'no'
¿Quieres una carta? owo -pon 'si' o 'no'- si
Obtuviste un 6.
Tus cartas son: [6]
Tu puntaje es de: 6
¿Quieres una carta? owo -pon 'si' o 'no'- si
Obtuviste un 4.
Tus cartas son: [6, 4]
Tu puntaje es de: 10
¿Quieres una carta? owo -pon 'si' o 'no'- si
Obtuviste un 7.
Tus cartas son: [6, 4, 7]
Tu puntaje es de: 17
¿Quieres una carta? owo -pon 'si' o 'no'- no
Te has detenido al tener un puntaje de 17
La casa tiene un puntaje de 25
La casa superó los 21 puntos ¡Has ganado! :D

´´´

El ciclo se repite hasta comprobar un ganador.

## Autor
* **Melanie Irigoyen** - Universidad Palmore - materia: programación 2

## Fecha 
* 19/septiembre/2024.

