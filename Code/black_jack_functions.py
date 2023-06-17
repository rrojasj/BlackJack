# 1st Deliverable

# "\u2663" = Clubs
# "\u2665" = Heart
# "\u2666" = Diamonds
# "\u2660" = Spades

def deck_construction():

    # List of Ranks
    card_deck_ranks = ['\u2663', '\u2665', '\u2666', '\u2660']
    
    # List of Suits
    card_deck_suits = ['A','A','A','A', 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']


    card_deck_list = [card_deck_ranks, card_deck_suits]

    return card_deck_list

def deck_print(p_card_deck):

    ranks = p_card_deck[0]
    suits = p_card_deck[1]

    # Matching all the suits with all the ranks
    # for rank in ranks:
    i=1
    for suit in suits:
        print(f'{i} = {suit}'.ljust(10), end='')
        i = i+1

    # Spacer
    print()

def get_random_card(p_card_deck):
    import random

    num_elements = 1  # Number of elements to select randomly

    random_elements = 0
    random_index = 0

    for _ in range(num_elements):
        random_index = random.randint(0, len(p_card_deck) - 1)
        random_elements = (p_card_deck[random_index])
        random_index = (random_index)

    print("Random elements:", random_elements)
    print("Index of random elements:", random_index)

    set_values_zero(p_card_deck, random_index)
    
    # return p_card_deck[random_index]

def set_values_zero(p_deck, p_index):
    print(p_deck[p_index])
    p_deck[p_index] = 0
    deck_print(p_deck)

def show_cards():
    return

def get_as_value():
    return

def define_points_dist():
    return