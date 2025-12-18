from Deck import *
import logging

class Agent():
    
    def __init__(self,name:str) -> None:
        self.name:str=name
        self.hand:list[Card]=[]
        self.possible_suspects = ["Plum","White","Scarlet","Green","Mustard","Peacock"]
        self.possible_weapons = ["Rope","Dagger","Wrench","Pistol","Candlestick","Lead Pipe"]
        self.possible_rooms = ["Courtyard","Game Room","Study","Dining Room","Garage","Living Room","Kitchen","Bedroom","Bathroom"]


    def __str__(self):
        return f"{self.name}"
    
    
    def __eq__(self, other):
        if isinstance(other,Agent):
            return self.name==other.name
        return False
    
    
    def __hash__(self) -> int:
        return hash((self.name))

    
    def take_card(self,card):
        self.hand.append(card)
        self.see_card(card)
    
    
    def see_card(self, card:Card):
        logging.info(f"Agent {self.name} has seen card {card}.")
        match card.type:
            case "Character":
                self.possible_suspects.remove(card.name)
            case "Weapon":
                self.possible_weapons.remove(card.name)
            case "Room":
                self.possible_rooms.remove(card.name)

    
    def check_hand(self, name:str)-> bool:
        if name in [card.name for card in self.hand]:
            return True
        return False
        
            
    

        

        
    