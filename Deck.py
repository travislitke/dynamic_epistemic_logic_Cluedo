import random

CHARACTERS = ["Plum","White","Scarlet","Green","Mustard","Peacock"]
WEAPONS = ["Rope","Dagger","Wrench","Pistol","Candlestick","Lead Pipe"]
ROOMS = ["Courtyard","Game Room","Study","Dining Room","Garage","Living Room","Kitchen","Bedroom","Bathroom"]

class Card():
    
    def __init__(self, name:str) -> None:
        self.name:str = name
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Card):
            return self.name == other.name
        return False
    
    def __str__(self):
        return f"{self.name}"
    
    def __hash__(self) -> int:
        return hash(self.name)
    

class Deck():
    
    def __init__(self, cards:list[Card]|None=None) -> None:
        if cards is None:
            cards = []
        self.cards:list[Card] = cards
            

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


    def pop(self)->Card:
        if not self.cards:
            raise IndexError("No cards in deck.")
        return self.cards.pop()
    
    
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

            
        