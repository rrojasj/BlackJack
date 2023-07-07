def crear_baraja() -> list:
    """
    function: crear_baraja()
    description: Crea la baraja con todos sus valores
    params: none
    """
    baraja = [
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
    "K \u2665", "K \u2666", "K \u2663", "K \u2660",
    "A's \u2665", "A's \u2666", "A's \u2663", "A's \u2660"]

    return baraja

def print_baraja(baraja):
    """
    function: print_baraja()
    description: Imprime la baraja con sus elementos actuales
    params: baraja
    """
    for i in range(0, len(baraja), 4):
     print(baraja[i:i+4])

def sumar_mano(mano_jugador:list) -> int:
    """
    function: sumar_mano()
    description: Suma los valores que contiene la mano del jugador
    params: mano_jugador
    
    """
    total_mano = 0

    for i in range(2):
        valor_actual = mano_jugador[i][0]
        if valor_actual in ["J","Q","K","1"]:
            total_mano += 10
        elif valor_actual == "A":
            decision = input("Qué valor desea darle al As, 1 o 11?\n")
            if decision == "1":
                total_mano += 1
            elif decision == "11":
                total_mano += 11
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
    import random
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
    total = sumar_mano(mano_J1)
    data_J1 = {
        "total_J1": total,
        "baraja_actual": baraja_actual
    }
    baraja_actual = data_J1["baraja_actual"]

    return data_J1

def play_J2(baraja) -> dict:
    import random
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
    total = sumar_mano(mano_J2)
    data_J2 = {
        "total_J2": total,
        "baraja_actual": baraja_actual
    }
    baraja_actual = data_J2["baraja_actual"]

    return data_J2