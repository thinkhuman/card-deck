import unittest
from card_game import *

class DeckTestCase(unittest.TestCase):
    """Tests for card_game.py"""

    def setUp(self):
        self.deck = []
        self.ranks = (2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace')
        self.suits = ('Spades', 'Clubs', 'Hearts', 'Diamonds')

    def test_create_new_deck(self):
        """Create a deck of 52 cards, covering 4 suits and 13 ranks"""

        self.deck = []
        self.assertTrue(len(Deck.create_new_deck(self)) == 52)           


class HandTestCase(unittest.TestCase):

    def setUp(self):
        self.deck = []
        self.ranks = (2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace')
        self.suits = ('Spades', 'Clubs', 'Hearts', 'Diamonds')
        self.cards = []
        Deck.create_new_deck(self)

    def test_draw_card(self):
        """Removes and returns a legal card (suit, rank) from the deck (not already in hand)"""

      # card drawn is not in the deck
        self.assertTrue(Hand.draw_card(self) not in self.deck)


if __name__ == '__main__':
    unittest.main()