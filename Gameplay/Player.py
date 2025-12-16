from Cards import Card

CHARACTERS = ["Plum","White","Scarlet","Green","Mustard","Peacock"]
WEAPONS = ["Rope","Dagger","Wrench","Pistol","Candlestick","Lead Pipe"]
ROOMS = ["Courtyard","Game Room","Study","Dining Room","Garage","Living Room","Kitchen","Bedroom","Bathroom"]


class Player():
    
    def __init__(self) -> None:
        self.hand:list[Card] =[]
        
        '''
        possible_worlds: DEL implementation of players' notebook, possible worlds
        are all possible combinations of cards that have not been seen by player. Seeing a card updates
        player knowledge model. Inits to all game possibilities (6x6x9).
        '''
        self.possible_worlds =set() 
        for char in CHARACTERS:
            for weap in WEAPONS:
                for room in ROOMS:
                    self.possible_worlds.add((char,weap,room))
    
    def knowledge_update(self, card:Card):
        self.possible_worlds = [item for item in self.possible_worlds if card.name not in item]
        
    def _assert(self):
        pass
    
    def accept(self):
        pass
    def reject(self):
        pass
    