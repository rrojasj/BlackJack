from black_jack_functions import *
import random

baraja = ["A's \u2665", "A's \u2666", "A's \u2663", "A's \u2660",
    "2 \u2665", "2 \u2666", "2 \u2663", "2 \u2660",
    "3 \u2665", "3 \u2666", "3 \u2663", "3 \u2660",
    "4 \u2665", "4 \u2666", "4 \u2663", "4 \u2660",
    "5 \u2665", "5 \u2666", "5 \u2663", "5 \u2660",
    "6 \u2665", "6 \u2666", "6 \u2663", "6 \u2660",
    "7 \u2665", "7 \u2666", "7 \u2663", "7 \u2660",
    "8 \u2665", "8 \u2666", "8 \u2663", "8 \u2660",
    "9 \u2665", "9 \u2666", "9 \u2663", "9 \u2660",
    "10 \u2665", "10 \u2666", "10 \u2663", "10 \u2660",
    "J \u2665", "J \u2666", "J \u2663", "J \u2660",
    "Q \u2665", "Q \u2666", "Q \u2663", "Q \u2660",
    "K \u2665", "K \u2666", "K \u2663", "K \u2660"]

cartasJugador1 = []
cartasJugador2 = []
totalJugador1 = 0
totalJugador2 = 0
puntosJugador1 = 0
puntosJugador2 = 0

flag = True

print("Black jack")
print("")


#Parte del jugador 1
while flag:
    cartaAleatoria = random.randint(0,51)
    if baraja[cartaAleatoria] == 0:
        ""
    else:
        cartasJugador1.append(baraja[cartaAleatoria])
        baraja[cartaAleatoria] = 0
        
    if len(cartasJugador1) == 2:
        flag = False

print("Jugador 1")
print("Sus cartas son '{}' y '{}'".format(cartasJugador1[0], cartasJugador1[1]))
for i in range(2):
    valorActual = cartasJugador1[i][0]
    if valorActual in ["J","Q", "K", "1"]:
        totalJugador1 += 10
    elif valorActual == "A":
        decicion = input("Qué valor desea darle al As, 1 o 11?\n")
        if decicion == "1":
            totalJugador1 += 1
        elif decicion == "11":
            totalJugador1 += 11
    else:
        totalJugador1 += int(valorActual)
print("Total: {}".format(totalJugador1))


#Parte del jugador 2
flag = True
print("")
while flag:
    cartaAleatoria = random.randint(0,51)
    if baraja[cartaAleatoria] == 0:
        ""
    else:
        cartasJugador2.append(baraja[cartaAleatoria])
        baraja[cartaAleatoria] = 0
    if len(cartasJugador2) == 2:
        flag = False

print("Jugador 2")
print("Sus cartas son '"+cartasJugador2[0]+"' y '"+cartasJugador2[1])
for i in range(2):
    valorActual =cartasJugador2[i][0]
    if valorActual in ["J","Q", "K", "1"]:
        totalJugador2 += 10
    elif valorActual == "A":
        decicion = input("Qué valor desea darle al As, 1 o 11?\n")
        if decicion == "1":
            totalJugador2 += 1
        elif decicion == "11":
            totalJugador2 += 11
    else:
        totalJugador2 += int(valorActual)


print("Total: {}".format(totalJugador2))

if totalJugador1 == 21:
    if totalJugador2 == 21:
        puntosJugador1 += 3
        puntosJugador2 += 3
    else:
        puntosJugador1 += 6
elif totalJugador1 >= 17 and totalJugador1 <= 20:
    if totalJugador1 > totalJugador2:
        puntosJugador1 += 2
elif totalJugador1 < 17:
    if totalJugador1 > totalJugador2:
        puntosJugador1 += 1
elif totalJugador1 > 21:
    puntosJugador1 += 0

if totalJugador2 == 21:
    if totalJugador1 == 21:
        puntosJugador2 += 3
    else:
        puntosJugador2 += 6
elif totalJugador2 >= 17 and totalJugador2 <= 20:
    if totalJugador2 > totalJugador1:
        puntosJugador2 += 2
elif totalJugador2 < 17:
    if totalJugador2 > totalJugador1:
        puntosJugador2 += 1
elif totalJugador2 > 21:
    puntosJugador2 += 0

print("")
print("Puntos obtenidos de jugador1: "+str(puntosJugador1))
print("Puntos obtenidos de jugador2: "+str(puntosJugador2))







