"""
TILES
----------------------------------------------------
Module to hold tile objects for inis game

Tiles will have their own functions related to them?

Cards related to tiles will be handled seperately...
"""

import random
from abc import ABC, abstractmethod
import traceback


class _TileDeck:

    def __init__(self, tiles: list):
        self.undrawn = tiles
        self.drawn = []

    def draw_tile(self):
        if len(self.undrawn) > 0:
            self.drawn.append(self.undrawn.pop())
            return self.drawn[-1]
        return None


class _Tile(ABC):

    @abstractmethod
    def tile_action(self, inis_game_state):
        """
        Specific tile action to be resolved
        :return: changes to game state...
        """
        pass


class _TileTypes:
    """
    Meta class for holding types of tiles dervived from tile ABC
    for the process director to create

    Probably not a great idea using inner classes.. oh well
    """

    class _StandardTile(_Tile):
        '''
        Base type for any tile that just has a name no action
        '''
        def __init__(self, name):
            self.name = name

        def tile_action(self, inis_game_state):
            return None

    class _Mountains(_Tile):
        """
        When one or more clans are moved into this territory,
        Player who moved in must discard one clan or one action card
        """
        def __init__(self, name):
            self.name = name

        def tile_action(self, inis_game_state):
            if inis_game_state.turn_direction != inis_game_state.previous_turn_direction:
                tile_location = inis_game_state.tiles([])
            return None

    class _GatesOfTirNaNog(_Tile):
        """
        Starts with a sanctuary
        If turn direction changes, each player in lands loses a clan and gets an epic tale
        Cheiftan has advantage card for this. Make sure turn order allows that... jfc
        """
        def __init__(self, name):
            self.name = name

        def tile_action(self, inis_game_state):
            if inis_game_state.turn_direction != inis_game_state.previous_turn_direction:
                tile_location = inis_game_state.tiles([])
            return None

    class _StoneCircle(_Tile):
        """
        Starts with a sanctuary
        """
        def __init__(self, name):
            self.name = name

        def tile_action(self, inis_game_state):
            if inis_game_state.turn_direction != inis_game_state.previous_turn_direction:
                tile_location = inis_game_state.tiles([])
            return None


class _ProcessDirector:
    '''
    Class to handle automatic generation of tiles from dict of:
    (name, str(class_type)) pairs to use builder pattern to generate
    any sort of tiles etc.
    '''
    def __init__(self):
        self.tiles = []

    def construct(self, builder_name: str, name: str) -> object:
        name.strip('_') #just incase I mislabel based of hidden/non important class names
        try:
            target_class = getattr(_TileTypes(), '_' + builder_name)
            instance = target_class(name)
            self.tiles.append( instance )
        except AttributeError:
            print("Builder {} not defined.".format(builder_name))
            traceback.print_stack()


def create_tiles() -> object:
    '''
    Actual function called to make tiles
    :return:
    '''
    import inis_constants
    tiles = inis_constants.TILES.copy()
    random.shuffle(tiles)
    director = _ProcessDirector()
    [director.construct(tile[1], tile[0]) for tile in tiles]
    return _TileDeck( director.tiles )


if __name__ == "__main__":
    tile_deck = create_tiles()
    for i in range(0, len(tile_deck.undrawn)):
        a = tile_deck.draw_tile()
        print( a.name )








