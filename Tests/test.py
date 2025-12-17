import Deck, Game, Agent
import random
import unittest

class TestSimulator(unittest.TestCase):
    def testDeckInit(self):
        test_deck = Deck.Deck()
        assert(len(test_deck)== 9+6+6)
        assert(len(test_deck.cards)==9+6+6)
    
    def testDeckHandShuffle(self):
        deck1 = Deck.Deck()
        deck2 = Deck.Deck()
        assert(deck1==deck2)
        deck2.hand_shuffle(1)
        assert(deck1!=deck2)
        
    def testDeckFYShuffle(self):
        deck1 = Deck.Deck()
        deck2 = Deck.Deck()
        assert(deck1==deck2)
        deck2.fy_shuffle()
        assert(deck1!=deck2)
    
