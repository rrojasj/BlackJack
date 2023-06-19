
from black_jack_functions import *
import random

# card_deck = deck_construction()

# deck_print(card_deck)

# suits_list = card_deck[1]
 
# rndm_card_index_list = get_random_card(suits_list)


player_1_In = True
player_2_In = True

deck=[ 2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,'J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K','A']

player_1_hand=[]
player_2_hand =[] 

def dealCard(turn):
    card = random.choice(deck)
    index = random.randint(0, len(deck) - 1)
    turn.append(card)
    deck.remove(card)

def total(turn):
    total=0
    face =["J","Q","K"]
    ace = "A"
    
    for card in turn:
        if total <= 20:
            if card in  range (1,11):
                total += card
            
            elif card in face:
                total += 10

            # elif card in ace:
            #     ace_selection = input("Valor del A's - 1: 1 - 2: 11\n")
            #     if ace_selection == "1":
            #         total += 1
            #     else:
            #         total += 11
                    
            else:
                ace_selection = input("Valor del A's - 1: 1 - 2: 11\n")
                if ace_selection == "1":
                    total += 1
                else:
                    total += 11
    return total

def revealplayer_2_hand():
    if len(player_2_hand) ==2 :
        return player_2_hand [0]
    elif len (player_2_hand) > 2:
     return player_2_hand[0] , player_2_hand[1]
    
for _ in range (2): 
    dealCard (player_2_hand)
    dealCard (player_1_hand)


while player_1_In or player_2_In:
    
    if player_1_In:
        print('\nMano del Jugador 1: ')
        print(*player_1_hand, sep=" & ")
        print (f"\nEl jugador 1 tiene {player_1_hand} por un total de {total(player_1_hand)}")
        stayOrHit1 = input("\nJugador 1 decida - 1: Se queda 2: Entra\n")
        if stayOrHit1 == '1':
            player_1_In = False
        else:
            dealCard(player_1_hand)
            print('\nMano del Jugador 1: ')
            print(*player_1_hand, sep=" & ")
            print(f'Total del jugador 1: {total(player_1_hand)}')
    
    if player_2_In:
        print('\nMano del Jugador 2: ')
        print(*player_2_hand, sep=" & ")
        print (f"\nEl jugador 2 tiene {player_2_hand} por un total de {total(player_2_hand)}")
        stayOrHit2 = input("\nJugador 2 decida - 1: Se queda 2: Entra\n")
        if stayOrHit2 == '1':
            player_2_In = False
        else:
            dealCard(player_2_hand)
            print(*player_2_hand, sep=" & ")
            print('\nMano del Jugador 2: ')
            print(*player_2_hand, sep=" & ")   
            print(f'Total del jugador 2: {total(player_2_hand)}')
            

    # if total (player_2_hand) > 16:
    #    player_2_In= False
    # else:
    #   dealCard(player_2_hand)

    if stayOrHit2 == '1':
       player_1_In = False
    else:
      dealCard(player_2_hand)

    if total (player_1_hand) >= 21:
        break
    elif total (player_2_hand) >= 21: 
        break

total_p1 = total(player_1_hand)
total_p2 = total(player_2_hand)


if total(player_1_hand) == 21: 
    print(f"\nEl J1 tiene {player_1_hand} por un total de {total_p1} y el J2 tiene {player_2_hand} por un total de {total_p2}")
    print("\nBlackjack! Jugador 1 gana!\n")
    print(f'Baraja = {deck}\n')

elif total(player_2_hand) == 21:
    print(f"\nEl J1 tiene {player_1_hand} por un total de {total_p1} y el J2 tiene {player_2_hand} por un total de {total_p2}")
    print("\nBlackjack! Jugador 2 gana!\n")
    print(f'Baraja = {deck}\n')

elif total(player_1_hand) > 21:
    print(f"\nEl J1 tiene {player_1_hand} por un total de {total_p1} y el J2 tiene {player_2_hand} por un total de {total_p2}")
    print("\nJugador 1 se ha pasado! El jugador 2 ha ganado!\n")
    print(f'Baraja = {deck}\n')

elif total(player_2_hand) > 21:
    print(f"\nEl J1 tiene {player_1_hand} por un total de {total_p1} y el J2 tiene {player_2_hand} por un total de {total_p2}")
    print("\nJugador 2 se ha pasado! El jugador 1 ha ganado!\n")
    print(f'Baraja = {deck}\n')

elif  21 - total(player_2_hand) < 21 -total(player_1_hand):
    print(f"\nEl J1 tiene {player_1_hand} por un total de {total_p1} y el J2 tiene {player_2_hand} por un total de {total_p2}")
    print("\nEl jugador 2 gana!\n")
    print(f'Baraja = {deck}\n')

elif 21 - total(player_2_hand) > 21 - total(player_1_hand):
   print(f"\nEl J1 tiene {player_1_hand} por un total de {total_p1} y el J2 tiene {player_2_hand} por un total de {total_p2}")
   print("\nEl jugador 1 gana!\n")
   print(f'Baraja = {deck}\n')


def pts ():
    if total(player_2_hand) or total(player_1_hand) == 21:
        print(f" el jugador obtuvo 6 {pts}")
    
    elif total(player_2_hand) and total(player_1_hand) == 2:
        print(f"el jugador obtuvo 3 {pts}")
    
    elif total(player_1_hand) or total(player_2_hand) == range [17,20] < 21:
       print(f"el jugador{pts(player_1_hand)} obtuvo 2 y el jugador  ")
    
    elif total (player_1_hand) or total(player_2_hand) < 17 <= 21: 
       print(f" el jugador obtuvo 1 {pts}")
    
    elif total(player_1_hand) and total (player_2_hand) > 21:
       print(f"el jugador obtuvo 1 {pts} ")

