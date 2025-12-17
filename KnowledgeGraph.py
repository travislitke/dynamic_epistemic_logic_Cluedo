import Agent
import Deck

CHARACTERS = ["Plum","White","Scarlet","Green","Mustard","Peacock"]
WEAPONS = ["Rope","Dagger","Wrench","Pistol","Candlestick","Lead Pipe"]
ROOMS = ["Courtyard","Game Room","Study","Dining Room","Garage","Living Room","Kitchen","Bedroom","Bathroom"]


class World():

    def __init__(self, props:tuple[str,...]):

        self.props = props
    
    def __str__(self):
        return self.props


class Kripke():
    
    def __init__(self, solution:tuple,agents):
        self.solution = solution
        self.possible_worlds = {v: f"w{i}" for i,v in enumerate([(i,j,k) for i in CHARACTERS for j in WEAPONS for k in ROOMS])}
        self.accessibility_relations = {agent.name: [world for world in self.possible_worlds] for agent in agents}
        self.actual_world = self.get_actual_world(solution)
        
    def get_actual_world(self, solution):
        for k,v in self.possible_worlds.items():
            if k==solution:
                print(f"ACTUAL WORLD = {v}")
                return v
            
    def update(self,agent:Agent.Agent,card:str):
        '''
        If an agent sees a card, they know that the correct world is any world
        where card does not hold, creates an accessibility relation (AR) between 
        worlds where card does not hold.
        i.e. if agent sees "Pistol", Ka ~Pistol
        
        :param player: The agent whose AR is being updated. 
        :param card: The card (proposition) that is adding information to player's AR.
        '''
        for world in self.accessibility_relations[agent.name]:
            if card in world:
                self.accessibility_relations[agent.name].remove(world)
