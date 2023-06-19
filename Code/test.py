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