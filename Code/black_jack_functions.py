import random

jug1 = "Jugador 1"
jug2 = "Jugador 2"

def crear_baraja() -> list:
    """
    function: crear_baraja()
    description: Crea la baraja con todos sus valores
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
    function: print_baraja()
    description: Imprime la baraja con sus elementos actuales
    params: baraja
    """
    for i in range(0, len(baraja), 4):
     print(baraja[i:i+4])

def convert_as(mano_J1:list) -> list:
    """
    function: convert_as()
    description: Convierte el valor actual de la mano en el valor que indique el usuario
    params: mano_J1
    """
    valid = True
    for i in range(len(mano_J1)):
        while valid == True:
            decision = input("Qué valor desea darle al As, 1 o 11?\n")
            if decision == "1":
                mano_J1[i] = 1
                valid = False
            elif decision == "11":
                mano_J1[i] = 11
                valid = False
            else:
                print('Lo siento, el dado no puede devolver ese valor')
                valid = False
    
    return mano_J1
        
def sumar_mano(mano_jugador:list) -> int:
    """
    function: sumar_mano()
    description: Suma los valores que contiene la mano del jugador
    params: mano_jugador
    """
    total_mano = 0

    for i in range(2):
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
    function: print_mano()
    description: Imprime el mensaje con la mano del jugador
    params: jugador, mano_jugador
    """
    print(f'\n{jugador}')
    print("Sus cartas son '"+mano_jugador[0]+"' y '"+mano_jugador[1]+"'")

def total_pts(total_J1:int, total_J2:int) -> dict:
    """
    function: total_pts()
    description: Imprime el mensaje con la mano del jugador
    params: jugador, mano_jugador
    """
    puntos_J1 = 0
    puntos_J2 = 0
    totales = {}


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

    if total_J2 == 21:
        if total_J1 == 21:
            puntos_J2 += 3
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

    totales = {
        'total_J1': puntos_J1,
        'total_J2': puntos_J2
        }
    
    return totales

def play_J1(baraja) -> dict:
    """
    function: total_pts()
    description: Imprime el mensaje con la mano del jugador
    params: jugador, mano_jugador
    """
    play_in = True
    data_J1 = {}
    mano_J1 = []
    total = 0
    baraja_actual = baraja
    jug1 = "Jugador 1"

    while play_in:
        carta_aleatoria = random.randint(0,51)
        if baraja_actual[carta_aleatoria] == 0:
            ""
        else:
            mano_J1.append(baraja_actual[carta_aleatoria])
            baraja_actual[carta_aleatoria] = 0
        
        if len(mano_J1) == 2:
            play_in = False

    print_mano(jug1, mano_J1)

    # Verifica si existen A's y si es verdadero reemplaza el valor por el que indique el usuario
    cant_ace = mano_J1.count("A")
    if cant_ace >= 1:
        mano_J1 = convert_as(mano_J1)

    total = sumar_mano(mano_J1)
    data_J1 = {
        "total_J1": total,
        "baraja_actual": baraja_actual,
        "mano_J1": mano_J1
    }

    return data_J1

def play_J2(baraja) -> dict:

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
    cant_as = mano_J2.count('A')
    if cant_as >= 1:
        mano_J2 = convert_as(mano_J2)

    total = sumar_mano(mano_J2)
    data_J2 = {
        "total_J2": total,
        "baraja_actual": baraja_actual,
        "mano_J2": mano_J2
    }
    baraja_actual = data_J2["baraja_actual"]

    return data_J2

# Para implementar para el avance #3
def jugar_extra(dict_J1:dict) -> dict:

    baraja_actual = dict_J1["baraja_actual"]
    carta_aleatoria = random.randint(0,51)

    mano_J1 = dict_J1["mano_J1"]

    if dict_J1["baraja_actual"][carta_aleatoria] == 0:
        ""
    else:
        mano_J1.append(dict_J1["baraja_actual"][carta_aleatoria])
        print_mano(jug1, mano_J1)
        total = sumar_mano(mano_J1)
        data_J1 = {
            "total_J1": total,
            "baraja_actual": baraja_actual,
            "mano_J1": mano_J1
    }  
    return data_J1