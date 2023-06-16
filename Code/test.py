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