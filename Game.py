import KnowledgeGraph
import logging
import random
from Agent import Agent as a
from Deck import Card, Deck
from typing import Optional



CHARACTERS = ["Plum","White","Scarlet","Green","Mustard","Peacock"]
WEAPONS = ["Rope","Dagger","Wrench","Pistol","Candlestick","Lead Pipe"]
ROOMS = ["Courtyard","Game Room","Study","Dining Room","Garage","Living Room","Kitchen","Bedroom","Bathroom"]

class Game():
    def __init__(self, num_players:int) -> None:
        self.num_players = num_players
        self.active_players = []
        self.deck=None
        self.kripke_model:Optional[KnowledgeGraph.Kripke] = None
        self.solution:tuple[str,...]|None = None
        self.rooms=ROOMS        
        
        
    def setup(self):
        
        # add players to game
        for i in range(self.num_players):
            name=str(f"A{i+1}")
            agent = a(name=name)
            self.active_players.append(agent)
            
        #separate weapon,suspect,room decks, shuffle
        character_deck = Deck([Card(i) for i in CHARACTERS])
        character_deck.fy_shuffle()
        weapon_deck = Deck([Card(i) for i in WEAPONS])
        weapon_deck.fy_shuffle()
        room_deck = Deck([Card(i) for i in ROOMS])
        room_deck.fy_shuffle()
        
        #take top card from each deck to create the murder case
        self.solution = tuple([character_deck.cards.pop().name, weapon_deck.cards.pop().name, room_deck.cards.pop().name])
        logging.info(f"Game solution: {self.solution}")

        #shuffle all cards together into one deck 
        mixed_deck = Deck(character_deck.cards+weapon_deck.cards+room_deck.cards)
        mixed_deck.fy_shuffle()
        self.deck=mixed_deck
        

        self.kripke_model = KnowledgeGraph.Kripke(solution=self.solution, agents=self.active_players)
        
        # deal remaining cards to n agents:
        while len(self.deck) > self.num_players:
            for player in self.active_players:
                card = self.deck.pop()
                player.take_card(card)
                self.kripke_model.update(player,card)
        
        # all agents have the same number of cards, and look at the remaining cards.
        for card in self.deck:
            for agent in self.active_players:
                agent.see_card(card)
                self.kripke_model.update(agent,card)
    
    def play(self):
        round=0
        turn=0
        while len(self.active_players) > 1:
            round += 1
            logging.info(f"Round {round}:")
            for agent in self.active_players:
                turn += 1
                logging.info(f"Agent {agent.name} turn {turn}:")
                agent_accessibility = self.kripke_model.accessibility_relations[agent.name]
                logging.info(f"Agent {agent.name}'s Accessibility relations:\n{[self.kripke_model.possible_worlds[i] for i in agent_accessibility]}")

                possible_suspects=[name for name in CHARACTERS if name not in agent.seen]
                possible_weapons=[weap for weap in WEAPONS if weap not in agent.seen]

                if len(agent_accessibility) > 1:
                    # move to a room and make a suggestion
                    suspect = random.choice(possible_suspects)
                    weapon = random.choice(possible_weapons)
                    room=random.choice(self.rooms)
                    suggestion = (suspect,room,weapon)
                    logging.info(f"Agent {agent.name} moves to {room}.")
                    logging.info(f"Agent {agent.name} suggests {suspect} with the {weapon} in the {room}.")
                    for opponent in self.active_players:
                        if opponent!=agent:
                            for name in suggestion:
                                if opponent.check_hand(name):
                                    agent.see_card(name)
                                    self.kripke_model.update(agent,name)
                                    break
                else:
                    # make a proposal to try to win
                    proposal = self.kripke_model.accessibility_relations[agent][0]
                    logging.info(f"Agent {agent.name} suggests {suspect} with the {weapon} in the {room}.")
                    if proposal==self.solution:
                        print("Game over!")
                        break
                    else:
                        self.active_players.remove(agent)
                        
                    
                
                    
                
                
                
        

    




                