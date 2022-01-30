"""
inis_map.py

This was painful...

"""
import itertools
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import matplotlib.colors as mcolors
import inis_tiles


class Map:

    def __init__(self, initial_tiles: list, colours=None, radius=1, hex_grid_orientation=np.pi / 2):

        self.r = radius
        self.hex_grid_orientation = hex_grid_orientation

        if colours:
            self.colours = colours

        # initialise calculated values for later
        self.points = []  # init for calculations later
        self.hexes = []  # init for calculations later

        # run setup function
        self.tiles = initial_tiles
        self._setup()

    def _setup(self):
        """make initial tiles and positions"""
        initial_point = np.array([0, 0])
        vector1 = np.array([-1 * 4 * self.r * np.cos(2 * np.pi / 6 * 1 / 2), 0])
        vector2 = np.array([-1 * 2 * self.r * np.cos(2 * np.pi / 6 * 1 / 2), 2 * self.r])
        vector3 = np.array([ 1 * 2 * self.r * np.cos(2 * np.pi / 6 * 1 / 2), 2 * self.r])
        vectors = [initial_point, vector1, vector2, vector3]
        orientations = [self.hex_grid_orientation, self.hex_grid_orientation, 2*np.pi/6*1/2, 2*np.pi/6*1/2]
        n = len(self.tiles) if len(self.tiles) >= 3 else 3
        for i in range(0, n):
            centre = np.add(initial_point, vectors[i])
            hexes = self.find_hexagon_points(centre, self.r, orientations[i], qty=3)
            self.tiles[i].centre = centre
            self.tiles[i].hexes = hexes
        self.find_adj()
        # for tile in self.tiles:
        #     print(tile, tile.adj)

    def player_add_tile(self, player, tile):
        """public method for game to call for exploration card"""
        options = self._find_possible_placements()
        selected_position = self._prompt_player_selection(player, options)
        self._add_tile(selected_position, tile)

    def _prompt_player_selection(self, player: object, options: list) -> 'numpy array':
        """Handles player selection and validation. Player class need method select tile..."""
        i = 0
        selection_valid = False
        selected_tile_location = np.empty((2, 1))
        while not selection_valid or i <= 10:
            selected_tile_location = player.select_tile(options)
            if selected_tile_location in options:
                print('Selection Invalid')
                selection_valid = True
            if i == 10:
                print('Too many invalid selections for tile location')
            i += 1
        return selected_tile_location

    def __add_tile(self, selected_position, tile):
        """Finally, adds the selection to the object"""
        tile.centre = selected_position[0]
        tile.hexes = selected_position[1]
        self.tiles.append(tile)

    def _add_tile_randomly(self, tile):
        """finds placements that can go on a single point"""
        options = self.find_possible_placements()
        select_spot = random.choice(options)
        self.__add_tile(select_spot, tile)
        # colour = random.choice(self.colours)
        # self.colours.pop(self.colours.index(colour))
        # self.tiles.append(Tile(select_spot[0], select_spot[1], colour))

    def _find_possible_placements(self) -> list:
        """find wehere to place next to two adjacent tiles"""
        pointData = []
        explored_points = []
        hexes = []
        for tile in self.tiles:
            for hexC in tile.hexes:
                for point in self.find_hexagon_points(hexC, self.r, self.hex_grid_orientation):
                    if len(pointData):
                        distance = np.linalg.norm(np.subtract(explored_points, point), axis=1)
                        location = np.where(distance < self.r/100)[0]
                        if len(location):
                            # fucking hate np where return format jfc
                            pointData[location[0]][1].append(hexC)
                            if tile not in pointData[location[0]][2]:
                                pointData[location[0]][2].append(tile)
                        else:
                            # if point doesn't exist, add it and add 1 to count
                            pointData.append([point, [hexC], [tile]])
                            explored_points.append(point)
                    else:
                        pointData.append([point, [hexC], [tile]])
                        explored_points.append(point)
                if len(hexes):
                    if not (hexC == hexes).all(axis=1).any():
                        hexes.append(hexC)
                else:
                    hexes.append(hexC)
        hexes = np.array(hexes)

        # Check points are correct
        # self.adjpoints = []
        # for pData in pointData:
        #     if len(pData[1]) == 2 and len(pData[2])==2:
        #         self.adjpoints.append(pData[0])
        # self.render()

        possible_positions = []
        for pData in pointData:
            if len(pData[1]) == 2 and len(pData[2])==2:
                g1 = self.find_hexagon_points(pData[1][0], 2*self.r * np.cos(2 * np.pi / 6 * 1 / 2), 0)
                g2 = self.find_hexagon_points(pData[1][1], 2*self.r * np.cos(2 * np.pi / 6 * 1 / 2), 0)
                for g in g2:
                    distance1 = np.linalg.norm( np.subtract(g1, g), axis=1 )
                    distance2 = np.linalg.norm( np.subtract(hexes, g), axis=1)
                    if len(np.where(distance1 < self.r/100)[0]) > 0 and (len(np.where(distance2 < self.r/100)[0])==0):
                        newHexCentre = g.copy()
                        break
                surrounding_hexes = self.find_hexagon_points(newHexCentre, 2*self.r*np.cos(2*np.pi/6*1/2), 0)
                available_hex_group = [newHexCentre]
                for aHex in surrounding_hexes:
                    distance = np.linalg.norm(np.subtract(hexes, aHex), axis=1)
                    if len(np.where(distance < self.r/100)[0]) == 0:
                        available_hex_group.append(aHex)
                possible_positions.append(available_hex_group)

        options = []
        for position in possible_positions:
            for hex_trio in itertools.combinations(position, 3):
                distances = []
                for pair in itertools.combinations(hex_trio, 2):
                    distances.append(np.linalg.norm(np.subtract(pair[0], pair[1])))
                if (np.abs(distances[0] - distances[1]) < self.r / 1000) and \
                        (np.abs(distances[1] - distances[2]) < self.r / 1000) and \
                        (np.abs(distances[2] - distances[1]) < self.r / 1000):
                    centre = np.average([position for position in hex_trio])
                    options.append([centre, hex_trio])

        self.find_adj()

        #returns [ [centrePoint, hexes], [centrePoint, hexes], ...]
        return options

    def find_adj(self):
        for tile1 in self.tiles:
            for tile2 in self.tiles:
                if tile1 != tile2:
                    for hex1 in tile1.hexes:
                        for hex2 in tile2.hexes:
                            distance = np.linalg.norm(np.subtract(hex2, hex1))
                            if np.abs(distance - (2*self.r*np.cos(2*np.pi/6*1/2))) < self.r/100:
                                if tile2 not in tile1.adj:
                                    tile1.adj.append(tile2)
                                if tile1 not in tile2.adj:
                                    tile2.adj.append(tile1)

    @staticmethod
    def find_hexagon_points(hex_centre, radius: float, hex_grid_orientation: float, qty=6):
        """returns a list of six points surrounding a hex centre"""
        return np.add(np.array([[radius * np.cos(i * 2 * np.pi / qty + hex_grid_orientation),
                                 radius * np.sin(i * 2 * np.pi / qty + hex_grid_orientation)]
                                for i in range(0, qty)]), hex_centre)

    def render(self):
        """renders the current map state"""
        fig, ax = plt.subplots()
        patches = []
        for tile in self.tiles:
            for hexC in tile.hexes:
                patches.append(mpatches.RegularPolygon(hexC, 6, self.r, facecolor=tile.colour))
        # for point in self.adjpoints:
        #     patches.append(mpatches.Circle(point, self.r/10, facecolor='r'))
        collection = PatchCollection(patches, match_original=True)
        ax.add_collection(collection)
        ax.add_collection(collection)
        plt.autoscale()
        plt.show()


if __name__ == "__main__":
    testlist = []
    matplotlibcolours = list(mcolors.CSS4_COLORS.keys())
    map = Map(testlist, colours=matplotlibcolours)
    for i in range(0, 4):
        map.__add_tile()
    map.render()




"""failed attempts"""
#
#
#
# import random
# import numpy as np
# import itertools
# import matplotlib.pyplot as plt
# from matplotlib.patches import Circle, RegularPolygon
# from matplotlib.collections import PatchCollection
#
#
# # #actually stupid, maybe matrix rep was better....
# # class Map:
# #     """
# #     Actually had a stroke making this. Seems fucking dumb
# #     """
# #
# #     def __init__(self, l:int, initial_tiles: dict, r=1, initial_point=np.array( [0.0,0.0] ),
# #                 hex_grid_orientation=np.pi/2):
# #
# #         #l is the length of the tile deck/number of lands to make sure arrays have correct mem size
# #         #C based
# #         self.l = l
# #
# #         # dict (index of tile: tileobjectinstance)
# #         self.tile_objects = initial_tiles
# #
# #         #bundle tiles by index into groups of three
# #         self.tiles_positions = np.inf*np.ones( (self.l, 3, 2) )
# #
# #         self.r = r
# #         self.initial_point = initial_point
# #         self.hex_grid_orientation = hex_grid_orientation
# #         self.hex_frontier = []
# #         self.explored_tile_positions = np.empty( (self.l, 2) )
# #
# #         # dodgy pointer to tiles location....
# #         self.tiles_in_game_index = 0
# #
# #         #np.array( [hex_x, hex_y], [hex_x2, ...], ....)
# #         self.renderHexGrid(self.hex_frontier, self.r)
# #
# #         self.__initialise()
# #
# #     def player_select_tile(self, player:object, tile:object):
# #         """interface for external objects for players to generate exploration locations"""
# #         options = self.__generate_placement_options()
# #         selected_position = self.__prompt_player_selection(player, options)
# #         self.__add_tile_to_instance(selected_position, tile)
# #
# #     def __select_tile_random(self, tile: dict):
# #         """Returns a list of positble locations to place the tile. Player will then select as handled by game"""
# #         options = self.explore_hex_frontier()
# #         self.__add_tile_to_instance(random.choice(options), tile)
# #         return random.choice(options)
# #
# #     def __add_tile_to_instance(self, positions, tile:dict):
# #         self.tiles_in_game_index += 1
# #         self.tiles_positions[self.i] = positions
# #         self.tile_objects.update(tile)
# #
# #     def __initialise(self):
# #         """Give everything a starting value to allow exploration function to work"""
# #         #self.tiles[self.tiles_in_game] = self.hex_frontier
# #         #add two more random tiles
# #         self.hex_centres(self.inital_point, self.hex_grid_orientation, r, qty=3)
# #         for i in range(1, len(self.tile_objects)):
# #             self.__select_tile_random(self, self.tile_objects[i])
# #         print(self.tiles)
# #
# #     def __explore_hex_frontier(self):
# #         """Find new adj tile locations, return list of options"""
# #         """Currently inefficient, hoping to add frontier element to reduce iterating over 'landlocked' hexes"""
# #         possible_locations = []
# #         self.__update_explored_tiles()
# #         for tile in self.explored_tile_positions:
# #             for adj_pos in self.hex_centres(tile, self.hex_grid_orientation, 6, self.r):
# #                 # find distances and if it already exists
# #                 c = np.linalg.norm(np.subtract(self.explored_tile_positions, adj_pos), axis=1)
# #                 if np.size(np.where(c==0)) == 0:
# #                     if np.size(np.where((c-self.r-10**-9) <= 0)) >= 2:
# #                         possible_locations.append(adj_pos)
# #                         print(possible_locations)
# #                     else:
# #                         self.hex_frontier.append(adj_pos)
# #         return possible_locations
# #
# #     def __generate_placement_options(self, initialise=False):
# #         """Takes hexes, check adjaceny to existing hexes"""
# #         options = self.explore_hex_frontier()
# #         #for option in options:
# #         #im not doing this complex shit for now jfc
# #         pass
# #
# #
# #
# #     def __prompt_player_selection(self, player:object, options: list) -> 'numpy array':
# #         """Handles player selection and validation. Player class need method select tile..."""
# #         i = 0
# #         selection_valid = False
# #         selected_tile_location = np.empty((2,1))
# #         while not selection_valid or i <= 10:
# #             selected_tile_location = player.select_tile(options)
# #             if selected_tile_location in options:
# #                 selection_valid = True
# #             if i == 10:
# #                 print('Too many invalid selections for tile location')
# #             i += 1
# #         return True, selected_tile_location
# #
# #     def __update_explored_tiles(self):
# #         self.explored_tile_positions = [exp for tile in self.tiles for exp in tile]
# #
# #     @staticmethod
# #     def hex_centres(hex_centre, hex_grid_orientation, r:float, qty=6):
# #         """Eavluates hexes around a point based off start rotation etc"""
# #         return np.add( np.array( [ [ r*np.cos(i*2*np.pi/qty + hex_grid_orientation),
# #                                      r*np.sin(i*2*np.pi/qty + hex_grid_orientation) ]
# #                                      for i in range(0, qty) ] ), hex_centre )
# #
# #     def renderHexGrid(self, hex_centres, radius):
# #         fig, ax = plt.subplots()
# #         patches = []
# #         for hex in hex_centres:
# #             patches.append(mpatches.RegularPolygon(hex, 6, radius) )
# #         collection = PatchCollection(patches)
# #         ax.add_collection(collection)
# #         plt.autoscale()
# #         plt.show()
# # """
#
#
# class Map:
#     """
#     Map Class is a way I developed of representing hexagonal
#     tessilication in a rectangular matrix
#     vertically aligned hexes can be imagined in rows
#     as being normal, offset, normal:
#     0 0 0 0 0 0
#      0 0 0 0 0 0
#     0 0 0 0 0 0
#     etc...
#     Each of this elements in the rect matrix represents one hex section of the tiles
#     tiles are comprised of three hex sections
#     relationship between the tiles (what's adjacent to what) is described in
#     the class variables below
#
#     To make sure the map can grow, methods will check current tile proxity to
#     map (rect array) edge and add a buffer based on the distance
#
#     Possible patterns to add to the grid are 4 different styles of a 2x2 matrix
#     These permutations will be checked for exploration methods
#     """
#     # common between all classes,
#     # buffer extender must be two rows to allow specific laying of tiles
#     map_buffer_extender = 3
#
#     # Pattern of connections to other indicies 1 - odd rows
#     # \ |
#     # --i--
#     # / |
#     # [i-1][j-1], [i-1][j]
#     # [i][j-1],   [i][j+1]
#     # [i+1][j-1], [i+1][j]
#     pattern_1 = np.array([[-1, 0], [-1, 1],
#                           [0, -1], [0, 1],
#                           [1, 0], [1, 1]], dtype=int)
#
#     pattern_3 = np.array([[1, 1, 0],
#                           [1, 1, 1],
#                           [1, 1, 0]], dtype=int)
#
#     # Pattern of connections to other indicies 2 - even rows
#     #   | /
#     # --i--
#     #   | \
#     # [i-1][j], [i-1][j+1]
#     # [i][j-1], [i][j+1]
#     # [i+1][j], [i+1][j+1]
#     pattern_2 = np.array([[-1, 0], [-1, 1],
#                           [0, -1], [0, 1],
#                           [1, 0], [1, 1]], dtype=int)
#
#     pattern_3 = np.array([ [0, 1, 1],
#                            [1, 1, 1],
#                            [0, 1, 1]], dtype=int )
#
#     def __init__(self, initial_tiles: dict, x: int = 12, r=1):
#         # player_qty ->
#         # initial_tiles -> the selected inital tiles
#         self.x = x
#         self.y = x
#         self.maprep = -1 * np.ones((self.x, self.y), dtype=int)
#         self.r = r
#         # Map will store the dict of index : tile object
#         # this allows colours etc to be grabbed later
#         self.tiles = initial_tiles
#         # Player qty is just the number of players in the game
#         self.player_qty = len(initial_tiles)
#         # tile count is a stored pointer that will update i++ for every
#         # tile added for tile dict
#         self.tile_count = 0
#
#         # Creates the 4 ways tile objects can be placed
#         self.hex_patterns = self.hex_patterns()
#         self.hex_inidices = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=int)
#
#         # run the initial setup function
#         self.__initial_map_layout()
#
#     def player_add_tile(self, player, tile):
#         """public method for game to call for exploration card"""
#         self.__check_map_size()
#         options = self.__generate_tile_placement_options()
#         selected_position = self.__prompt_player_selection(player, options)
#         self.__add_tile_to_instance(selected_position, tile)
#
#     def __prompt_player_selection(self, player: object, options: list) -> 'numpy array':
#         """Handles player selection and validation. Player class need method select tile..."""
#         i = 0
#         selection_valid = False
#         selected_tile_location = np.empty((2, 1))
#         while not selection_valid or i <= 10:
#             selected_tile_location = player.select_tile(options)
#             if selected_tile_location in options:
#                 print('Selection Invalid')
#                 selection_valid = True
#             if i == 10:
#                 print('Too many invalid selections for tile location')
#             i += 1
#         return selected_tile_location
#
#     def __add_tile_to_instance(self, selected_position, tile):
#         """Finally, adds the selection to the object"""
#
#     def __initial_map_layout(self):
#         """Place the qty of initial tiles"""
#         # start_pos = self.x
#         # self.maprep[int(x/2), int(y/2)] = random.choice(Map.hex_patterns)
#         # To fix later, for now just use a specific start grid with known indexes min of 2 player
#         # need to check this fits in with row offset patterns
#         a = Map.map_buffer_extender
#         start_array = np.array([[0, 0, 1],
#                                 [0, 1, 1]])
#         m = np.shape(start_array)
#         self.maprep[ int(self.x/2)-3:int(self.x/2)-3 + m[0], int(self.y/2)-1:int(self.y/2)-1 + m[1]] = start_array
#         self.tile_count = 2
#         print(self.maprep)
#         for i in range(2, self.player_qty):
#             self.maprep = random.choice(self.__find_tile_placement_option())
#             print(self.maprep)
#             self.tile_count += 1
#         self.render_matplotlib()
#
#     # def __generate_tile_placement_options(self):
#     #     """Generates all permutations of positions new tile can go"""
#     #     options = []
#     #     self.__existing_tile_locations()
#     #     options += self.__find_tile_placement_options(loc)
#     #     for loc in self.__find_valid_adj_tile_locations():
#     #         options += self.__find_tile_placement_options(loc)
#     #     return options
#     #
#     def __existing_tile_locations(self):
#         """Find 0 or greater (tile indicies in the map"""
#         self.existing = np.transpose(np.nonzero(self.maprep >= 0))
#
#     #
#     def __find_adj_tile_locations(self, array):
#         """Finds points adjacent to each element on the map via indicies in the given array"""
#         m = np.shape(array)[0]
#         adjs = np.array([np.add(self.__patterns(element[0]), element) for element in array])
#         adjs = np.unique( np.reshape(adjs, (m * 6, 2)), axis=1 )
#         return adjs
#
#     # def __find_valid_adj_tile_locations(self):
#     #     """Test which adjacent tiles are adcacent to two different tiles"""
#     #     valid_locations = []
#     #     for adj in self.__find_adj_tile_locations(self.existing):
#     #         distance = self.array_distances(self.existing, adj)
#     #         if np.size(np.where(distance == 0)) == 0:
#     #             # check if its adjacent to atleast two existing points
#     #             adjacents = self.__find_adj_tile_locations([adj])
#     #             count = 0
#     #             for e in self.existing:
#     #                 if e in adjacents:
#     #                     count += 1
#     #             if count >= 2:
#     #                 valid_locations.append(adj)
#     #     return valid_locations
#
#     def __find_tile_placement_option(self):
#         """Finds the permutations of placement options available to the tile"""
#         self.__existing_tile_locations()
#         adjs = self.__find_adj_tile_locations(self.existing)
#         m = np.shape(self.maprep)
#         available = [[i, j] for i in range(0, m[0]) for j in range(0, m[1]) if
#                      ((self.existing == np.array([i, j])).all(axis=1).any() is False)
#                      and (adjs == np.array([i, j])).all(axis=1).any()]
#         print(available)
#
#         print(adjs)
#
#
#         possible_placements = []
#         for i in range(1, m[0]-1):
#             for j in range(1, m[1]-1):
#                 array = np.array([[i, j]])
#                 adjs = self.__find_adj_tile_locations(array)
#                 count = 0
#                 unavailable = []
#                 for adj in adjs:
#                     matches = np.where((self.existing == adj).all(axis=1))
#                     if matches[0].any():
#                         count += 1
#                         unavailable.append(np.array([matches[0], matches[1]]))
#                 if count >= 2:
#                     adj_shape = self.__patterns2(i)
#                     for k in range(0, 1):
#                         for j in range(0, 1):
#                             for shape in self.hex_patterns:
#                                 placement = np.add(shape, array)
#
#                     available.append()
#
#
#         # for i in range(0, 1):
#         #     for j in range(0, 1):
#         #         sp = np.subtract(loc, [-1 * i, -1 * j])
#         #         for pattern in self.hex_patterns:
#         #             tile = []
#         #             tile_lay = np.add(np.multiply(self.hex_inidices, tile), sp)
#         #             print(tile_lay)
#         #             count = 0
#         #             for hex in tile_lay:
#         #                 if (len(np.where(np.linalg.norm(np.subtract(adjs, hex), axis=1) == 0)[0]) > 0) \
#         #                         and \
#         #                         (len(np.where(np.linalg.norm(np.subtract(self.existing, hex), axis=1) == 0)[0]) > 0):
#         #                     count += 1
#         #             if count == 3:
#         #                 placement = self.maprep.copy()
#         #                 placement[sp[0]:sp[0] + 1, sp[1]:sp[1] + 1] = tile_lay
#         #                 possible_placements.append(placement)
#         #
#
#         # print(adjs)
#         # for pair in itertools.combinations(adjs, 2):
#         #     if np.linalg.norm(np.subtract(pair[0], pair[1])) == 1:
#         #         print(pair)
#         #         pair_valid = True
#         #         for element in pair:
#         #             distance = self.array_distances(self.existing, element)
#         #             if np.size(np.where(distance == 0)):
#         #                 pair_valid = False
#         #         if pair_valid:
#         #             print(pair)
#         #             placement = self.maprep.copy()
#         #             placement[loc[0]][loc[1]] = self.tile_count
#         #             placement[pair[0][0]][pair[0][1]] = self.tile_count
#         #             placement[pair[1][0]][pair[1][1]] = self.tile_count
#         #             possible_placements.append(placement)
#
#         return possible_placements
#
#     @staticmethod
#     def array_distances(array, point):
#         """Finds distance between array and a point"""
#         return np.linalg.norm(np.subtract(array, point), axis=1)
#
#     def __check_map_size(self):
#         """checks and increases size as map gets explored to the edges"""
#         buffer_check = np.sum(self.maprep[:, 0]) + \
#                        np.sum(self.maprep[:, -1]) + \
#                        np.sum(self.maprep[0, :]) + \
#                        np.sum(self.maprep[-1, :])
#         if buffer_check > 0:
#             self.__extend_map()
#
#     def __extend_map(self):
#         """add a column and a row buffer around the entire map"""
#         self.x += Map.map_buffer_extender
#         self.y += Map.map_buffer_extender
#         newMap = -1 * np.ones((self.x, self.y), dtype=int)
#         newMap[1:-1, 1:-1] = self.maprep.copy()
#         self.maprep = newMap.copy()
#
#     def __patterns(self, row_index):
#         """way of converting vertical hex grids into matrcies"""
#         if row_index % 2 == 1:
#             return self.pattern_1
#         return self.pattern_2
#
#     def __patterns2(self, row_index):
#         """way of converting vertical hex grids into matrcies"""
#         if row_index % 2 == 1:
#             return self.pattern_3
#         return self.pattern_4
#
#
#     @staticmethod
#     def hex_patterns():
#         hex = np.array([[1, 1], [1, 0]])
#         hex_patterns = [np.rot90(hex, k) for k in range(0, 4)]
#         return hex_patterns
#
#     def render_matplotlib(self):
#         """Renders as plotted which is a vertical hex grid"""
#         fig, ax = plt.subplots()
#         patches = []
#         m, n = np.shape(self.maprep)
#         for i in range(0, m):
#             for j in range(0, n):
#                 tile_index = self.maprep[i][j]
#                 if tile_index >= 0:
#                     # sart from top left as (0,0)
#                     x = ((2 * j) - (i % 2)) * self.r * np.cos(2 * np.pi / 6 * 1 / 2)
#                     y = -1 * i * (self.r + self.r * np.sin(2 * np.pi / 6 * 1 / 2))
#                     colour = self.tiles[str(tile_index)][1]
#                     patches.append(RegularPolygon((x, y), 6, self.r, facecolor=colour))
#         collection = PatchCollection(patches, match_original=True)
#         ax.add_collection(collection)
#         plt.autoscale()
#         plt.show()
#
#     # def update_map_dict(self):
#     #     dict_values = {}
#     #     for i in range(0, self.x):
#     #         for j in range(0, self.x):
#     #             dict_values.update({(str(i) + str(j)) : np.add(self.__patterns(i), self.map[i][j])})
#
#
# if __name__ == '__main__':
#     tiles = {'0': [5, 'lime'], '1': [6, 'darkorange'], '2': [6, 'chocolate'], '3': [6, 'blue']}
#     test = Map(tiles)
