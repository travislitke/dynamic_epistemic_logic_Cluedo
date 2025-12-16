class Kripke():
    
    def __init__(self):
        self.possible_worlds = []
        self.accessibility_relations = []
        
class PossibleWorld():
    
    def __init__(self, props:tuple):
        self.props = props
            