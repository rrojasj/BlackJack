# BlackJack
- Black Jack Game

# Description
- This game consists of using a full English deck (52 cards without jokers) and approaching the nearest value of 21 without going over.

# General Description

- The game will be a simulation, where the player will compete against a computer artificial intelligence algorithm, which will be explained later.
  To do this, the game must load a deck of 52 cards, where a complete game against the computer will be the result of several rounds of play, until the deck of cards is exhausted. This means that a game can have between 5 and 13 game rounds.
  Number cards are used according to the value represented (from 2 to 10). Cards like J, Q, K, will have a fixed value of 10. The Ace can be worth 11 or 1, it will depend on the decision made by the player, which means that if he got an 8 at the beginning and an Ace as With the second card, the game must ask the player if it counts as 11 or 1. In the case of the computer, the decision will depend on whether the Ace in 11 affects it to exceed 21. If the above happens, the computer will automatically take it. as 1, not as 11. If you have an Ace and the sum amount is less than 21, it will take it as 11.

# Deliverables

* 1st Advance

Deck construction. The deck of cards must be represented in a list of 52 spaces, where each card must be consumed.
   - There must be a random way to get a card from the list, and replace the value of the card with a zero. As more cards are requested, and a space with a zero is randomly selected, the algorithm must re-request a new space, until it finds an available card.
   - Python implementation of a program that randomly shows two cards to the user, and calculates the total for the player.
   - If the letter that appears is an AS, the program must ask the user what value he wants to give to said letter, that is, a 1 or an 11.
   - According to the total obtained by the player, you must calculate the points, based on the following rules.
     1. If the player gets 21, he earns 6 points.
     2. If both players get 21, they earn 3 points each.
     3. If the player is between 17 and 20, but closer to 21 than his opponent, he wins 2 points.
     4. If the player falls below 17, but closer to 21 than his opponent, he scores 1 point.
     5. If the player is over 21, he does not earn any points.

These points will accumulate as the game progresses.
