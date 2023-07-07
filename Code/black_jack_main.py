from black_jack_functions import *
import random

# Inicialización de Variables

# Listas
cartas_J1 = []
cartas_J2 = []
baraja_actual = []

# Diccionarios
data_J1 = {}
data_J2 = {}

# Primitivos
ciclo_juego = True
total_J1 = 0
total_J2 = 0
puntos_J1 = 0
puntos_J2 = 0
jug1 = "Jugador 1"
jug2 = "Jugador 2"

baraja = crear_baraja()
print_baraja(baraja)

print("\nBienvenido al Juego del siglo - BlackJack!!\n")
input("Presione enter para iniciar")

# Variables para ciclo de rondas de juego
# rondas_de_juego = 1 #Contador de rondas
# sumatoria_total_J1 = 0
# sumatoria_total_J2 = 0

#Parte del jugador 1
data_J1 = play_J1(baraja)
print("Total: {}".format(data_J1["total_J1"]))
baraja_actual = data_J1["baraja_actual"]

#Parte del jugador 2
data_J2 = play_J2(baraja_actual)
print("Total: {}".format(data_J2["total_J2"]))
baraja_actual = data_J2["baraja_actual"]

totales = total_pts(data_J1["total_J1"], data_J2["total_J2"])
print("\nPuntos obtenidos de jugador1: "+str(totales['total_J1']))
print("Puntos obtenidos de jugador2: "+str(totales['total_J2'])+"\n")

print_baraja(baraja_actual)
# sumatoria_total_J1 += totales['total_J1']
# sumatoria_total_J2 += totales['total_J2']
# rondas_de_juego += 1

print_baraja(baraja)
print("")