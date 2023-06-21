
from black_jack_functions import *
import random

# card_deck = deck_construction()

# deck_print(card_deck)

# suits_list = card_deck[1]
 
# rndm_card_index_list = get_random_card(suits_list)


player_1_in = True
player_2_in = True

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
                # total = total + 10

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
    
for _ in range (2): 
    dealCard (player_1_hand)
    dealCard (player_2_hand)

while player_1_in or player_2_in:
    
    if player_1_in:
        print('\nMano del Jugador 1: ')
        print(*player_1_hand, sep=", ")
        print (f"- Total: {total(player_1_hand)}")
        stayOrHit1 = input("\nJugador 1 decida - 1: Se queda 2: Entra\n")
        if stayOrHit1 == '1':
            player_1_in = False
        else:
            dealCard(player_1_hand)
            print('\nMano del Jugador 1: ')
            print(*player_1_hand, sep=", ")
            print(f'Total del jugador 1: {total(player_1_hand)}')
    
    if player_2_in:
        print('\nMano del Jugador 2: ')
        print(*player_2_hand, sep=", ")
        print (f"- Total: {total(player_2_hand)}")
        stayOrHit2 = input("\nJugador 2 decida - 1: Se queda 2: Entra\n")
        if stayOrHit2 == '1':
            player_2_in = False
        else:
            dealCard(player_2_hand)
            print(*player_2_hand, sep=", ")
            print('\nMano del Jugador 2: ')
            print(*player_2_hand, sep=", ")   
            print(f'Total del jugador 2: {total(player_2_hand)}')
            

    # if total (player_2_hand) > 16:
    #    player_2_in= False
    # else:
    #   dealCard(player_2_hand)

    if total (player_1_hand) >= 21:
        break
    elif total (player_2_hand) >= 21: 
        break

total_p1 = total(player_1_hand)
total_p2 = total(player_2_hand)

win_msg_1 = f"\nEl J1 tiene {player_1_hand} por un total de {total_p1} y el J2 tiene {player_2_hand} por un total de {total_p2}\nBlackjack! Jugador 1 gana!\nBaraja = {deck}\n"

win_msg_2 = f"\nEl J1 tiene {player_1_hand} por un total de {total_p1} y el J2 tiene {player_2_hand} por un total de {total_p2}\nBlackjack! Jugador 2 gana!\nBaraja = {deck}\n"

win_msg_3 = f"\nEl J1 tiene {player_1_hand} por un total de {total_p1} y el J2 tiene {player_2_hand} por un total de {total_p2}\nJugador 1 se ha pasado! El jugador 2 ha ganado!\nBaraja = {deck}\n"

win_msg_4 = f"\nEl J1 tiene {player_1_hand} por un total de {total_p1} y el J2 tiene {player_2_hand} por un total de {total_p2}\nJugador 2 se ha pasado! El jugador 1 ha ganado!\nBaraja = {deck}\n"

win_msg_5 = f"\nEl J1 tiene {player_1_hand} por un total de {total_p1} y el J2 tiene {player_2_hand} por un total de {total_p2}\nEl jugador 2 gana!\nBaraja = {deck}\n"

win_msg_6 = f"\nEl J1 tiene {player_1_hand} por un total de {total_p1} y el J2 tiene {player_2_hand} por un total de {total_p2}\nEl jugador 1 gana!\nBaraja = {deck}\n"


if total(player_1_hand) == 21: 
    print(win_msg_1)

elif total(player_2_hand) == 21:
    print(win_msg_2)

elif total(player_1_hand) > 21:
    print(win_msg_3)

elif total(player_2_hand) > 21:
    print(win_msg_4)

elif  21 - total(player_2_hand) < 21 -total(player_1_hand):
    print(win_msg_5)

elif 21 - total(player_2_hand) > 21 - total(player_1_hand):
   print(win_msg_6)


# TO DO

# def pts ():
#     if total(player_2_hand) or total(player_1_hand) == 21:
#         print(f" el jugador obtuvo 6 {pts}")
    
#     elif total(player_2_hand) and total(player_1_hand) == 2:
#         print(f"el jugador obtuvo 3 {pts}")
    
#     elif total(player_1_hand) or total(player_2_hand) == range [17,20] < 21:
#        print(f"el jugador{pts(player_1_hand)} obtuvo 2 y el jugador  ")
    
#     elif total (player_1_hand) or total(player_2_hand) < 17 <= 21: 
#        print(f" el jugador obtuvo 1 {pts}")
    
#     elif total(player_1_hand) and total (player_2_hand) > 21:
#        print(f"el jugador obtuvo 1 {pts} ")

