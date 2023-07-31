import random

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

def print_baraja(baraja):
    """
    función: print_baraja()
    descripción: Imprime la baraja con sus elementos actuales
    params: baraja
    """
    for i in range(0, len(baraja), 4):
     print(', '.join(baraja[i:i+4]))

def convert_ace(mano_jug:list) -> list:
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
        #     valor_as = convert_as(valor_actual)
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

def total_pts(total_J1:int, total_J2:int) -> dict:
    """
    función: total_pts()
    descripción: Imprime el mensaje con la mano del jugador
    params: jugador, mano_jugador
    """
    puntos_J1 = 0
    puntos_J2 = 0
    totales = {}

    # Puntos - Jugador 1
    if total_J1 == 21:
        if total_J2 == 21:
            puntos_J1 += 3
            puntos_J2 += 3
        else:
            puntos_J1 += 6
    elif total_J1 >= 17 and total_J1 <= 20:
        if total_J1 > total_J2:
            puntos_J1 += 2
    elif total_J1 < 17:
        if total_J1 > total_J2:
            puntos_J1 += 1
    elif total_J1 > 21:
        puntos_J1 += 0
        puntos_J2 += 6
    
    # Puntos - Jugador 2
    if total_J2 == 21:
        if total_J1 == 21:
            puntos_J2 += 3
            puntos_J1 += 3
        else:
            puntos_J2 += 6
    elif total_J2 >= 17 and total_J2 <= 20:
        if total_J2 > total_J1:
            puntos_J2 += 2
    elif total_J2 < 17:
        if total_J2 > total_J1:
            puntos_J2 += 1
    elif total_J2 > 21:
        puntos_J2 += 0
        puntos_J1 += 6

    totales = {
        'pts_J1': puntos_J1,
        'pts_J2': puntos_J2
        }
    
    return totales

def play_J1(baraja) -> dict:
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
            baraja_actual[carta_aleatoria] = 0
        
        if len(mano_J1) == 2:
            play_in = False

    print_mano(jug1, mano_J1)

    # Verifica si existen A's y si es verdadero reemplaza el valor por el que indique el usuario
    cant_ace = mano_J1.count("A")
    if cant_ace >= 1:
        mano_J1 = convert_ace(mano_J1)

    total = sumar_mano(mano_J1)
    data_J1 = {
        "total_mano_J1": total,
        "baraja_actual": baraja_actual,
        "mano_J1": mano_J1
    }

    return data_J1

def play_J2(baraja) -> dict:
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

    while play_in:
        carta_aleatoria = random.randint(0,51)
        if baraja_actual[carta_aleatoria] == 0:
            ""
        else:
            mano_J2.append(baraja_actual[carta_aleatoria])
            baraja_actual[carta_aleatoria] = 0
        
        if len(mano_J2) == 2:
            play_in = False

    print_mano(jug2, mano_J2) 

    # Verifica si existen A's y si es verdadero reemplaza el valor por el que indique el usuario
    cant_aces = mano_J2.count('A')
    if cant_aces >= 1:
        mano_J2 = convert_ace(mano_J2)

    total = sumar_mano(mano_J2)
    data_J2 = {
        "total_mano_J2": total,
        "baraja_actual": baraja_actual,
        "mano_J2": mano_J2
    }
    baraja_actual = data_J2["baraja_actual"]

    return data_J2

def jugar_extra(dict_J1:dict) -> dict:

    """
    función: jugar_extra()
    descripción: 
    params: baraja
    """
    baraja_actual = dict_J1["baraja_actual"]
    carta_aleatoria = random.randint(0,51)

    mano_J1 = dict_J1["mano_J1"]

    if dict_J1["baraja_actual"][carta_aleatoria] == 0:
        ""
    else:
        mano_J1.append(dict_J1["baraja_actual"][carta_aleatoria])
        baraja_actual[carta_aleatoria] = 0
        print_mano(jug1, mano_J1)

        cant_ace = mano_J1.count("A")
        if cant_ace >= 1:
            mano_J1 = convert_ace(mano_J1)

        total = sumar_mano(mano_J1)
        data_J1 = {
            "total_mano_J1": total,
            "baraja_actual": baraja_actual,
            "mano_J1": mano_J1
    }  
    return data_J1

def obtener_resultado(total_pts_J1:int, total_pts_J2:int) -> str:
    msj = ""
    if total_pts_J1 == total_pts_J2:
        msj = "Esto es un empate"
    else:
        if total_pts_J1 > total_pts_J2:
            msj = f"Ganador del juego: {jug1}"
        else:
            msj = f"Ganador del juego: {jug2}"

    return msj

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