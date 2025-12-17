from Deck import *
import logging

ROOMS = ["Courtyard","Game Room","Study","Dining Room","Garage","Living Room","Kitchen","Bedroom","Bathroom"]

class Agent():
    
    def __init__(self,name:str) -> None:
        self.name=name
        self.hand:list[Card]=[]
        self.seen:list[str]=[]
        self.rooms = ROOMS


    def __str__(self):
        return self.name
    
    
    def take_card(self, card:Card):
        self.hand.append(card)
        self.see_card(card.name)
    
    def see_card(self, card:str):
        self.seen.append(card)
        if card in self.rooms:
            self.rooms.remove(card)
        logging.info(f"Agent {self.name} has seen card {card}.")
        
    def check_hand(self, name:str)-> bool:
        if name in [card.name for card in self.hand]:
            return True
        return False
        
            
    

        

        
    