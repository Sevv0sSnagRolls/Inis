import random
import numpy as np


# #actually stupid, maybe matrix rep was better....
# class Map:
#     """
#     Actually had a stroke making this. Seems fucking dumb
#     """
#
#     def __init__(self, l:int, initial_tiles: dict, r=1, initial_point=np.array( [0.0,0.0] ),
#                 hex_grid_orientation=np.pi/2):
#
#         #l is the length of the tile deck/number of lands to make sure arrays have correct mem size
#         #C based
#         self.l = l
#
#         # dict (index of tile: tileobjectinstance)
#         self.tile_objects = initial_tiles
#
#         #bundle tiles by index into groups of three
#         self.tiles_positions = np.inf*np.ones( (self.l, 3, 2) )
#
#         self.r = r
#         self.initial_point = initial_point
#         self.hex_grid_orientation = hex_grid_orientation
#         self.hex_frontier = []
#         self.explored_tile_positions = np.empty( (self.l, 2) )
#
#         # dodgy pointer to tiles location....
#         self.tiles_in_game_index = 0
#
#         #np.array( [hex_x, hex_y], [hex_x2, ...], ....)
#         self.renderHexGrid(self.hex_frontier, self.r)
#
#         self.__initialise()
#
#     def player_select_tile(self, player:object, tile:object):
#         """interface for external objects for players to generate exploration locations"""
#         options = self.__generate_placement_options()
#         selected_position = self.__prompt_player_selection(player, options)
#         self.__add_tile_to_instance(selected_position, tile)
#
#     def __select_tile_random(self, tile: dict):
#         """Returns a list of positble locations to place the tile. Player will then select as handled by game"""
#         options = self.explore_hex_frontier()
#         self.__add_tile_to_instance(random.choice(options), tile)
#         return random.choice(options)
#
#     def __add_tile_to_instance(self, positions, tile:dict):
#         self.tiles_in_game_index += 1
#         self.tiles_positions[self.i] = positions
#         self.tile_objects.update(tile)
#
#     def __initialise(self):
#         """Give everything a starting value to allow exploration function to work"""
#         #self.tiles[self.tiles_in_game] = self.hex_frontier
#         #add two more random tiles
#         self.hex_centres(self.inital_point, self.hex_grid_orientation, r, qty=3)
#         for i in range(1, len(self.tile_objects)):
#             self.__select_tile_random(self, self.tile_objects[i])
#         print(self.tiles)
#
#     def __explore_hex_frontier(self):
#         """Find new adj tile locations, return list of options"""
#         """Currently inefficient, hoping to add frontier element to reduce iterating over 'landlocked' hexes"""
#         possible_locations = []
#         self.__update_explored_tiles()
#         for tile in self.explored_tile_positions:
#             for adj_pos in self.hex_centres(tile, self.hex_grid_orientation, 6, self.r):
#                 # find distances and if it already exists
#                 c = np.linalg.norm(np.subtract(self.explored_tile_positions, adj_pos), axis=1)
#                 if np.size(np.where(c==0)) == 0:
#                     if np.size(np.where((c-self.r-10**-9) <= 0)) >= 2:
#                         possible_locations.append(adj_pos)
#                         print(possible_locations)
#                     else:
#                         self.hex_frontier.append(adj_pos)
#         return possible_locations
#
#     def __generate_placement_options(self, initialise=False):
#         """Takes hexes, check adjaceny to existing hexes"""
#         options = self.explore_hex_frontier()
#         #for option in options:
#         #im not doing this complex shit for now jfc
#         pass
#
#
#
#     def __prompt_player_selection(self, player:object, options: list) -> 'numpy array':
#         """Handles player selection and validation. Player class need method select tile..."""
#         i = 0
#         selection_valid = False
#         selected_tile_location = np.empty((2,1))
#         while not selection_valid or i <= 10:
#             selected_tile_location = player.select_tile(options)
#             if selected_tile_location in options:
#                 selection_valid = True
#             if i == 10:
#                 print('Too many invalid selections for tile location')
#             i += 1
#         return True, selected_tile_location
#
#     def __update_explored_tiles(self):
#         self.explored_tile_positions = [exp for tile in self.tiles for exp in tile]
#
#     @staticmethod
#     def hex_centres(hex_centre, hex_grid_orientation, r:float, qty=6):
#         """Eavluates hexes around a point based off start rotation etc"""
#         return np.add( np.array( [ [ r*np.cos(i*2*np.pi/qty + hex_grid_orientation),
#                                      r*np.sin(i*2*np.pi/qty + hex_grid_orientation) ]
#                                      for i in range(0, qty) ] ), hex_centre )
#
#     def renderHexGrid(self, hex_centres, radius):
#         fig, ax = plt.subplots()
#         patches = []
#         for hex in hex_centres:
#             patches.append(mpatches.RegularPolygon(hex, 6, radius) )
#         collection = PatchCollection(patches)
#         ax.add_collection(collection)
#         plt.autoscale()
#         plt.show()
# """


class Map:

    map_buffer_extender = 2 #common between all classes
    hex = np.array([[1, 1], [1, 0]])
    hex_patterns = [np.rot90(hex, k) for k in range(0, 4)]

    def __init__(self, x:int=3, r=1):

        self.x = x
        self.y = x
        self.maprep = -1*np.ones((self.x,self.y),dtype=int)
        self.r = r

        #Pattern of connections to other indicies 1 - odd rows
        # \ |
        # --i--
        # / |
        #[i-1][j-1], [i-1][j]
        #[i][j-1],   [i][j+1]
        #[i+1][j-1], [i+1][j]
        self.pattern_1 = np.array([[-1, 0],
                              [-1, 1],
                              [0, -1],
                              [0, 1],
                              [1, 0],
                              [1, 1]], dtype=int)

        # Pattern of connections to other indicies 2 - even rows
        #   | /
        # --i--
        #   | \
        # [i-1][j], [i-1][j+1]
        # [i][j-1], [i][j+1]
        # [i+1][j], [i+1][j+1]
        self.pattern_2 = np.array([ [-1, 0],
                               [-1, 1],
                               [0, -1],
                               [0, 1],
                               [1, 0],
                               [1, 1] ], dtype=int )

        initial_tile =

    def player_add_tile(self):
        options = self.__generate_placement_options()
        selected_position = self.__prompt_player_selection(player, options)
        self.__add_tile_to_instance(selected_position, tile)

    def __prompt_player_selection(self, player: object, options: list) -> 'numpy array':
        """Handles player selection and validation. Player class need method select tile..."""
        i = 0
        selection_valid = False
        selected_tile_location = np.empty((2,1))
        while not selection_valid or i <= 10:
            selected_tile_location = player.select_tile(options)
            if selected_tile_location in options:
                print('Selection Invalid')
                selection_valid = True
            if i == 10:
                print('Too many invalid selections for tile location')
            i += 1
        return selected_tile_location

    def initial_map_layout(self, TileDeck):


    def generate_tile_placement_options(self):
        """Generates all permutations of positions new tile can go"""
        for loc in self._valid_adj_tile_locations():



    def _valid_adj_tile_locations(self):
        """Finds Adj tile locations adj to atleast two existing tiles"""
        valid_locations = []
        existing = np.transpose(np.nonzero(self.maprep > 0))
        for location in np.transpose(np.nonzero(self.maprep > 0)):
            adjs = np.add(self.patterns(location[0]), location)

            for adj in adjs:
                distances = self.array_distances(existing, adj)
                #check if it's already in the existing points
                if np.size(np.where(distances == 0)):
                    #check if its adjacent to atleast two existing points
                    if np.size( np.where( distances == self.r )) == 2:
                        valid_locations.append(adj)
                    # else:
                    #     #if hex is not adj to two, but is next to existing etc,
                    # way too hard fuck this
                    #     self.frontier.append(adj)
        return valid_locations

    def find_adj(self, mapArray, existing):
        """Finds points adjacent in map array for each element in existing array"""
        m, _ = np.shape(existing)
        #3d array, one set of 6 adj 2D points for each existing point
        adjs = np.add(np.ones((m,6 2), dtype=int), existing)
        adjs = np.add(self.patterns(location[0]), location)


    @staticmethod
    def array_distances(array, point):
        """Finds distance between array and a point"""
        return np.linalg.norm(np.subtract(array, point), axis=1)

    def check_map_size(self):
        """checks and increases size as map gets explored to the edges"""
        buffer_check = np.sum(self.maprep[:,0])  + \
                       np.sum(self.maprep[:,-1]) + \
                       np.sum(self.maprep[0,:])  + \
                       np.sum(self.maprep[-1,:])
        if buffer_check > 0:
            self.extend_map()

    def extend_map(self):
        """add a column and a row buffer around the entire map"""
        self.x += map_rep.extender
        self.y += extender
        new_map = -1*np.ones((self.x, self.y), dtype=int)
        newmap[1:-1,1:-1] = self.maprep.copy()
        self.maprep = new_map

    def patterns(self, row_index):
        """way of converting vertical hex grids into matrcies"""
        if row_index % 2 == 1:
            return self.pattern_1
        return self.pattern_2


if __name__ == '__main__':
    """
    a = testclass.testcard()
    print(a.name)
    b = testclass.testcard2()
    print(a.qty_sanctuaries)
    print(b.qty_sanctuaries)
    testclass.sanctuaries()
    print(a.qty_sanctuaries)
    print(b.qty_sanctuaries)
    """

    #clans = np.random.rand(10,3)
    #print(clans)
    #print( find_chieftans(clans) )

    tiles = [1,2,3,4,5,6]
    l = len(tiles)
    test = Map(l, tiles)
