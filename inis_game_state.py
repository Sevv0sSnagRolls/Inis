"""
Inis Game State.py


Inis Main
- Optional Setups
- Game Type and Player selection

Game Logic -> f(gamestate)

----------
Game State
----------
  |
  - Map
  |
  = Tile Deck - Tile_0, Tile_1, Tile_2....
  |
  - Action Card Deck - Action_Card_0 , Action_Card_1
  |
  - Advantage Card Deck - Advantage_Card_0 , Advantage_Card_1
  |
  - Epic Tale Card Deck - Epic_tale_Card_0 , Epic_tale_Card_1
  |
  - Victory Conditions
  |
  - Player Agents
  |
  - Game Log

"""
import numpy as np
import random

class InisGameState:

    def __init__(self, players: dict, tile_deck: object):
        self.players = players

        #Map
        self.tile_deck = tile_deck
        self.map_size = self.tiles.size
        self.adjacent_tiles = {}

        #Components
        self.sanctuaries = np.zeros( (len(self.map_size)), dtype=int )
        self.citadels = np.zeros((len(self.map_size)), dtype=int )
        self.clans = np.zeros( (len(players), len(self.map_size)), dtype=int )
        self.chieftans = np.copy(self.map_size) #chieftan of 0 is the Brenn
        """Form of clans
                   P1 P2 P3
        clans = [ [0, 0, 0 ],   #tile 1
                  [0, 0, 0 ],   #tile 2
                  [0, 0, 0 ], ]  #tile 3 etc 
        """

        #Setup pieces - Simple quantity based methods for adding subtract from these starting values
        self.deeds_available = 12
        self.sanctuaries_available = 10
        self.citadels_available = 10

        #setup semantics
        self.player_order = []
        self.turn_direction = 1
        self.brenn = random.choice( list(self.players.keys()) )

        #Victory
        self.player_victory_conditions = []
        self.winner = None

    #Functionality for adding more attrs to class module after setup
    def add_attributes(self, **kwargs: dict) -> None:
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        return


    #Placements/Interactions----------------------------------------------
    def add_sanctuary(self, position) -> bool:
        """Add sanctuary to given tile index (in tiles dict)"""
        assert isinstance(position, np.ndarray)
        assert np.sum(position) == 1
        if self.sanctuaries_available > 0:
            self.sanctuaries_available -= 1
            self.sanctuaries = np.add(self.sanctuaries, position)
            return True
        return False

    def add_citadel(self, position) -> bool:
        """Add citadel to given tile index (in tiles dict)"""
        assert isinstance(position, np.ndarray)
        assert np.sum(position) == 1
        if self.citadels_available > 0:
            self.citadels_available -= 1
            self.sanctuaries = np.add(self.sanctuaries, position)
            return True
        return False

    def add_clans(self, player_id: int, position_qty) -> bool:
        """Add clan(s) to given tile index (in tiles dict) Bool tells whether process worked"""
        assert isinstance(position_qty, np.ndarray)
        qty = np.sum(position_qty)
        if qty > self.players[player_id].clans_available:
            print("Invalid turn, not enough clans remaining")
            return False
        self.clans[player_id] = np.add(self.clans[player_id], position_qty)
        self.deeds_available -= qty
        return True

    def take_deed(self, player_id) -> bool:
        """Give player a deed token. Bool tells whether process worked"""
        if self.deeds_available > 0:
            self.players[player_id].deeds += 1
            return True
        return False


    # Placements/Interactions----------------------------------------------
    def __find_chieftans(self):
        """returns player with max clans in each tile, if max has two values. Sets to 0"""
        m, _ = np.shape(self.clans)
        for i in range(0, m):
            maxes = np.where(self.clans[i] == np.amax(self.clans[i]))[0]
            if len(maxes) == 1:
                self.chieftans[i] = maxes[0]
            elif len(maxes) > 1 and i != 0:
                """Brenn stays Brenn, others get changed"""
                self.chieftans[i] = -1
        self.brenn = self.chieftans[0]

    def __assign_advantage_cards(self):
        """Uses tile_index:advantage card pairing to deal cards to chieftans"""
        for tile_index, chieftan_index in enumerate(self.chieftans):
            if chieftan_index >= 0: #check for actual existance [-1 is noone is cheiftan]
                tile = self.tiles[tile_index]
                advantage_card = self.tile_advantage_pairs(tile)
                self.players[chieftan_index].deal_card(advantage_card)

    def __flip_crows_token(self):
        """Creates new player order"""
        self.previous_turn_direction = self.turn_direction
        a = self.players.copy()
        K = self.brenn
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
        """"""
        for player in self.players:
            pass

    def find_victory_conditions(self, player_id: int):
        """"""
        self.victory_exploration(player_id)
        self.victory_cheiftan(player_id)
        self.victory_sanctuaries(player_id)
        return

    def victory_exploration(self, player_id: int):
        """Needs to be in 6 different territories"""
        explored = [i for i, e in enumerate(self.clans[:, player_id]) if e > 0]
        victory = True if explored >= 6 else False
        return victory, len(explored), explored

    def victory_sanctuaries(self, player_id: int):
        """Needs to be in territories with 6 Sacntuaries total"""
        sanctuaries = np.multiply(clans[player] / clans[player_id], self.sanctuaires)
        qty_sanctuaries = np.sum(sanctuaries)
        victory = True if qty_sanctuaries >= 6 else False
        return victory, qty_sanctuaries, sanctuaries

    def victory_cheiftan(self, player_id: int):
        """Needs to be chieftan over atleast 6 other clans"""
        clans_ruled_over = np.zeros((len(self.tiles), 1), dtype=int)
        for i, e in enumerate(clans_ruled_over):
            if np.argmax(clans[:, i]) == clans[player_id][i]:
                clans_ruled_over[i] = np.sum(clans[:, i]) - clans[player_id][i]
        qty_clans_ruled_over = np.sum(clans_ruled_over)
        victory = True if qty_clans_ruled_over >= 6 else False
        return victory, qty_clans_ruled_over, clans_ruled_over



