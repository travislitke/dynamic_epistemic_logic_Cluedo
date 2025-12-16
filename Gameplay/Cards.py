import Player
import random

CHARACTERS = ["Plum","White","Scarlet","Green","Mustard","Peacock"]
WEAPONS = ["Rope","Dagger","Wrench","Pistol","Candlestick","Lead Pipe"]
ROOMS = ["Courtyard","Game Room","Study","Dining Room","Garage","Living Room","Kitchen","Bedroom","Bathroom"]

class Card():
    
    def __init__(self, type:str, name:str) -> None:
        self.type = type
        self.name = name
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Card):
            return self.name == other.name
        return False
    
    def __str__(self):
        return self.name
    

class Deck():
    
    def __init__(self) -> None:
        self.cards:list[Card] = []
        
        for name in CHARACTERS:
            self.cards.append(Card(type="character",name=name))
        for room in ROOMS:
            self.cards.append(Card(type="room",name=room))
        for weap in WEAPONS:
            self.cards.append(Card(type="weapon",name=weap))    
        

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Deck):
            for idx in range(len(self.cards)):
                if self.cards[idx] != other.cards[idx]:
                    return False
            return True
        return False
    
    def __getitem__ (self,idx):
        return self.cards[idx]


    def __len__(self):
        return len(self.cards)
    
    
    def __str__(self):
        string = ""
        for card in self.cards:
            string+= str(card)+"\n"
        return string
    
    def add(self, card:Card):
        self.cards.append(card)
    
    def deal(self, player: Player.Player):
        card = self.cards[0]
        del self.cards[0]
        player.hand.append(card)
    
    def remove(self, name:str):
        for card in self.cards:
            if card == name:
                self.cards.remove(card)
    
    
    '''Employs in-place Fisher-Yates Shuffle algorithm'''
    def fy_shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            new = random.randint(0,i)
            self.cards[i],self.cards[new] = self.cards[new],self.cards[i]

    '''Regular hand-shuffling method implemented for funsies'''
    def hand_shuffle(self, repeat:int=1):
        for _ in range(repeat):
            arr1 = [self.cards[i] for i in range(len(self.cards)) if i%2==0]
            arr2 = [self.cards[i] for i in range(len(self.cards)) if i%2==1]
            self.cards = arr1+arr2

            
        