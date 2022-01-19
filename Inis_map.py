import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

class Map:

    def __init__(self, l:int, initial_tiles: dict, r=1, initial_point=np.array( [0,0] ),
                hex_grid_orientation=np.pi/2):

        #l is the length of the tile deck/number of lands to make sure arrays have correct mem size
        #C based
        self.l = l
        # dict (index of tile: tileobjectinstance)
        self.tile_objects = initial_tiles
        #bundle tiles by index into groups of three
        self.tiles = np.inf*np.ones( (self.l, 3, 2) )
        self.r = r
        self.inital_point = initial_point
        self.hex_grid_orientation = hex_grid_orientation
        self.hex_frontier = self.hex_centres(self.inital_point, self.hex_grid_orientation, r, qty=3)
        self.explored_tile_positions = np.empty( (self.l, 2) )
        self.tiles_in_game = 0 #dodgy pointer to tiles location....
        #np.array( [hex_x, hex_y], [hex_x2, ...], ....)
        self.renderHexGrid(self.hex_frontier, self.r)

        self.initialise()

    def add_tile(self, tile: object):
        """Returns a list of positble locations to place the tile. Player will then select as handled by game"""
        self.explore_hex_frontier()

        return

    def initialise(self):
        """Give everything a starting value to allow exploration function to work"""
        self.tiles[self.tiles_in_game] = self.hex_frontier
        self.update_explored_tiles()
        print(self.tiles)

    def explore_hex_frontier(self):
        """Find new adj tile locations, return list of options"""
        """Currently inefficient, hoping to add frontier element to reduce iterating over 'landlocked' hexes"""
        possible_locations = []
        for tile in self.explored_tile_positions::
            for adj_pos in self.hex_centres(tile, self.hex_grid_orientation, self.r, 6)
                if adj_pos not in self.explored_tile_positions:
                    possible_locations.append(adj_pos)

        return

    def update_explored_tiles(self):
        self.explored_tile_positions = [exp for tile in self.tiles for exp in tile]

    @staticmethod
    def hex_centres(hex_centre, hex_grid_orientation, r:float, qty=6):
        """Eavluates hexes around a point based off start rotation etc"""
        return np.add( np.array( [ [ r*np.cos(i*2*np.pi/qty + hex_grid_orientation),
                                     r*np.sin(i*2*np.pi/qty + hex_grid_orientation) ]
                                     for i in range(0, qty) ] ), hex_centre )

    def renderHexGrid(self, hex_centres, radius):
        fig, ax = plt.subplots()
        patches = []
        for hex in hex_centres:
            patches.append(mpatches.RegularPolygon(hex, 6, radius) )
        collection = PatchCollection(patches)
        ax.add_collection(collection)
        plt.autoscale()
        plt.show()



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
    test = Map(tiles)
