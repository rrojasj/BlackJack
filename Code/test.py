# card_deck = deck_construction()

# deck_print(card_deck)

# suits_list = card_deck[1]
 
# rndm_card_index_list = get_random_card(suits_list)

# a list of all the suits

# "\u2663" = Clubs
# "\u2665" = Heart
# "\u2666" = Diamonds
# "\u2660" = Spades

# Suits = ["\u2663", "\u2665",
#          "\u2666", "\u2660"]
# # a list of all the ranks
# Ranks = ['A', '2', '3', '4', '5',
#          '6', '7', '8', '9', '10',
#          'J', 'Q', 'K']
  
# # Matching all the suits with all the ranks
# for rank in Ranks:
  
#     for suit in Suits:
#         print(f'{rank} of {suit}'.ljust(10), end='')
  
#     # Spacer
#     print()

# *- -------------------------------------------------- -*

# a list of cards - Dictionary

# def deck_construction():
    
#     card_deck = {
#         "\u2663": [1,2,3,4,5,6,7,8,9,10,"J","Q","K"],
#         "\u2665": [1,2,3,4,5,6,7,8,9,10,"J","Q","K"],
#         "\u2666": [1,2,3,4,5,6,7,8,9,10,"J","Q","K"],
#         "\u2660": [1,2,3,4,5,6,7,8,9,10,"J","Q","K"]
#     }

# *- -------------------------------------------------- -*

    # # a list of all the suits
    # Suits = ['\u2663', '\u2665', '\u2666', '\u2660']
    
    # # a list of all the ranks
    # Ranks = ['A',2, 3, '4',
    #         '5', '6', '7', '8',
    #         '9', '10', 'J', 'Q', 'K']
    
    # card_deck = [Suits, Ranks]

    # return card_deck

# # Matching all the suits with all the ranks
#     for rank in p_ranks:
  
#         for suit in p_suits:
#             print(f'{rank} of {suit}'.ljust(16), end='')
#         # Spacer
#         print()

# *- -------------------------------------------------- -*

    # card_deck_dic = {
    #     "\u2663": ['A',1,2,3,4,5,6,7,8,9,10,'J','Q','K'],
    #     "\u2665": ['A',1,2,3,4,5,6,7,8,9,10,'J','Q','K'],
    #     "\u2666": ['A',1,2,3,4,5,6,7,8,9,10,'J','Q','K'],
    #     "\u2660": ['A',1,2,3,4,5,6,7,8,9,10,'J','Q','K']
    # }

# *- -------------------------------------------------- -*

# import random

# my_list = ['apple', 'banana', 'orange', 'grape', 'kiwi']
# num_elements = 2  # Number of elements to select randomly

# random_elements = []
# random_indices = []

# for _ in range(num_elements):
#     random_index = random.randint(0, len(my_list) - 1)
#     random_elements.append(my_list[random_index])
#     random_indices.append(random_index)

# print("Random elements:", random_elements)
# print("Indices of random elements:", random_indices)

# *- -------------------------------------------------- -*

# FUNCTIONS - OLD

# 1st Deliverable

# "\u2663" = Clubs
# "\u2665" = Heart
# "\u2666" = Diamonds
# "\u2660" = Spades

# def deck_construction():

#     # List of Ranks
#     # card_deck_ranks = ['\u2663', '\u2665', '\u2666', '\u2660']
    
#     # List of Suits
#     deck = [ 2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10
#       ,'J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K','A']

#     return deck

# def deck_print(p_card_deck):

#     ranks = p_card_deck[0]
#     suits = p_card_deck[1]

#     # Matching all the suits with all the ranks
#     # for rank in ranks:
#     i=1
#     for suit in suits:
#         print(f'{i} = {suit}'.ljust(10), end='')
#         i = i+1

#     # Spacer
#     print()

# def get_random_card(p_card_deck):
#     import random

#     my_list = ['apple', 'banana', 'orange', 'grape', 'kiwi']
#     num_elements = 2  # Number of elements to select randomly

#     random_elements = []
#     random_indexes = []

#     for _ in range(num_elements):
#         random_index = random.randint(0, len(my_list) - 1)
#         random_elements.append(my_list[random_index])
#         random_indexes.append(random_index)

#     # print("Random elements:", random_elements)
#     # print("Indices of random elements:", random_indexes)

#     set_values_zero(p_card_deck, random_index)

# def set_values_zero(p_deck, p_index):
#     print(p_deck)
#     p_deck[p_index] = 0
#     print(p_deck)
#     deck_print(f'El resultado es: {p_deck}')

# def show_cards():
#     return

# def get_as_value():
#     return

# def define_points_dist():
#     return


# *- -------------------------------------------------- -*

# Functions of current Code

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


for _ in range (2): 
    dealCard (player_1_hand, deck)
    dealCard (player_2_hand, deck)

formatted_hand_1 = ' y '.join(map(str, player_1_hand))
formatted_hand_2 = ' y '.join(map(str, player_2_hand))



while player_1_in or player_2_in:
    
    if player_1_in:
        
        print(f'\nMano del Jugador 1: {formatted_hand_1}')
        print (f'- Total: {total(player_1_hand)}')
        stayOrHit1 = input("\nJugador decida - 1: Se queda 2: Entra ")
        if stayOrHit1 == '1':
            player_1_in = False
        else:
            dealCard(player_1_hand, deck)
            print(f'\nMano del Jugador 1: {formatted_hand_1}')
            print(f'- Total: {total(player_1_hand)}')
    
    if player_2_in:
        print(f'\nMano del Jugador 2: {formatted_hand_2}')
        print (f'- Total: {total(player_2_hand)}')
        stayOrHit2 = input("\nJugador decida - 1: Se queda 2: Entra ")
        if stayOrHit2 == '1':
            player_2_in = False
        else:
            dealCard(player_2_hand, deck)
            print(f'\nMano del Jugador 2: {formatted_hand_2}') 
            print(f'- Total: {total(player_2_hand)}')
            

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

