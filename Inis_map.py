"""
def explore(input):
    return input * 2


def new_clans(input, *f):
    return input * 3

deck = [new_clans, explore]

print( [ e(2) for e in deck ])



class inis_deck():

    def __init__(self):
        self.name = ''
        self.type = ''
        self.cards = []


class card():

    def __init__(self):
        self.name = ''
        self.type = ''



# Messenger/MessengerIdiom.py

class Messenger:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

m = Messenger(info="some information", b=['a', 'list'])
m.more = 11
print m.info, m.b, m.more

"""

import numpy as np

class testclass:

    qty_sanctuaries = 12

    def __init__(self, name, style):
        self.name = name
        self.style = style

    def add_attributes(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def testcard(cls):
        return cls('john', 15)

    @classmethod
    def testcard2(cls):
        return cls('jSam', 35)

    @classmethod
    def sanctuaries(cls):
        if cls.qty_sanctuaries > 0:
            cls.qty_sanctuaries -= 1
        return


def find_chieftans(clans):
    """returns player with max clans in each tile, if max has two values"""
    m,n = np.shape(clans)
    chieftans = np.zeros( (m, 1) )
    for i in range(0, m):
        maxes = np.where(clans[i] == np.amax(clans[i]))[0]
        if len(maxes) == 1:
            chieftans[i] = maxes[0]
    return chieftans

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class Map:

    def __init__(self, tiles, r=1, initial_point=np.array( [0,0] ),
                hex_grid_orientation=np.pi/2):

        self.tiles = np.inf*np.ones( (len(tiles), 3, 2) )  #initialise
        self.r = r
        self.inital_point = initial_point
        self.hex_grid_orientation = hex_grid_orientation
        self.hex_frontier = self.hex_centres(self.inital_point, self.hex_grid_orientation, r, qty=3)
        #np.array( [hex_x, hex_y], [hex_x2, ...], ....)

    def explore_hex_frontier(self):
        for tile in self.hex_frontier:
            adj_exp_pos = self.hex_centres(tile, self.hex_grid_orientation, self.r, 6)
            if adj_exp_pos

        adj_exp_pos = [self.hex_centres(tile, self.hex_grid_orientation, self.r, 6)
                        for tile in self.hex_frontier]
        for adj_tile in adj_exp_pos:
            if adj_tile not in self.tiles

    @staticmethod
    def hex_centres(hex_centre, hex_grid_orientation, r:float, qty=6):
        """Eavluates hexes around a point based off start rotation etc"""
        return np.add( np.array( [ [ r*np.cos(i*2*np.pi/qty + hex_grid_orientation),
                                     r*np.cos(i*2*np.pi/qty + hex_grid_orientation) ]
                                     for i in range(0, qty) ] ), hex_centre )


    def render(self):

        fig, ax = plt.subplots()
        ax.add_patch



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

    clans = np.random.rand(10,3)
    print(clans)
    print( find_chieftans(clans) )

    tiles = [1,2,3,4,5,6]
