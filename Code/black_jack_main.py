from black_jack_functions import *
import random

# Inicialización de Variables

# Diccionarios
data_J1 = {}
data_J2 = {}

# Primitivos
total_J1 = 0
puntos_J1 = 0
puntos_J2 = 0
jug1 = "Jugador 1"
jug2 = "Jugador 2"

baraja = crear_baraja()
print_baraja(baraja)

print("\nBienvenido al Juego del siglo - BlackJack!!\n")

# Variables para ciclo de rondas de juego
cant_zeros = 0
salida_juego = False
total_pts_J1 = 0
total_pts_J2 = 0
ronda = 1

while salida_juego == False:

    print(f"\nRonda #{ronda}")
    input("Presione enter para iniciar\n")

    cant_zeros = baraja.count(0)

    if cant_zeros <= 48:
        #Parte del jugador 1
        data_J1 = play_J1(baraja)
        print("Total: {}".format(data_J1["total_mano_J1"]))
        baraja = data_J1["baraja_actual"]
        total_J1 = data_J1["total_mano_J1"]

        if total_J1 <= 20:
            extra = input("Jugador 1 decida - 1: Entra   2: Se queda\n")
            if extra == '1':

                cant_zeros = baraja.count(0)
                
                if cant_zeros <= 49:
                    data_J1 = jugar_extra(data_J1)
                    print("Total: {}".format(data_J1["total_mano_J1"]))
                    baraja = data_J1["baraja_actual"]
                else: 
                    print("No es posible jugar la carta extra. Quedan solamente " + str((52-cant_zeros)) + " cartas disponibles para el " + jug2 +".\n")

        #Parte del jugador 2 - Máquina
        data_J2 = play_J2(baraja)
        print("Total: {}".format(data_J2["total_mano_J2"]))
        baraja = data_J2["baraja_actual"]

        totales = total_pts(data_J1["total_mano_J1"], data_J2["total_mano_J2"])
        puntos_J1 = totales['pts_J1']
        puntos_J2 = totales['pts_J2']
        print(f"\n- Puntos de la mano del jugador 1: {puntos_J1}")
        print(f"- Puntos de la mano del jugador 2: {puntos_J2}\n")

        defect_val = True
        while defect_val == True:
            
            opcion_salida = input("Desea continuar el juego? 1. Si   2. No\n")

            if opcion_salida == "1":
                salida_juego = False
                defect_val = False

            elif opcion_salida == "2":
                salida_juego = True
                defect_val = False

            elif opcion_salida == "!" or opcion_salida == "@" or opcion_salida == "#" or opcion_salida == "$" or opcion_salida == "%" or opcion_salida == "^" or opcion_salida == "&" or opcion_salida == "*":
                salida_juego = True
                defect_val = False
                print_baraja(baraja)
                print("")
            
            else:
                defect_val = True
                print("\nValor incorrecto! Trate nuevamente.")

        total_pts_J1 += puntos_J1
        total_pts_J2 += puntos_J2
    
    else:
        if cant_zeros == 50 or cant_zeros <= 49:
            data_J1 = jugar_extra(data_J1)
            print("Total: {}".format(data_J1["total_mano_J1"]))

            data_J2 = jugar_extra(data_J2)
            print("Total: {}".format(data_J2["total_mano_J2"]))


            totales = total_pts(data_J1["total_mano_J1"], data_J2["total_mano_J2"])
            puntos_J1 = totales['pts_J1']
            puntos_J2 = totales['pts_J2']

            total_pts_J1 += puntos_J1
            total_pts_J2 += puntos_J2

            print(f"\n- Puntos de la mano del jugador 1: {puntos_J1}")
            print(f"- Puntos de la mano del jugador 2: {puntos_J2}\n")

            salida_juego = True
        
        else:
            total_pts_J1 += 0
            total_pts_J2 += 0
            print("No quedan mas cartas en la baraja. Inicie un nuevo juego. Gracias, chao!")
            salida_juego = True
            
    
    ronda += 1

print(f"\n- Puntos del {jug1}: {total_pts_J1}")
print(f"- Puntos del {jug2}: {total_pts_J2}")

msj = obtener_resultado(total_pts_J1, total_pts_J2)

print("")
print(msj)
print("")