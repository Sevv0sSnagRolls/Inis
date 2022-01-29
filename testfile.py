"""

"""
import itertools
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import matplotlib.colors as mcolors
from scipy.optimize import minimize

class Tile:

    def __init__(self, centre, hexes, colour):
        self.centre = centre
        self.hexes = hexes
        self.colour = colour

    def render(self):
        pass


class Map:

    def __init__(self, initial_tiles: list, colours, radius=1, hex_grid_orientation=np.pi / 2):

        self.colours = colours

        self.r = radius
        self.hex_grid_orientation = hex_grid_orientation

        # initialise calculated values for later
        self.points = []  # init for calculations later
        self.hexes = []  # init for calculations later

        # run setup function
        self.tiles = []
        self.setup(initial_tiles)

    def setup(self, initial_tiles):
        """make initial tiles and positions"""
        inital_point = np.array([0, 0])
        centre = inital_point
        hexes = self.find_hexagon_points(centre, self.r, self.hex_grid_orientation, qty=3)
        colour = random.choice(self.colours)
        self.colours.pop(self.colours.index(colour))
        self.tiles.append(Tile(centre, hexes, colour))

        distance1 = np.array([-1 * 4 * self.r * np.cos(2 * np.pi / 6 * 1 / 2), 0])
        centre = np.add(inital_point, distance1)
        hexes = self.find_hexagon_points(centre, self.r, self.hex_grid_orientation, qty=3)
        colour = random.choice(self.colours)
        self.colours.pop(self.colours.index(colour))
        self.tiles.append(Tile(centre, hexes, colour))

        distance2 = np.array([-1 * 2 * self.r * np.cos(2 * np.pi / 6 * 1 / 2), 2 * self.r])
        centre = np.add(inital_point, distance2)
        hexes = self.find_hexagon_points(centre, self.r, 2 * np.pi / 6 * 1 / 2, qty=3)
        colour = random.choice(self.colours)
        self.colours.pop(self.colours.index(colour))
        self.tiles.append(Tile(centre, hexes, colour))

    def add_tile(self):
        """finds placements that can go on a single point"""
        options = self.find_possible_placements()
        select_spot = random.choice(options)
        colour = random.choice(self.colours)
        self.colours.pop(self.colours.index(colour))
        self.tiles.append(Tile(select_spot[0], select_spot[1], colour))

    def find_possible_placements(self):
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

        # self.adjpoints = []
        # for pData in pointData:
        #     if len(pData[1]) == 2 and len(pData[2])==2:
        #         self.adjpoints.append(pData[0])
        # self.render()

        possible_positions = []
        for pData in pointData:
            if len(pData[1]) == 2 and len(pData[2])==2:
                # bounds = [[self.r*-100, self.r*100], [self.r*-100, self.r*100]]
                # newHexCentre = minimize(zero, point, method='Nelder-Mead', args=(pData[1][0], pData[1][1]), bounds=bounds)

                # vector = np.subtract(pData[1][1], pData[1][0])
                # midPoint = np.add(vector, pData[1][0])
                # initial_vector = np.array([1, 0])
                # angle1 = np.dot(initial_vector, point)
                # angle2 = np.dot(initial_vector, pData[1][1])
                # vector = np.array( [np.linalg.norm(vector), 0])
                # if angle1 < angle2:
                #     # theta = 2*np.pi/6
                #     theta = angle2 - np.pi/2
                # else:
                #     theta = -2*np.pi / 6
                #     theta = angle2 + np.pi / 2
                # rotation_matrix = np.array( [ [np.cos(theta), -1*np.sin(theta)],
                #                               [np.sin(theta),    np.cos(theta)] ])
                # newHexCentre = np.add( np.dot(vector, rotation_matrix), pData[1][0])
                #
                g1 = self.find_hexagon_points(pData[1][0], 2*self.r * np.cos(2 * np.pi / 6 * 1 / 2), 0)
                g2 = self.find_hexagon_points(pData[1][1], 2*self.r * np.cos(2 * np.pi / 6 * 1 / 2), 0)
                # print(g1)
                # print(g2)
                # print(hexes)
                for g in g2:
                    # print(g)
                    distance1 = np.linalg.norm( np.subtract(g1, g), axis=1 )
                    distance2 = np.linalg.norm( np.subtract(hexes, g), axis=1)
                    # print("d1: ", distance1)
                    # print("d2: ", distance2)
                    # print("w1: ", np.where(distance1 < self.r / 100)[0])
                    # print("w2: ", np.where(distance2 < self.r / 100)[0])
                    if len(np.where(distance1 < self.r/100)[0]) > 0 and (len(np.where(distance2 < self.r/100)[0])==0):
                        # print("YAY")
                        # print("d1: ", distance1)
                        # print("d2: ", distance2)
                        # print("w1: ", np.where(distance1 < self.r / 100)[0])
                        # print("w2: ", np.where(distance2 < self.r / 100)[0])
                        newHexCentre = g.copy()
                        break
                surrounding_hexes = self.find_hexagon_points(newHexCentre, 2*self.r*np.cos(2*np.pi/6*1/2), 0)
                # print(pData[0])
                # print(pData[1][0])
                # print(pData[1][1])
                # print("centre ", newHexCentre)
                # print(surrounding_hexes)
                available_hex_group = [newHexCentre]
                for aHex in surrounding_hexes:
                    distance = np.linalg.norm(np.subtract(hexes, aHex), axis=1)
                    if len(np.where(distance < self.r/100)[0]) == 0:
                        available_hex_group.append(aHex)
                possible_positions.append(available_hex_group)

        print(possible_positions)
        options = []
        for position in possible_positions:
            print("position ", position)
            for hex_trio in itertools.combinations(position, 3):
                print("trio ", hex_trio)
                distances = []
                for pair in itertools.combinations(hex_trio, 2):
                    print(pair)
                    distances.append(np.linalg.norm(np.subtract(pair[0], pair[1])))
                print("distances ", distances)
                if (np.abs(distances[0] - distances[1]) < self.r / 1000) and \
                        (np.abs(distances[1] - distances[2]) < self.r / 1000) and \
                        (np.abs(distances[2] - distances[1]) < self.r / 1000):
                    centre = np.average([position for position in hex_trio])
                    print("centres ", centre)
                    options.append([centre, hex_trio])
        print(options)
        return options

    @staticmethod
    def find_hexagon_points(hex_centre, radius: float, hex_grid_orientation: float, qty=6):
        """returns a list of six points surrounding a hex centre"""
        return np.add(np.array([[radius * np.cos(i * 2 * np.pi / qty + hex_grid_orientation),
                                 radius * np.sin(i * 2 * np.pi / qty + hex_grid_orientation)]
                                for i in range(0, qty)]), hex_centre)

    def render(self):
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


# def zero(guess, point1, point2):
#     l1 = np.linalg.norm( np.subtract(point2, point1) )
#     l2 = np.linalg.norm( np.subtract(guess, point1) )
#     l3 = np.linalg.norm( np.subtract(guess, point2) )
#     return 2*l1 - (l2 + l3)

if __name__ == "__main__":
    testlist = []
    matplotlibcolours = list(mcolors.CSS4_COLORS.keys())
    map = Map(testlist, matplotlibcolours)
    for i in range(0, 4):
        map.add_tile()
    map.render()
