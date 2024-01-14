import random
from art import logo

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


def who_won(player_score, dealer_score):
    if player_score == dealer_score:
        print("It's a draw")
    elif player_score > 21:
        print("You lose")
    elif player_score < dealer_score and dealer_score <= 21:
        print("You lose")
    else:
        print("You won")


def blackjack_capstone():

    print(logo)
       
    dealer_hand = random.sample(cards, 2)
    dealer_score = sum(dealer_hand)

    while dealer_score < 17 or 11 in dealer_hand:
        dealer_hand.append(random.choice(cards))
        dealer_score = sum(dealer_hand)

        if dealer_score > 21 and 11 in dealer_hand:
                dealer_hand[dealer_hand.index(11)] = 1
                dealer_score = sum(dealer_hand)   

    player_hand = random.sample(cards, 2)
    player_score = sum(player_hand)
    if player_score > 21 and 11 in player_hand:
        player_hand[player_hand.index(11)] = 1
        player_score = sum(player_hand)

    while True:      
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {dealer_hand[0]}")

        cmd = input("Type 'y' to het another card, type 'n' to pass: ")

        if cmd == 'n':
            break
        else:
            player_hand.append(random.choice(cards))
            player_score = sum(player_hand)
            if player_score > 21 and 11 in player_hand:
                player_hand[player_hand.index(11)] = 1
                player_score = sum(player_hand)
        
        if player_score > 21:
            break

    print(f"Your final hand: {player_hand}, and score: {player_score}")
    print(f"Computer's final hand: {dealer_hand} and score {dealer_score}")
    who_won(player_score, dealer_score)

    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    blackjack_capstone()








