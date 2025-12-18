import random

CHARACTERS = ["Plum","White","Scarlet","Green","Mustard","Peacock"]
WEAPONS = ["Rope","Dagger","Wrench","Pistol","Candlestick","Lead Pipe"]
ROOMS = ["Courtyard","Game Room","Study","Dining Room","Garage","Living Room","Kitchen","Bedroom","Bathroom"]

class Card():
    
    def __init__(self, type:str,name:str) -> None:
        self.type:str=type
        self.name:str=name
    
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Card):
            return self.name == other.name and self.type == other.type
        return False
    
    
    def __str__(self):
        return f"{self.type}: {self.name}"
    
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __iter__(self):
        yield self.type
        yield self.name
    

class Deck():
    
    def __init__(self):
        
        self.cards:list[Card] = []
        for char in CHARACTERS:
            self.cards.append(Card("Character",char))
        for weapon in WEAPONS:
            self.cards.append(Card("Weapon",weapon))
        for room in ROOMS:
            self.cards.append(Card("Room", room))
            

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
    
    
    def generate_solution(self)-> tuple[str,...]:
        
        character_cards = [card for card in self.cards if card.type=="Character"]
        weapon_cards = [card for card in self.cards if card.type == 'Weapon']
        room_cards = [card for card in self.cards if card.type=="Room"]
        solution = tuple([character_cards[0].name,weapon_cards[0].name,room_cards[0].name])
        self.cards.remove(character_cards[0])
        self.cards.remove(weapon_cards[0])
        self.cards.remove(room_cards[0])
        
        return solution
    
    
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

            
        