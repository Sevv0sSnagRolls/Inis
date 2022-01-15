"""
MODULE - Cards Handling
---------------------------------------------------------
Uses Factory Pattern to create cards
probably a bad implementation case for it, but wanted to try it.

Constructor classes (decks) will build the correct card classes
as instanced for a game instigated by the setup function.
"""
from abc import ABC, abstractmethod


class Card(ABC):
    """
    Class to hold meta info around each card function
    name = card name for terminal/UI
    type = [action, epic, advantage]

    Every function is designed to have the same set of inputs
    as each card can have a season, triskel or both

    discard handled seperately
    """

    @abstractmethod
    def season(self, inis_game_state, player) -> "Season action":
        """
        Possible season action for the card
        """
        pass

    @abstractmethod
    def triskel(self, inis_game_state, player) -> "Triskel action":
        """
        Possible season action for the card
        """
        pass


class Conquest(Card):
    """
    Specific implementation of ABC 'card' for the conquest card
    Must return all possible actions the player can take as a formatted change of game state?
    """
    def __init__(self):
        self.name = 'Conquest'
        self.type = 'Action'
        self.blurb = "Chose 1 territory. You may move any number of your clans from territories adjacent \
                      to this chosen territory into it"

    def season(self, inis_game_state, player_id) -> 'Season action':
        actions = []
        clans_copy = inis_game_state.clans.copy()
        for tile_id, clan_qty in enumerate(inis_game_state.clans[player_id]):
            #relies on adjacent tiles being a dynamically updated list as each tile is added to the game
            #so it doesn't need to update every time a tile is added'
            for adjacent_tile_id in tiles[tile_id].adjacent_tiles:
                for i in range(0, clan_qty):
                    pass

        return actions

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class Warlord(Card):
    """
    Specific implementation of ABC 'card' for the conquest card
    Must return all possible actions the player can take as a formatted change of game state?
    """
    def __init__(self):
        self.name = 'Warlord'
        self.type = 'action'
        self.blurb =   "Season Action: \n" \
                     + " Initiate a clash in a territory where you are present with you as the instigator \n" \
                     + "OR \n" \
                     + "Triskel Action: \n" \
                     + " During a clash with you involved, after a manoeuvre is performed, \n" \
                     + " place 1 clan in the territory and choose who performs the next manoeuvre"

    def season(self, inis_game_state, player_id) -> 'Season action':
        actions = []
        clans_copy = inis_game_state.clans.copy()
        for tile_id, clan_qty in enumerate(inis_game_state.clans[player_id]):
            #relies on adjacent tiles being a dynamically updated list as each tile is added to the game
            #so it doesn't need to update every time a tile is added'
            for adjacent_tile_id in tiles[tile_id].adjacent_tiles:
                for i in range(0, clan_qty):
                    pass

        return actions

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None

    def display_card(self):
        print(self.name + ' - ' + self.type)
        print(self.blurb)


class Warlor1d(Card):
    """
    Specific implementation of ABC 'card' for the conquest card
    Must return all possible actions the player can take as a formatted change of game state?
    """
    def __init__(self):
        self.name = 'Warlord'
        self.type = 'action'
        self.blurb = "Season Action: \
                     Initiate a clash in a territory where you are present with you as the instigator \
                     or \
                     Triskel Action: \
                     During a clash with you involved, after a manoeuvre is performed, "

    def season(self, inis_game_state, player_id) -> 'Season action':
        actions = []
        clans_copy = inis_game_state.clans.copy()
        for tile_id, clan_qty in enumerate(inis_game_state.clans[player_id]):
            #relies on adjacent tiles being a dynamically updated list as each tile is added to the game
            #so it doesn't need to update every time a tile is added'
            for adjacent_tile_id in tiles[tile_id].adjacent_tiles:
                for i in range(0, clan_qty):
                    pass

        return actions

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class Warlor1d(Card):
    """
    Specific implementation of ABC 'card' for the conquest card
    Must return all possible actions the player can take as a formatted change of game state?
    """
    def __init__(self):
        self.name = 'Warlord'
        self.type = 'action'
        self.blurb = "Season Action: \
                     Initiate a clash in a territory where you are present with you as the instigator \
                     or \
                     Triskel Action: \
                     During a clash with you involved, after a manoeuvre is performed, "

    def season(self, inis_game_state, player_id) -> 'Season action':
        actions = []
        clans_copy = inis_game_state.clans.copy()
        for tile_id, clan_qty in enumerate(inis_game_state.clans[player_id]):
            #relies on adjacent tiles being a dynamically updated list as each tile is added to the game
            #so it doesn't need to update every time a tile is added'
            for adjacent_tile_id in tiles[tile_id].adjacent_tiles:
                for i in range(0, clan_qty):
                    pass

        return actions

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None




if __name__ == "__main__":
    #TEST 1 = Create Card Decks
    A = Warlord()
    A.display_card()

    #TEST 2 - Deal a Card

    #TEST 3 - Deal multiple Cards

    #TEST 4 - Deal Action Card Deck

    #TEST 5 - Deal Action Card Deck
