
from black_jack_functions import *

card_deck = deck_construction()

deck_print(card_deck)

suits_list = card_deck[1]
 
rndm_card_index_list = get_random_card(suits_list)
