from black_jack_functions import *
import random

# Crear archivo .txt para bitácora de acciones
dir_bitacora = crear_bitacora()


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

baraja = crear_baraja(dir_bitacora)
print_baraja(baraja, dir_bitacora)

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

    msj_bitacora = f"\n\nSe ha iniciado un juego nuevo - Ronda No.{ronda}.\n"
    agregar_accion_bitacora(dir_bitacora, msj_bitacora)

    cant_zeros = baraja.count(0)

    total_J1 = 0
    total_J2 = 0

    if cant_zeros <= 48:
        #Parte del jugador 1
        data_J1 = play_J1(baraja, dir_bitacora)
        print("Total: {}".format(data_J1["total_mano_J1"]))
        # print("Total: " + str(data_J1["total_mano_J1"])) - Qué es la diferencia o ventaja entre una y otra?
        baraja = data_J1["baraja_actual"]
        total_J1 = data_J1["total_mano_J1"]
        cant_zeros = baraja.count(0)

        if total_J1 <= 20:
            extra = input("Jugador 1 decida - 1: Entra   2: Se queda\n")
            if extra == '1':

                msj_bitacora = f"El {jug1} ha solicitado una carta adicional.\n"
                agregar_accion_bitacora(dir_bitacora, msj_bitacora)

                cant_zeros = baraja.count(0)
                
                if cant_zeros <= 49:
                    data_J1 = jugar_extra_1(data_J1, dir_bitacora)
                    print("Total: {}".format(data_J1["total_mano_J1"]))
                    baraja = data_J1["baraja_actual"]
                    cant_zeros = baraja.count(0)
                else: 
                    print("No es posible jugar la carta extra. Quedan solamente " + str((52-cant_zeros)) + " cartas disponibles para el " + jug2 +".\n")

        #Parte del jugador 2 - Máquina
        data_J2 = play_J2(baraja, dir_bitacora)
        print("Total: {}".format(data_J2["total_mano_J2"]))
        baraja = data_J2["baraja_actual"]
        total_J2 = data_J2["total_mano_J2"]
        cant_zeros = baraja.count(0)

        while total_J2 > 0 and total_J2 <= 9:
            data_J2 = jugar_extra_2(data_J2, dir_bitacora)
            print("Total: {}".format(data_J2["total_mano_J2"]))
            baraja = data_J2["baraja_actual"]
            cant_zeros = baraja.count(0)
            
            msj_bitacora = f"El {jug2} ha solicitado una carta adicional.\n"
            agregar_accion_bitacora(dir_bitacora, msj_bitacora)

        while total_J2 > 9 and total_J2 <= 14 and total_J1 > 14 and total_J2 <= 21:
            data_J2 = jugar_extra_2(data_J2, dir_bitacora)
            total_J2 += data_J2["total_mano_J2"]
            print("Total: {}".format(data_J2["total_mano_J2"]))
            baraja = data_J2["baraja_actual"]
            cant_zeros = baraja.count(0)
            
            msj_bitacora = f"El {jug2} ha solicitado una carta adicional.\n"
            agregar_accion_bitacora(dir_bitacora, msj_bitacora)
        
        if total_J2 > 14 and total_J2 < 21 and total_J1 <= 21:
            valor_random = random_boolean()

            if valor_random == True:
                data_J2 = jugar_extra_2(data_J2, dir_bitacora)
                print("Total: {}".format(data_J2["total_mano_J2"]))
                baraja = data_J2["baraja_actual"]
                cant_zeros = baraja.count(0)
                
                msj_bitacora = f"El {jug2} ha solicitado una carta adicional.\n"
                agregar_accion_bitacora(dir_bitacora, msj_bitacora)

            else:
                msj_bitacora = f"El {jug2} ha decidido no solicitar mas cartas.\n"
                agregar_accion_bitacora(dir_bitacora, msj_bitacora)


        totales = total_pts(data_J1["total_mano_J1"], data_J2["total_mano_J2"])
        puntos_J1 = totales['pts_J1']
        puntos_J2 = totales['pts_J2']
        
        msj_bitacora = f"Información de puntos:\n      * Puntos del {jug1}: {puntos_J1}\n      * Puntos del {jug2}: {puntos_J2}\n"
        agregar_accion_bitacora(dir_bitacora, msj_bitacora)

        print
        print(f"\n- Puntos de la mano del jugador 1: {puntos_J1}")
        print(f"- Puntos de la mano del jugador 2: {puntos_J2}\n")

        defect_val = True
        while defect_val == True:
            
            opcion_salida = input("Desea continuar el juego? 1. Si   2. No\n")

            if opcion_salida == "1":
                salida_juego = False
                defect_val = False
                
                msj_bitacora = f"El {jug1} ha decidido continuar con el juego.\n"
                agregar_accion_bitacora(dir_bitacora, msj_bitacora)

            elif opcion_salida == "2":
                salida_juego = True
                defect_val = False
                
                msj_bitacora = f"El {jug1} ha decidido terminar el juego.\n"
                agregar_accion_bitacora(dir_bitacora, msj_bitacora)

            elif opcion_salida == "!" or opcion_salida == "@" or opcion_salida == "#" or opcion_salida == "$" or opcion_salida == "%" or opcion_salida == "^" or opcion_salida == "&" or opcion_salida == "*":
                salida_juego = True
                defect_val = False
                print_baraja(baraja)
                print("")
                
                msj_bitacora = f"El {jug1} ha solicitado mostrar la baraja del juego actual.\n"
                agregar_accion_bitacora(dir_bitacora, msj_bitacora)
            
            else:
                defect_val = True
                print("\nValor incorrecto! Trate nuevamente.")
                
                msj_bitacora = f"El {jug1} ha ingresado un valor incorrecto en la decisión de continuar o no con el juego.\n"
                agregar_accion_bitacora(dir_bitacora, msj_bitacora)

        total_pts_J1 += puntos_J1
        total_pts_J2 += puntos_J2
    
    else:
        if cant_zeros == 50 or cant_zeros <= 49:
            data_J1 = jugar_extra_1(data_J1)
            print("Total: {}".format(data_J1["total_mano_J1"]))

            data_J2 = jugar_extra_2(data_J2)
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
            # Este bloque de "else" lleva implícito que pasa cuando quedan una o 2 cartas.
            total_pts_J1 += 0
            total_pts_J2 += 0
            print("No quedan mas cartas en la baraja. Inicie un nuevo juego. Gracias, chao!")
            msj_bitacora = f"El juego se ha quedado sin cartas en la baraja y ha finalizado.\n"
            agregar_accion_bitacora(dir_bitacora, msj_bitacora)

            salida_juego = True
            
    ronda += 1

print(f"\nInformación del puntaje:\n- Puntos del {jug1}: {total_pts_J1}")
print(f"- Puntos del {jug2}: {total_pts_J2}")

cartas_rest = 52 - cant_zeros
print(f"\n- Cantidad de zeros: {cant_zeros}")
print(f"- Total de cartas restantes: {cartas_rest}")
print("\nBaraja actual:\n")
print_baraja(data_J2["baraja_actual"])

msj = obtener_resultado(total_pts_J1, total_pts_J2, dir_bitacora)

msj_bitacora = f"Este es el último mensaje en la bitácora, el juego ha finalizado!\n"
agregar_accion_bitacora(dir_bitacora, msj_bitacora)

print("")
print(msj)
print("")