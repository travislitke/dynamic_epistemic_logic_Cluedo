import logging
import Agent
from Deck import Card

CHARACTERS = ["Plum","White","Scarlet","Green","Mustard","Peacock"]
WEAPONS = ["Rope","Dagger","Wrench","Pistol","Candlestick","Lead Pipe"]
ROOMS = ["Courtyard","Game Room","Study","Dining Room","Garage","Living Room","Kitchen","Bedroom","Bathroom"]

class Kripke():
    
    def __init__(self, solution:tuple[str,...],agents:list[Agent.Agent]):
        self.solution = solution
        self.agents = agents
        self.possible_worlds = {f"w{i}":v for i,v in enumerate([(i,j,k) for i in CHARACTERS for j in WEAPONS for k in ROOMS])}
        self.actual_world = self.get_actual_world(solution)
        self.accessibility_relations = {agent.name:[(self.actual_world,possible_world) for possible_world in self.possible_worlds] for agent in self.agents}

        
    def get_actual_world(self, solution):
        for k,v in self.possible_worlds.items():
            if v == solution:
                return k
    
    def deduce(self,agent: Agent.Agent,suggestion: tuple[str,...]):
        '''
        If an agent makes a suggestion and nobody can answer, their silence means that no player
        holds any of the cards. The agent can deduce that their suggestion must be the solution
        to the game. 
        
        :param self: Description
        :param agent: Agent making the deduction
        :type agent: Object of type agent
        :param suggestion: A tuple of three strings, (suspect, weapon, room)
        :type suggestion: tuple[str, ...]
        '''
        
        for i in suggestion:
            assert(type(i)==str)
            for relation in self.accessibility_relations[agent.name]:
                if i not in self.possible_worlds[relation[1]]:
                        self.accessibility_relations[agent.name].remove(relation)
                
    def update(self,agent:Agent.Agent,card:Card):
        '''
        If an agent sees a card, they know that the correct world is any world
        where card does not hold, creates an accessibility relation (AR) between 
        worlds where card does not hold.
        i.e. if agent sees "Pistol", Ka ~Pistol
        
        :param player: The agent whose AR is being updated. 
        :param card: The card (proposition) that is adding information to player's AR.
        '''
        
        for relation in self.accessibility_relations[agent.name]:
                if card.name in self.possible_worlds[relation[1]]:
                        self.accessibility_relations[agent.name].remove(relation)
                        
            
        # logging.info(f"Agent {agent.name} has updated list of accessible worlds.")