import random

def run_hands(player_1_hand, player_2_hand, deck):
    for _ in range (2): 
        dealCard (player_1_hand, deck)
        total_p1 = total(player_1_hand)
        dealCard (player_2_hand)
        total_p2 = total(player_2_hand)
        player_totals = [total_p1, total_p2]
    
    return player_totals

def dealCard(turn, deck):
    card = random.choice(deck)
    index = random.randint(0, len(deck) - 1)
    turn.append(card)
    deck.remove(card)

def total(turn):
    total=0
    face =["J","Q","K"]
    
    for card in turn:
        if total <= 20:
            if card in range(1,11):
                total += card
            
            elif card in face:
                total += 10
                    
            else:
                ace_selection = input("Valor del A's - 1: 1 - 2: 11\n")
                if ace_selection == "1":
                    total += 1
                else:
                    total += 11
            # else:
            #     if total > 10:
            #         total += 1
                    
            #     else:
            #         total += 11
    return total

# def revealplayer_2_hand():
#     if len(player_2_hand) ==2 :
#         return player_2_hand [0]
#     elif len (player_2_hand) > 2:
#      return player_2_hand[0] , player_2_hand[1]