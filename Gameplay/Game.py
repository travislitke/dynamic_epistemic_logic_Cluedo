import random

from Cards import Deck


CHARACTERS = ["Plum","White","Scarlet","Green","Mustard","Peacock"]
WEAPONS = ["Rope","Dagger","Wrench","Pistol","Candlestick","Lead Pipe"]
ROOMS = ["Courtyard","Game Room","Study","Dining Room","Garage","Living Room","Kitchen","Bedroom","Bathroom"]

class Game():
    def __init__(self, num_players:int) -> None:
        self.active_players = []
        self.deck:Deck = Deck()
        self.envelope = ()
        self.num_players = num_players
        
        
    def setup(self,num_players:int):
        #each of n players chooses a character
        self.active_players = random.sample(CHARACTERS,num_players)
            
        #separate weapon,suspect,room decks
        #take top card from each deck to create the murder case
        #shuffle all cards together into one deck 
        #deal remaining cards to n players
        #leftover cards discarded, all players have the same number of cards
        
        pass

    def play(self):
        turn = 0
        print("init")
        self.setup(self.num_players)
        print("Simulating CLUE~")
        
        while len(self.active_players) >0:
            turn += 1
            print(f"Turn {turn}:")
            print(f"Kripke = {None}")
        

    




                