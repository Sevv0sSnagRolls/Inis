import logging

class inis()

    def __init__(self, players, map_x=20, map_y=20):
        self.log = []

        # unique ID of each player created 0,1,2,3,4...
        # these are also the index of the clans placement array
        self.players = players
        self.winner = None
        self.player_order = []
        self.bren = random.choice[players]  # initialise for wtv purpose
        self.turn_direction = 1

        # map constants
        self.map = np.zeros((map_x, map_y),
                            dtype=int)  # cheat an initialise a map bigger than the board can become (spare array)
        self.tiles = []  # empty list of tile objects which will be added in order as reference to each tile
        self.capitals = np.zeros(int(map_x * map_y / 3))
        self.sanctuaires = np.copy(self.capitals)
        self.citadels = np.copy(self.capitals)
        self.clans = np.zeros((len(players), map_x, map_y), dtype=int)

        # extras
        self.deeds_available = 12
        self.sanctuaries_available = 10
        self.citadels_available = 10

        # cards
        self.action_cards = action_deck
        self.epic_tale_cards = epic_tale_deck

        # ID of tile relates to ID of advantage cards
        self.advantage_cards = advantage_card_deck

    def find_chieftans(self, tile):
        '''
        returns index relating to player with max clans in capital
        if max has two values, returns previous Bren
        '''
        for x, y in itertools.product():

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

    def check_victory_conditions(self):
        """
        Updates for all players in a data object which everyone can view (as it's not hidden information)
        Will do this at the start of every round
        """
        for player in self.players:
            pass

    def find_victory_conditions(self, player):
        '''
        Reason its kept in game class is because every player wants to know
        every other players victory conditions at every stage of the game
        and also their 'distance' to victory
        Find_victory_conditions will add the deed tokens seperately
        Will also display to terminal text of how player wins
        :return:
        '''
        self.victory_exploration()
        self.victory_cheiftan()
        self.victory_sanctuaries()
        return

    def victory_exploration(self, player):
        '''
        Checks the exploration victory condition
        Gives how many have been explored and which ones
        Returns [False/True, Qty Explored, TilesExplored]
        All relies on sparse tiles array being large enough and
        placements allowable functions not allocating clans to tiles that don't exist
        '''
        explored = [i for i, _ in enumerate(clans[player]) if e > 0]
        victory = True if explored >= 6 else False
        return victory, len(explored), explored

    def victory_sanctuaries(self, player):
        '''
        Checks player position against each sanctuary
        Uses a bit of array maths to make things ez
        '''
        sanctuaries = np.multiply(clans[player] / clans[player], self.sanctuaires)
        qty_sanctuaries = np.sum(sanctuaries)
        victory = True if qty_sanctuaries >= 6 else False
        return victory, qty_sanctuaries, sanctuaries

    def victory_cheiftan(self, player):
        '''
        Needs to be chieftan over atleast 6 other clans
        Use array maths in the clans object
        returns T/F, qty, which tiles they are in and how many from each
        '''
        clans_ruled = np.zeros((len(self.tiles), 1), dtype=int)
        for i, e in enumerate(clans_ruled):
            if np.argmax(clans[:, i]) == clans[player][i]:
                clans_ruled[i] = np.sum(clans[:, i]) - clans[player][i]
        qty_clans_ruled = np.sum(clans_ruled)
        victory = True if qty_clans_ruled >= 6 else False
        return victory, qty_clans_ruled, clans_ruled



if __name__ == "__main__":
    #TESTS
    game = inis(2)

    #check

    #check map build

    #check victory conditions
    player0 = player(0)
    player1 = player(1)



