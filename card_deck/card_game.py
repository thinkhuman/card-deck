
import random

class Deck(object):
    """
    A deck consists of 52 cards: 13 of each of four suits, rank Ace (1) through King.
    """

    deck = []

    def __init__(self):
        self.ranks = (2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace')
        self.suits = ('Spades', 'Clubs', 'Hearts', 'Diamonds')

    def create_new_deck(self):
        """
        Create and return a deck of 52 cards, containing 13 ranks in 4 suits.
        """
        self.deck = [(r,s) for r in self.ranks for s in self.suits]
        return self.deck

    def shuffle_deck(self):
        """ 
        Randomly reorder the deck so that cards are not in sequential order

        """
        return random.shuffle(self.deck)


class Hand(Deck):
    """
    A hand is all the cards drawn (currently "in hand")
    """
    def __init__(self, Deck):
        self.deck = Deck.deck
        self.cards = []

    def draw_card(self):
        """
        Draw one card from a random location in the deck.
        
        """
        card = self.deck.pop(random.randrange(len(self.deck)))
        self.cards.append(card)
        return card


class Start(object):
    """
    A user can:
    1. Draw a card as many times as they wish, until the deck is depleted
    2. Shuffle the entire deck at any time
    3. See a list of the cards they've drawn so far
    4. Quit playing with the deck (Exit the program)
    """

    def start_game():

        new_deck = Deck()
        new_deck.create_new_deck()
        new_deck.shuffle_deck()
        new_hand = Hand(new_deck)

        print("****************")
        print("*  CARD DECK   *")
        print("****************")

        while True:
            choice = input("\nWould you like to: \n* (S)huffle the deck \n* (D)raw a card \n* See Your (C)ards \n* (Q)uit? ")
            choice = choice.lower()
            if choice == 's':
                new_deck.create_new_deck()
                new_deck.shuffle_deck()
                new_hand = Hand(new_deck)
                # for card in new_deck.deck:
                #     print(card)
                print("Okay, I shuffled the deck.")
                continue
            elif choice == 'd':
                if len(new_hand.deck) >= 1:
                    mycard = new_hand.draw_card()
                    print("\nYou drew the {} of {}.".format(mycard[0], mycard[1]))                    
                    print("There are {} cards left in the deck.".format(len(new_hand.deck)))
                    continue
                else:
                    print("Sorry, there are no more cards left!")
                    continue
            elif choice == 'c':
                print("\nSo far, you've drawn these cards:\n")
                for card in new_hand.cards:
                    print("{} of {}".format(card[0], card[1]) )
                continue
            elif choice == 'q':
                print('Thanks for playing!')
                break
            else:
                print("Sorry, that's not a valid choice")
                continue






