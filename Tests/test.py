from Gameplay import Cards, Game, Player
import random
import unittest

class TestSimulator(unittest.TestCase):
    def testDeckInit(self):
        test_deck = Cards.Deck()
        assert(len(test_deck)== 9+6+6)
        assert(len(test_deck.cards)==9+6+6)
    
    def testDeckHandShuffle(self):
        deck1 = Cards.Deck()
        deck2 = Cards.Deck()
        assert(deck1==deck2)
        deck2.hand_shuffle(1)
        assert(deck1!=deck2)
        
    def testDeckFYShuffle(self):
        deck1 = Cards.Deck()
        deck2 = Cards.Deck()
        assert(deck1==deck2)
        deck2.fy_shuffle()
        assert(deck1!=deck2)
    
    def testPlayerInit(self):
        test_player = Player.Player()
        assert(len(test_player.possible_worlds)==9*6*6)
        
    def testKnowledgeUpdate(self):
        test_player_1 = Player.Player()
        test_deck = Cards.Deck()
        card = random.sample(test_deck.cards,k=1)[0]
        test_player_1.knowledge_update(card)
        for world in test_player_1.possible_worlds:
            assert(card.name not in world)
        