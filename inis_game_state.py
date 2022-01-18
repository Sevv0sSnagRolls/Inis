"""
Module which holds a class that contains all information about the game state
There are a few methods on the class itself, but the core struct is small so should be fast to copy()

Adjacent Tiles
# Inis_game_state holds a method to find adjacent tiles and has a dictionary component which keeps
        # this information up to date
        # dictionary of form { tile_id : [adj_tile_id, adj_tile_id....], tile_id_2, [], ... }

Player vzictory Conditions
#unsure how to store this right now...


"""
import numpy as np
import itertools
from inis_decks import inis_card_deck
from inis_game_log import game_logger
from inis_tiles import create_tiles
import inis_player_agents
import random

class inis_game_state():

    def __init__(self, players: dict, map_x:int=15, map_y:int=15):
        self.players = players

        #Map
        self.map = np.zeros((map_x, map_y),
                            dtype=int)
        self.adjacent_tiles = {}

        #setup placement of pieces based off of map
        self.capitals = np.zeros(int(map_x * map_y / 3))
        self.sanctuaries = np.copy(self.capitals)
        self.citadels = np.copy(self.capitals)
        self.clans = np.zeros((len(players), map_x, map_y), dtype=int)

        #Setup pieces - Simple quantity based methods for adding subtract from these starting values
        self.deeds_available = 12
        self.sanctuaries_available = 10
        self.citadels_available = 10

        #setup semantics
        self.player_order = []
        self.turn_direction = 1
        self.brenn = random.choice[self.players.keys()]

        #Victory
        self.player_victory_conditions = []
        self.winner = None

        #MAP
        """

        """

    #Functionality for adding more attrs to class module after setup
    def add_attributes(self, **kwargs: dict) -> None:
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        return

    #Map
    def add_tile(self):
        """adds tile in new position and updates length off all the vars: sancts etc"""

        pass

    def find_adjacent_tiles(self):
        pass

    def find_available_exploration_locations(self):
        pass

    #Placements/Interactions----------------------------------------------
    def add_sanctuary(self, position:int) -> bool:
        """Add sanctuary to given tile index (in tiles dict)"""
        if self.sanctuaries_available > 0:
            self.sanctuaries[position] += 1
            return True
        return False

    def add_citadel(self, position:int) -> bool:
        """Add citadel to given tile index (in tiles dict)"""
        if self.citadels_available > 0:
            self.citadels[position] += 1
            return True
        return False

    def add_clans(self, player_id: int, qt, position:int) -> bool:
        """Add clan(s) to given tile index (in tiles dict)"""
        if qty > self.players[player_id].clans_available:
            print("Invalid turn, not enough clans remaining")
            return False
        if self.sanctuaries_available > 0:
            self.sanctuaries[position] += 1
        return

    def take_deed(self, player_id):
        """Give player a deed token"""
        if self.deeds_available > 0:
            self.players[player_id].deeds += 1
        return

    # Placements/Interactions----------------------------------------------
    def find_chieftans(self):
        """returns player with max clans in each tile, if max has two values"""
        for clan in self.clans:
            pass
        if
            return index.max()
        else:
            return None

    def find_bren(self):
        return find_cheiftan(self.capital)

    def assign_advantage_cards(self):
        for player in inis.players:
            for x in range:
                for y in range:
                    if chieftan == player:
                        player.add_card()
        return

    def flip_crows_token(self):
        """
        Flip crows token performs a few functions
        1) Stores - Last state of token direction - i.e [-1,1]
        2) Finds the new player order for the turn based off of the current Bren

        :returns: basically creates a player order for the turn based off of who is the Bren for
        the current turn, must be called after the bren is found
        """
        #1---
        self.previous_turn_direction = self.turn_direction

        #2---
        a = self.players.copy()
        K = self.bren
        f = random.choice([-1, 1])
        self.turn_direction = f
        if f == -1:
            self.player_order = [a[(K + i * f)] for i in range(1, len(a))]
        else:
            self.player_order = [a[(K + i * f) % len(a)] for i in range(1, len(a))]
        return

    def assembly_phase_check_for_victory(self):
        '''
        Sorts out victory

        1) evaluate every players current victory conditions against rules
        2) add deed tokens to each player
        3) check for victory and resolve ties
        :return: victor
        '''
        if player.has_pretender_token()
            self.find_victory_conditions()

        return winner

    def check_victory_conditions(self, player_id: int):
        """
        Updates for all players in a data object which everyone can view (as it's not hidden information)
        Will do this at the start of every round
        """
        for player in self.players:
            pass

    def find_victory_conditions(self, player_id: int):
        '''
        Reason its kept in game class is because every player wants to know
        every other players victory conditions at every stage of the game
        and also their 'distance' to victory
        Find_victory_conditions will add the deed tokens seperately
        Will also display to terminal text of how player wins
        :return:
        '''
        self.victory_exploration(player_id)
        self.victory_cheiftan(player_id)
        self.victory_sanctuaries(player_id)
        return

    def victory_exploration(self, player_id: int):
        '''
        Checks the exploration victory condition
        Gives how many have been explored and which ones
        Returns [False/True, Qty Explored, TilesExplored]
        All relies on sparse tiles array being large enough and
        placements allowable functions not allocating clans to tiles that don't exist
        '''
        explored = [i for i, _ in enumerate(clans[player_id]) if e > 0]
        victory = True if explored >= 6 else False
        return victory, len(explored), explored

    def victory_sanctuaries(self, player_id: int):
        '''
        Checks player position against each sanctuary
        Uses a bit of array maths to make things ez
        '''
        sanctuaries = np.multiply(clans[player] / clans[player_id], self.sanctuaires)
        qty_sanctuaries = np.sum(sanctuaries)
        victory = True if qty_sanctuaries >= 6 else False
        return victory, qty_sanctuaries, sanctuaries

    def victory_cheiftan(self, player_id: int):
        '''
        Needs to be chieftan over atleast 6 other clans
        Use array maths in the clans object
        returns T/F, qty, which tiles they are in and how many from each
        '''
        clans_ruled_over = np.zeros((len(self.tiles), 1), dtype=int)
        for i, e in enumerate(clans_ruled_over):
            if np.argmax(clans[:, i]) == clans[player_id][i]:
                clans_ruled_over[i] = np.sum(clans[:, i]) - clans[player_id][i]
        qty_clans_ruled_over = np.sum(clans_ruled_over)
        victory = True if qty_clans_ruled_over >= 6 else False
        return victory, qty_clans_ruled_over, clans_ruled_over


    @classmethod
    def setup_inis(cls, player_agents:dict) -> object:
        """
        Sets up game state variable and dependencies based on players
        """
        if not self.validate_player_agents(player_agents):
            raise Exception("One or more player agents are incorrectly built or referenced")
        player_agent_instances = build_player_reference_instances_and_connect_to_agents( player_agents )
        build_player_reference_instances_and_connect_to_agents( player_agents )
        current_game_state = setup_inis_instance( player_agent_instances, logging=True )

        #setup_game_board(current_game_state)

        #setup fake games for the players for sims...
        #
        #...
        #
        return current_game_state

    def __setup_inis_instance(player_agents: dict, logging: bool = False) -> object:
        """
        Function to construct Inis instances
        Variability is whethe the player agents are the real ones or fake ones/sims
        which the agents can use to simulate the game from the current game state
        Functionality in the game state class is copying to other game state instances
        :param player_agents:
        :rtype: object
        :return:
        """
        if validate_player_agents(player_agents) == False:
            raise Exception("One or more player agents are incorrectly built or referenced")
        n = len(player_agents)
        game_state_instance = inis_game_state( player_agents )
        tiles = create_tiles()
        action_deck, epic_tale_deck, advantage_deck = build_decks(n)
        tile_advantage_pairs = connect_tiles_and_advantage_cards(tiles, advantage_deck)
        kwargs = {}
        if logging:
            kwargs.update( { 'game_log': game_logger() } )
        kwargs.update( {
                         'tile_deck' : tiles,
                         'action_deck': action_deck,
                         'epic_tale_deck': epic_tale_deck,
                         'advantage_deck' : advantage_deck,
                         'tile_advantage_pairs' : tile_advantage_pairs
                        } )
        return game_state_instance


    def __setup_game_board(self, inis_game_state: object):
        """
        Initial Tile Draw
        Initial Clan Placement
        Will just randomise Capital Territory for now
        Capital can just be tile index 0 for ease of my life... maybe this is dumb
        :return:
        """
        place_initial_tiles(inis_game_state)

        for player in inis_game_state.players:
            pass


    def __place_initial_tiles(self, inis_game_state):
        """
        Tile deck can probably be built from the same class as all the other decks...
        :return:
        """
        initial_tiles = [inis_game_state.tile_deck.draw_tile() for i in range(0, len(inis_game_state.players)) ]
        starting_position = int(inis_game_state.x/2), int(inis_game_state.y/2)

        return initial_tiles

    @staticmethod
    def __validate_player_agents(player_agents) -> bool:
        """
        Needs to check it fits the form of tha ABC created in the inis_player_agents file?
        :param player_agents:
        :return:
        """
        return True

    @staticmethod
    def __build_player_reference_instances_and_connect_to_agents(player_agents: dict) -> None:
        """
        As long as player agents passed into the game are correctly keyworded etc
        will call a class based off of their name to construct a player and agent class
        to play the game
        :param player_agents:
        :return: players -> a list of object references to agent instances which
                            contain player instances as a class parameter
        """

        for player_id, player_agent in player_agents.items():
            player_references = { { key : inis_player_agents.dumbass_test_agent( key,
                                   player_agents[key].name ) } for key in player_agents.keys()
                                   if key != player_id }
            player_agent.player_references = player_references.copy()
        return

    @staticmethod
    def __connect_tiles_and_advantage_cards(tile_deck: object, advantage_deck: object) -> dict:
        """
        Tile deck and advantage cards are created independently
        Need to connect the tile object to the card to bring the card into play
        when the tile is drawn
        reliance is on both sets of classes being correctly named in accordance with TILES
        list object in inis_constants.py
        :param tile_deck: object that holds info about all tile object
                parameter to get this info out is '.tiles'
        :param advantage_deck: object that hold info about all advantage cards
                parameter to get this info out is '.cards'
        :return: dict of the object references which inis_game_state can use to find and assign cards etc
        """
        assert 'tiles' in dir(tile_deck)
        assert 'cards' in dir(advantage_deck)

        tile_card_pairs = dict( (tile, card) for tile in tile_deck.tiles \
                                for card in advantage_deck.cards if tile.name == card.name)
        return tile_card_pairs




class victory_conditions():
    """
    Hold information about each victory condition for each player
    """
    def __init__(self, player_id, condition):
        self.player_id = player_id
        self.condition = condition
        self.victory = False
        self.qty = 0
        self.positions = []

    def update_victory_conditions(self, victory_bool, qty, positions):
        self.victory = victory_bool
        self.qty = qty
        self.positions = positions


if __name__=="__main__":
    #Test 1 - Build a new game setup?

    player_0 = {
                'name' : 'Doug',
                'player_agent' : inis_player_agents.dumbass_test_agent()
                }

    player_1 = {
                'name' : 'John',
                'player_agent' : inis_player_agents.dumbass_test_agent()
                }

    player_2 = {
                'name' : 'Brad',
                'player_agent' : inis_player_agents.dumbass_test_agent()
                }

    player_3 = {
                'name' : 'Test 2',
                'player_agent' : inis_player_agents.dumbass_test_agent()
                }

    player_agents = {
                      0: player_0,
                      1: player_1,
                      2: player_2,
                      3: player_3
                    }

    setup_inis(player_agents)


