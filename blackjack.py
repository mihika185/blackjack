import random

suits = ["\u2660", "\u2665", "\u2666", "\u2663"]
# suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
rank_vals = [1,2,3,4,5,6,7,8,9,10,10,10,10]

class Card:
    def __init__(self, rank, suit): 
        self.suit = suit
        self.rank = rank
        self.name = rank+"of"+suit
        self.value = rank_vals[ranks.index(rank)]

deck = []
for rank in ranks:
    for suit in suits:
        newcard = Card(rank, suit)
        deck.append(newcard)

for card in deck:
    print(card.name, end=", ")
print()
# print(len(deck))

def deal(n,deck):
    card_to_be_dealt = deck.pop(random.randint(0,len(deck)-1))
    hand = []
    hand.append(card_to_be_dealt)
    while len(hand)<n:
        card_to_be_dealt = deck.pop(random.randint(0,len(deck)-1))
        hand.append(card_to_be_dealt)
    return hand

def evaluate(hand):
    val = 0
    for card in hand:
        val += card.value
    return val

# print(len(deck))
# testhand = deal(2,deck)
# for card in testhand:
#     print(card.name, end=", ")
# print()
# print(len(deck))

def play():
    playerhand = deal(2,deck)
    dealerhand = deal(2,deck)

    print("\nDealer's hand is: ", end="")
    print(dealerhand[0].name, "?")

    print("\nYour hand is: ", end="")
    for card in playerhand:
        print(card.name, end=", ")
    print()

    stood = False
    surrendered = False

    while not stood and not surrendered:
        choice = input("\nEnter 1 to hit ,2 to stand, 3 to surrender: ")

        if choice == "1":
            playerhand.append(deal(1,deck)[0])
            print("\nYour hand is: ", end="")
            for card in playerhand:
                print(card.name, end=", ")
            print()
        elif choice == "2":
            stood = True
            print("\nYour hand is: ", end="")
            for card in playerhand:
                print(card.name, end=", ")
            print()

        elif choice == "3":
            surrendered = True
            print("\nYour hand is: ", end="")
            for card in playerhand:
                print(card.name, end=", ")
            print()

    for card in playerhand:
        if card.rank == "Ace":
            print("Do you want your ", card.name," to be worth 1 or 11?: ")
            ace_value = input("Enter value (1 or 11): ")
            card.value = int(ace_value)

    playerhand_value = evaluate(playerhand)
    dealerhand_value = evaluate(dealerhand)

    print("\nPlayer has played, it is dealer's turn\n")

    #dealer playes
    dealer_stood = False
    dealer_bust = False
    while not dealer_stood and not dealer_bust:
        if dealerhand_value>21:
            dealer_bust=True
        elif dealerhand_value>=playerhand_value:
            dealer_stood = True
        elif dealerhand_value<=playerhand_value:
            dealerhand.append(deal(1,deck)[0])
            print("Dealer's hand is: ", end="")
            for card in dealerhand:
                print(card.name, end=", ")
            print()
            dealerhand_value = evaluate(dealerhand)
        
    for card in dealerhand:
        if card.name == "Ace":
            if dealerhand_value+11-1>21:
                card.value = 1
            else:
                card.value = 11
        dealerhand_value = evaluate(dealerhand)

    print("\nYour hand is: ", end="")
    for card in playerhand:
        print(card.name, end=", ")
    print()
    print("Your hand is worth: ", evaluate(playerhand))

    print("Dealer's hand is: ", end="")
    for card in dealerhand:
        print(card.name, end=", ")
    print()
    print("Dealer's hand is worth: ", evaluate(dealerhand))

    if playerhand_value > 21:
        print("Oh no! player1 looses :(")

    elif dealerhand_value > 21:
        print("Dealer busts, player wins! :)")

    elif playerhand_value > dealerhand_value:
        print("Player beats dealer and wins :)")

    elif dealerhand_value > playerhand_value:
        print("Dealer beats player, player looses :(")

play()