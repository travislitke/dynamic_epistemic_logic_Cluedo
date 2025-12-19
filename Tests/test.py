import Deck, Game, Agent
import math
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
        
    def testDeal(self):
        num_players=[2,3,4,5,6]
        
        for n in num_players:
            # after shuffling deck of 21 cards and removing the three
            # solution cards, 18 cards should remain, divide amongst the 
            # current active players. 
            
            game = Game.Game(n)
            game.deal()
            expected_hand_size = math.floor(18/n)
            expected_leftover_cards=18%n
            for player in game.active_players:
                assert(len(player.hand)==expected_hand_size)
                assert(len(game.deck.cards)==expected_leftover_cards)
        
    
