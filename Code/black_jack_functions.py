import random
import os
from datetime import datetime

jug1 = "Jugador 1"
jug2 = "Jugador 2"

def crear_baraja() -> list:
    """
    función: crear_baraja()
    descripción: Crea la baraja con todos sus valores
    params: none
    """
    baraja = [
    "2", "2", "2", "2",
    "3", "3", "3", "3",
    "4", "4", "4", "4",
    "5", "5", "5", "5",
    "6", "6", "6", "6",
    "7", "7", "7", "7",
    "8", "8", "8", "8",
    "9", "9", "9", "9",
    "10", "10", "10", "10",
    "J", "J", "J", "J",
    "Q", "Q", "Q", "Q",
    "K", "K", "K", "K",
    "A", "A", "A", "A"]

    return baraja

def print_baraja(baraja: list):
    """
    función: print_baraja()
    descripción: Imprime la baraja con sus elementos actuales
    params: baraja
    """
    for i in range(0, len(baraja), 4):

        print(', '.join(map(str, baraja[i:i+4]))) # With this option "map" converts each element to a string
        #  print(', '.join(baraja[i:i+4])) - This option reads only the strings

def convert_ace(mano_jug:list, jugador: str, dir_bitacora: str) -> list:
    """
    función: convert_as()
    descripción: Convierte el valor actual de la mano en el valor que indique el usuario
    params: mano_J1
    """
    for index in range(len(mano_jug)):
        if mano_jug[index] == "A":
            decision = input("Qué valor desea darle al As, 1 o 11?\n")

            if decision == "1":
                mano_jug[index] = 1
            elif decision == "11":
                mano_jug[index] = 11
    
    msj_bitacora = f"{jugador} le ha dado el valor de {mano_jug[index]} a su A's"
    agregar_accion_bitacora(dir_bitacora, msj_bitacora)
    
    return mano_jug
        
def sumar_mano(mano_jugador:list) -> int:
    """
    función: sumar_mano()
    descripción: Suma los valores que contiene la mano del jugador
    params: mano_jugador
    """
    total_mano = 0

    for i in range(len(mano_jugador)):
        valor_actual = mano_jugador[i]
        if valor_actual in ["J","Q","K","1"]:
            total_mano += 10
        # elif valor_actual == "A":
        #     valor_as = convert_ace(valor_actual)
        #     total_mano += valor_as
        else:
            total_mano += int(valor_actual)
    
    return total_mano

def print_mano(jugador:str, mano_jugador:list): 
    """
    función: print_mano()
    descripción: Imprime el mensaje con la mano del jugador
    params: jugador, mano_jugador
    """
    cont = 1
    print(f"\nCartas del {jugador}:")
    for i in range(len(mano_jugador)):
        print(f"{cont}: {mano_jugador[i]}")
        cont += 1
    print("")

def calcular_pts_individuales(total_jug, total_adv):

    bj = 21
    pts_won = 0

    if total_jug == bj:
        if total_adv == bj:
            pts_won = 3
        else:
            pts_won = 6
    else:
        if total_jug >= 17 and total_jug <= 20:
            if total_adv > 21:
                pts_won = 2
            elif total_jug > total_adv:
                pts_won = 2
        else:
            if total_jug < 17:
                if total_jug > total_adv:
                    pts_won = 1
            else:
                if total_jug > bj:
                    pts_won = 0
    return pts_won

def total_pts(total_J1:int, total_J2:int) -> dict:
    """
    función: total_pts()
    descripción: Imprime el mensaje con la mano del jugador
    params: jugador, mano_jugador
    """

    puntos_J1 = calcular_pts_individuales(total_J1, total_J2)
    puntos_J2 = calcular_pts_individuales(total_J2, total_J1)

    totales = {
        'pts_J1': puntos_J1,
        'pts_J2': puntos_J2
        }
    
    return totales

def play_J1(baraja: list, dir_bitacora: str) -> dict:
    """
    función: play_J1()
    descripción: Proceso de juego de una mano del Jugador 1 
    params: baraja
    """
    play_in = True
    data_J1 = {}
    mano_J1 = []
    total = 0
    baraja_actual = baraja
    jug1 = "Jugador 1"

    while play_in:
        carta_aleatoria = random.randint(0,51)
        if baraja_actual[carta_aleatoria] != 0:
            mano_J1.append(baraja_actual[carta_aleatoria])

            if carta_aleatoria in ["J", "Q", "K"]:
                # msj_bitacora = jug1 + " - Carta: " + str(baraja_actual[carta_aleatoria]) + "y su valor es '10'.\n"
                msj_bitacora = f"{jug1} - Carta: '{baraja_actual[carta_aleatoria]}' y su valor es '10'.\n" 
                agregar_accion_bitacora(dir_bitacora, msj_bitacora)
            else:
                # msj_bitacora = msj_bitacora = jug1 + " - Carta: " + str(baraja_actual[carta_aleatoria]) + "y su valor es" + str(baraja_actual[carta_aleatoria])+".\n"

                msj_bitacora = f"{jug1} - Carta: '{baraja_actual[carta_aleatoria]}' y su valor es '{baraja_actual[carta_aleatoria]}.'\n" 
                agregar_accion_bitacora(dir_bitacora, msj_bitacora)
            
            baraja_actual[carta_aleatoria] = 0
        
        if len(mano_J1) == 2:
            play_in = False

    print_mano(jug1, mano_J1)

    # Verifica si existen A's y si es verdadero reemplaza el valor por el que indique el usuario
    cant_ace = mano_J1.count("A")
    if cant_ace >= 1:
        mano_J1 = convert_ace(mano_J1, jug1, dir_bitacora)

    total = sumar_mano(mano_J1)
    msj_bitacora = f"La mano del {jug1} suma un total de {total}\n"
    agregar_accion_bitacora(dir_bitacora, msj_bitacora)

    data_J1 = {
        "total_mano_J1": total,
        "baraja_actual": baraja_actual,
        "mano_J1": mano_J1
    }

    return data_J1

def play_J2(baraja: list, dir_bitacora: str) -> dict:
    """
    función: play_J2()
    descripción: Proceso de juego de una mano del Jugador 2
    params: baraja
    """
    play_in = True
    data_J2 = {}
    mano_J2 = []
    total = 0
    baraja_actual = baraja
    jug2 = "Jugador 2"
    cant_zeros = baraja.count(0)

    while play_in:
        carta_aleatoria = random.randint(0,51)
        if baraja_actual[carta_aleatoria] == 0:
            ""
        else:
            mano_J2.append(baraja_actual[carta_aleatoria])
            
            if carta_aleatoria in ["J", "Q", "K"]:
                msj_bitacora = f"{jug2} - Carta: '{baraja_actual[carta_aleatoria]}' y su valor es '10'.\n" 

                agregar_accion_bitacora(dir_bitacora, msj_bitacora)
            else:
                msj_bitacora = f"{jug2} - Carta: '{baraja_actual[carta_aleatoria]}' y su valor es '{baraja_actual[carta_aleatoria]}.'\n" 
                agregar_accion_bitacora(dir_bitacora, msj_bitacora)

            baraja_actual[carta_aleatoria] = 0
        
        if len(mano_J2) == 2:
            play_in = False

    print_mano(jug2, mano_J2) 

    # Verifica si existen A's y si es verdadero reemplaza el valor por el que indique el usuario
    cant_aces = mano_J2.count('A')
    if cant_aces >= 1:
        mano_J2 = convert_ace(mano_J2, jug2, dir_bitacora)

    total = sumar_mano(mano_J2)
    msj_bitacora = f"La mano del {jug2} suma un total de {total}\n"
    agregar_accion_bitacora(dir_bitacora, msj_bitacora)

    data_J2 = {
        "total_mano_J2": total,
        "baraja_actual": baraja_actual,
        "mano_J2": mano_J2
    }
    baraja_actual = data_J2["baraja_actual"]

    return data_J2

def jugar_extra_1(dict_J1:dict, dir_bitacora: str) -> dict:
    """
    función: jugar_extra_1()
    descripción: Jugar una carta extra del jugador 1
    params: dict_J1
    """
    baraja_actual = dict_J1["baraja_actual"]
    carta_aleatoria = random.randint(0,51)

    data_J1 = []

    mano_J1 = dict_J1["mano_J1"]

    if dict_J1["baraja_actual"][carta_aleatoria] == 0:
        ""
    else:
        mano_J1.append(dict_J1["baraja_actual"][carta_aleatoria])
        baraja_actual[carta_aleatoria] = 0
        print_mano(jug1, mano_J1)

        cant_ace = mano_J1.count("A")
        if cant_ace >= 1:
            mano_J1 = convert_ace(mano_J1, jug1, dir_bitacora)

        total = sumar_mano(mano_J1)
        data_J1 = {
            "total_mano_J1": total,
            "baraja_actual": baraja_actual,
            "mano_J1": mano_J1
    }  
    return data_J1

def jugar_extra_2(dict_J2:dict, dir_bitacora: str) -> dict:
    """
    función: jugar_extra_1()
    descripción: Jugar una carta extra del jugador 1
    params: dict_J2
    """
    baraja_actual = dict_J2["baraja_actual"]
    carta_aleatoria = random.randint(0,51)

    data_J2 = []

    mano_J2 = dict_J2["mano_J2"]

    if dict_J2["baraja_actual"][carta_aleatoria] == 0:
        ""
    else:
        mano_J2.append(dict_J2["baraja_actual"][carta_aleatoria])
        baraja_actual[carta_aleatoria] = 0
        print_mano(jug2, mano_J2)

        cant_ace = mano_J2.count("A")
        if cant_ace >= 1:
            mano_J2 = convert_ace(mano_J2, jug2, dir_bitacora)

        total = sumar_mano(mano_J2)
        data_J2 = {
            "total_mano_J2": total,
            "baraja_actual": baraja_actual,
            "mano_J2": mano_J2
    }  
    return data_J2

def obtener_resultado(total_pts_J1:int, total_pts_J2:int, dir_bitacora:str) -> str:
    """
    función: obtener_resultado()
    descripción: Función para obtener el mensaje de acuerdo al resultado obtenido
    params: total_pts_J1, total_pts_J2
    """
    msj = ""
    if total_pts_J1 == total_pts_J2:
        msj = "Esto es un empate"
        msj_bitacora = f"El {jug1} y el {jug2} han empatado!\n"

    else:
        if total_pts_J1 > total_pts_J2:
            msj = f"Ganador del juego: {jug1}"
            msj_bitacora = f"El {jug1} ha ganado y el {jug2} perdió el juego!\n"
        else:
            msj = f"Ganador del juego: {jug2}"
            msj_bitacora = f"El {jug2} ha ganado y el {jug1} perdió el juego!\n"

    agregar_accion_bitacora(dir_bitacora, msj_bitacora)

    return msj

def random_boolean() -> bool:
    """
    función: random_boolean()
    descripción: Función para obtener un valor aleatorio de True o False
    params: N/A
    """
    random_num = random.random()

    return random_num <= 0.4

def crear_bitacora() -> str:
    """
    función: random_boolean()
    descripción: Función para obtener un valor aleatorio de True o False
    params: N/A
    """
    directory = "/Users/robjimn/Documents/Roberto Rojas/Cenfotec/Principios Programación/Proyecto/bitacora"

    tiempo_actual = datetime.now()

    # Crear String de timestamp
    timestamp_str = tiempo_actual.strftime("%d%m%Y_%H%M%S")

    file_name = f"Blackjack_Bitácora_{timestamp_str}.txt"

    file_path = os.path.join(directory, file_name)

    with open(file_path, "w") as file:
        file.write(f"Bitácora: {tiempo_actual}\nPD: Las horas se muestran en formato de 24 horas\n")

    return file_path

def agregar_accion_bitacora(dir_bitacora, msj_bitacora):

    ta = datetime.now()
    formatted_time = ta.strftime("%I:%M:%S %p")
    msj_completo = f"- {formatted_time} - {msj_bitacora}\n"

    with open(dir_bitacora, "a") as file:
        file.write(msj_completo)


# /Users/robjimn/Documents/Roberto Rojas/Cenfotec/Principios Programación/Proyecto/bitacora

# -- FUNCIONES DE PRUEBAS

# def crear_baraja() -> list:
#     """
#     función: crear_baraja() -- PRUEBAS
#     descripción: Crea la baraja con todos sus valores
#     params: none
#     """
#     # baraja = [
#     # "2", "2", "2", "2",
#     # "3", "3", "3", "3",
#     # "4", "4", "4", "4",
#     # "5", "5", "5", "5",
#     # "6", "6", "6", "6",
#     # "7", "7", "7", "7",
#     # "8", "8", "8", "8",
#     # "9", "9", "9", "9",
#     # "10", "10", "10", "10",
#     # "J", "J", "J", "J",
#     # "Q", "Q", "Q", "Q",
#     # "K", "K", "K", "K",
#     # "A", "A", "A", "A"]

#     # Baraja de prueba
#     baraja = [
#     0, 0, 0, "2",
#     0, 0, 0, 0,
#     0, 0, 0, 0,
#     0, 0, "5", 0,
#     0, 0, 0, 0,
#     0, 0, 0, 0,
#     "8", 0, 0, 0,
#     0, 0, 0, 0,
#     0, 0, 0 ,0,
#     0, 0, 0, 0,
#     0, "Q", 0, 0,
#     0, 0, 0, 0,
#     0, 0, 0, 0]

#     return baraja