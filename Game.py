import logging
import random
from typing import Optional
from Agent import Agent as player
from Deck import Card, Deck
import KnowledgeGraph

CHARACTERS = ["Plum","White","Scarlet","Green","Mustard","Peacock"]
WEAPONS = ["Rope","Dagger","Wrench","Pistol","Candlestick","Lead Pipe"]
ROOMS = ["Courtyard","Game Room","Study","Dining Room","Garage","Living Room","Kitchen","Bedroom","Bathroom"]

class Game():
    def __init__(self, num_players:int, log_accessibility:bool=False) -> None:
        self.log_ar = log_accessibility
        if num_players < 2 or num_players > 6:
            raise ValueError("Requires 2-6 players!")
        self.num_players = num_players
        self.active_players = [player(f"a{i+1}") for i in range(num_players)]
        # init and shuffle deck
        self.deck=Deck()
        self.deck.fy_shuffle()
        #solution is first of each card type in deck:        
        self.solution = self.deck.generate_solution()
        self.kripke_model = KnowledgeGraph.Kripke(self.solution,self.active_players)
        
        self.game_stats={
            "Solution":self.solution,
            "Num Players":self.num_players,
            "Winner":None,
            "Eliminations":0,
            "Num Rounds":0
        }


    def __str__(self):
        return f"Clue game with {self.num_players} player(s)."
    
    '''
    Cards are deal out to players so that each player has 
    an equal amount and there are fewer remaining cards than
    active players. 
    '''
    def deal(self):
        logging.info(f"Dealing to each player. Each player should have {int(len(self.deck.cards)/self.num_players)} cards, with {len(self.deck.cards)%self.num_players} leftover cards.")
        cards_in_deck = len(self.deck.cards)
        while cards_in_deck >= self.num_players:
            for player in self.active_players:
                top_card = self.deck.cards.pop(0)
                player.take_card(top_card)
                player.see_card(top_card)
                self.kripke_model.update(agent=player,card=top_card)
                cards_in_deck -= 1
                
        assert(cards_in_deck==(18%self.num_players))
    
        

    def question_players(self, player, suggestion:tuple):
        opponents = [other for other in self.active_players if other != player]
        for opponent in opponents:
            card_names = [card.name for card in opponent.hand]
            if suggestion[0] in card_names or suggestion[1] in card_names or suggestion[2] in card_names:
                return opponent
        return None
    
    
    def suggest(self, player):
        # move to a room
        room = random.choice(player.possible_rooms)
        logging.info(f"Agent {player.name} has entered the {room}.")
        # make a suggestion
        suspect = random.choice(player.possible_suspects)
        weapon = random.choice(player.possible_weapons)
        suggestion = (suspect, weapon, room)
        
        logging.info(f"Agent {player.name} suggests {suspect} with the {weapon} in the {room}.")
        
        return suggestion

    
    def propose(self, player, proposal: tuple[str,...])-> bool:
        logging.info(f"Agent {player.name} has proposed {proposal}.")
        if proposal == self.solution:
            logging.info(f"Agent {player.name} has solved the mystery.")
            self.game_stats["Winner"] = player.name
            self.active_players.clear()
            return True
        else:
            self.active_players.remove(player)
            self.game_stats['Eliminations'] += 1
            logging.info(f"Agent {player.name} has made an incorrect proposal and has been eliminated from the game.")
            return False
    
    def play(self):

        self.deal()
        
        if self.log_ar:
            for player in self.active_players:
                logging.info(f"Agent {player.name} updated accessibility relations:\n{self.kripke_model.accessibility_relations[player.name]}")
        '''
        All remaining cards are shown to players (per Clue rules).
        '''
        for player in self.active_players:
            for card in self.deck.cards:
                player.see_card(card)
                self.kripke_model.update(agent=player,card=card)
                if self.log_ar:
                    logging.info(f"Agent {player.name} updated accessibility relations:\n{self.kripke_model.accessibility_relations[player.name]}")
            assert(len(self.kripke_model.accessibility_relations[player.name])<9*6*6)        
        
        while len(self.active_players) > 1:
            # update game state
            self.game_stats['Num Rounds']+=1
            
            # each player takes a turn
            for player in self.active_players:
                assert((self.kripke_model.actual_world,self.kripke_model.actual_world) in self.kripke_model.accessibility_relations[player.name])
                
                # logic loop if player hasn't solved the murder yet
                if len(self.kripke_model.accessibility_relations[player.name]) > 1:
                    suggestion = self.suggest(player=player)
                    other_char = self.question_players(player,suggestion)
                    # if any other character has a card from the player's suggestion:
                    if other_char != None:
                        # see one matching card
                        for card in other_char.hand:
                            if card.name in suggestion:
                                logging.info(f"Agent {other_char.name} shows Agent {player.name} {card}.")
                                player.see_card(card)
                                self.kripke_model.update(agent=player,card=card)
                                if self.log_ar:
                                    logging.info(f"Agent {player.name} updated accessibility relations:\n{self.kripke_model.accessibility_relations[player.name]}")
                                break
                    else:
                        # if no players have any matching cards, murder solved! 
                        logging.info(f"All other players remain silent. Agent {player.name} has deduced the solution.")
                        # Eliminate all possible worlds that don't involve any element of the suggestion
                        self.kripke_model.deduce(agent=player,suggestion=suggestion)
                        self.propose(player=player,proposal=suggestion)

                else:
                    # propose a solution
                    logging.info(f"Agent {player.name} has eliminated all uncertainty about possible worlds.")
                    final_possible_world = str(self.kripke_model.accessibility_relations[player.name][0][0])
                    proposal=self.kripke_model.possible_worlds[final_possible_world]
                    solved = self.propose(player,proposal=proposal)
                    if solved:
                        break
        
