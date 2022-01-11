"""
Module which holds a class that contains all information about the game state
There are a few methods on the class itself, but the core struct is small so should be fast to copy()
"""
import itertools

class inis_game_state():

    def __init__(self, players: list, map_x:int=20, map_y:int=20,):
        #Depreciated, players list handled elsewhere
        #Handle to each player object created
        #Players list needs to be immutable - convert to a set
        #this means player order can change, but as list indexing is used by player id which is also
        #the position in a list because I'm lazy, better to make this data structure a const
        self.players = set( players )
        self.player_victory_conditions = []

        #Map representation
        #I Cheat and initialise a map bigger than the board can become
        #this might have an effect later on, but should be okay for now... also wastes memory
        #Each element in the map array is 1/3 of a tile. This allows for "easy" adjacency calculations
        #assuming offset rows and a bunch of janky stufd
        self.map = np.zeros((map_x, map_y),
                            dtype=int)

        # Inis_game_state holds a method to find adjacent tiles and has a dictionary component which keeps
        # this information up to date
        # dictionary of form { tile_id : [adj_tile_id, adj_tile_id....], tile_id_2, [], ... }
        self.adjacent_tiles = {}

        #setup placement of pieces based off of map
        self.capitals = np.zeros(int(map_x * map_y / 3))
        self.sanctuaires = np.copy(self.capitals)
        self.citadels = np.copy(self.capitals)
        self.clans = np.zeros((len(players), map_x, map_y), dtype=int)

        #Setup pieces - Simple quantity based methods for adding subtract from these starting values
        self.deeds_available = 12
        self.sanctuaries_available = 10
        self.citadels_available = 10

        #setup semantics
        self.player_order = []
        self.bren = random.choice[self.players]  # initialise for wtv purpose
        self.turn_direction = 1
        self.winner = None

    def add_game_logger(self, game_events_logger):
        self.game_event_logger = game_events_logger

    def add_game_decks(self, action_deck, epic_tale_deck, advantage_deck):
        self.action_cards = action_deck
        self.epic_tale_cards = epic_tale_deck
        self.advantage_cards = advantage_deck

    def add_tile_deck(self, tile_deck):
        #Tiles - References to instances of tile classes which make up the board
        #Tile index in the tiles list is the identifier used in the map matrix to allocate tile positions
        #Inis_game_state holds a method to find adjacent tiles and has a dictionary component which keeps
        #this information up to date
        self.tiles = tile_deck

    def find_chieftans(self, players):
        '''
        returns index relating to player with max clans in capital
        if max has two values, returns previous Bren
        '''
        for x, y in itertools.product():

        if
            return index.max()
        else:
            return None

    def find_bren(self, players):
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


if __name__ == "__main__":
    #TESTS


