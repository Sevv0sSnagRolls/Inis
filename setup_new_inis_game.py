"""
SETUP
--------------------------------------------------------------
Creates all objects and references necessary to start a new game

Validates the agents passed exist and can be used for the game
"""
from inis_decks import build_decks
from inis_game_log import game_logger
from inis_game_state import inis_game_state
from inis_tiles import create_tiles
import inis_player_agents

def setup_inis(player_agents:dict) -> object:
    """
    Function responsible for calling all sub modules and functions to setup game and players
    to allow turns to be played

    Players need to be of a particular format, may need some validatin function here for that purpose
    """
    if validate_player_agents(player_agents) == False:
        raise Exception("One or more player agents are incorrectly built or referenced")

    player_agent_instances = build_player_reference_instances_and_connect_to_agents( player_agents )
    build_player_reference_instances_and_connect_to_agents( player_agents )
    current_game_state = setup_inis_instance( player_agent_instances, logging=True )

    #setup fake games for the players for sims...
    #
    #...
    #

    return current_game_state


def setup_inis_instance(player_agents: list, logging: bool = False) -> object:
    """
    Function to construct Inis instances

    Variability is whether or not the player agents are the real ones or fake ones/sims
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

    tile_deck = create_tiles()
    action_deck, epic_tale_deck, advantage_deck = build_decks(n)
    kwargs = {}
    if logging:
        kwargs.update( { 'game_log': game_logger() } )
    kwargs.update( {
                     'tile_deck' : tile_deck,
                     'action_deck': action_deck,
                     'epic_tale_deck': epic_tale_deck,
                     'advantage_deck' : advantage_deck
                    } )

    return game_state_instance


def setup_game_board(inis_game_obj: object):
    """
    IDK how to handle where to place the initial clans??
    Maybe just use a random choice function for player agent for now??
    :return:
    """
    for players in player:
        place


def place_initial_tiles():
    """
    Tile deck can probably be built from the same class as all the other decks...

    :return:
    """
    initial_tiles = [inis_game_state.tile_deck.draw_tile() for i in range(0, len(inis_game_state.players)) ]


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


#if __name__=="__main__":
    #Test 1 - Build a new game setup?
