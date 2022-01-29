"""
SETUP
--------------------------------------------------------------
Creates all objects and references necessary to start a new game
Validates the agents passed exist and can be used for the game
"""
import numpy as np
import random
import inis_tiles
import inis_decks
import inis_game_log
import inis_map

def setup_inis(player_agent_instances:dict) -> object:
    """
    Sets up game state variable and dependencies based on players
    """
    if not InisGameState.validate_player_agents(player_agent_instances):
        raise Exception("One or more player agents are incorrectly built or referenced")

    build_player_reference_instances_and_connect_to_agents( player_agent_instances )

    current_game_state = setup_inis_instance( player_agent_instances, logging=True )

    #setup_game_board(current_game_state)

    #setup fake games for the players for sims...
    #
    #...
    #
    return current_game_state


def setup_inis_instance(inis_game_state:object, player_agents:dict, logging: bool = False) -> object:
    """
    Function to construct Inis instances
    Variability is whethe the player agents are the real ones or fake ones/sims
    which the agents can use to simulate the game from the current game state
    Functionality in the game state class is copying to other game state instances
    :param player_agents:
    :rtype: object
    :return:
    """
    if validate_player_agents(player_agents) == False:
        raise Exception("One or more player agents are incorrectly built or referenced")
    n = len(player_agents)
    game_state_instance = inis_game_state( player_agents )
    tiles = inis_tiles.create_tiles()
    action_deck, epic_tale_deck, advantage_deck = inis_decks.build_decks(n)
    tile_advantage_pairs = connect_tiles_and_advantage_cards(tiles, advantage_deck)
    kwargs = {}
    if logging:
        kwargs.update( { 'game_log': inis_game_log.game_logger() } )
    kwargs.update( {
                     'tile_deck' : tiles,
                     'action_deck': action_deck,
                     'epic_tale_deck': epic_tale_deck,
                     'advantage_deck' : advantage_deck,
                     'tile_advantage_pairs' : tile_advantage_pairs
                    } )
    return game_state_instance


def setup_game_board(self, inis_game_state: object):
    """Creates Map Object and passes initial tiles to setup the map"""
    map = inis_map.Map()

    return


def validate_player_agents(player_agents) -> bool:
    """
    Needs to check it fits the form of tha ABC created in the inis_player_agents file?
    :param player_agents:
    :return:
    """
    return True


def build_player_reference_instances_and_connect_to_agents(player_agents: dict) -> None:
    """
    As long as player agents passed into the game are correctly keyworded etc
    will call a class based off of their name to construct a player and agent class
    to play the game
    :param player_agents:
    :return: players -> a list of object references to agent instances which
                        contain player instances as a class parameter
    """
    for player_id, player_agent in player_agents.items():
        player_references = { { key : inis_player_agents.dumbass_test_agent( key,
                               player_agents[key].name ) } for key in player_agents.keys()
                               if key != player_id }
        player_agent.player_references = player_references.copy()
    return


def connect_tiles_and_advantage_cards(tile_deck: object, advantage_deck: object) -> dict:
    """
    Tile deck and advantage cards are created independently
    Need to connect the tile object to the card to bring the card into play
    when the tile is drawn
    reliance is on both sets of classes being correctly named in accordance with TILES
    list object in inis_constants.py
    :param tile_deck: object that holds info about all tile object
            parameter to get this info out is '.tiles'
    :param advantage_deck: object that hold info about all advantage cards
            parameter to get this info out is '.cards'
    :return: dict of the object references which inis_game_state can use to find and assign cards etc
    """
    assert 'tiles' in dir(tile_deck)
    assert 'cards' in dir(advantage_deck)

    tile_card_pairs = dict( (tile, card) for tile in tile_deck.tiles \
                            for card in advantage_deck.cards if tile.name == card.name)
    return tile_card_pairs



if __name__=="__main__":
    #Test 1 - Build a new game setup?
    import inis_player_agents

    player_0 = {
                'name' : 'Doug',
                'player_agent' : inis_player_agents.dumbass_test_agent()
                }

    player_1 = {
                'name' : 'John',
                'player_agent' : inis_player_agents.dumbass_test_agent()
                }

    player_2 = {
                'name' : 'Brad',
                'player_agent' : inis_player_agents.dumbass_test_agent()
                }

    player_3 = {
                'name' : 'Test 2',
                'player_agent' : inis_player_agents.dumbass_test_agent()
                }

    player_agents = {
                      0: player_0,
                      1: player_1,
                      2: player_2,
                      3: player_3
                    }


