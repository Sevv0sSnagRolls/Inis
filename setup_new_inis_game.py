"""
SETUP
--------------------------------------------------------------
Creates all objects and references necessary to start a new game

Validates the agents passed exist and can be used for the game
"""
import inis_player_class
from inis_game_log import game_logger
from inis_game_state import inis_game_state
from inis_decks import build_decks
#from inis_game_meta import inis_game


def setup_inis(player_agents) -> object:
    """
    Function responsible for calling all sub modules and functions to setup game and players
    to allow turns to be played

    Players need to be of a particular format, may need some validatin function here for that purpose
    """
    if validate_player_agents(player_agents) == False:
        raise Exception("One or more player agents are incorrectly built or referenced")
    n = len(player_agents)
    player_agent_instances = build_players_and_connect_to_agents(player_agents)
    action_deck, epic_tale_deck, advantage_deck = build_decks(n)
    current_game_log = game_logger(n)
    current_game_state = inis_game_state( player_agent_instances )
    current_game_state.add_game_logger(current_game_log)
    current_game_state.add_game_decks(action_deck, epic_tale_deck, advantage_deck)
    return current_game_state


def validate_player_agents(player_agents):
    """
    Needs to check it fits the form of tha ABC created in the inis_player_agents file?

    :param player_agents:
    :return:
    """

    return True


def build_players_and_connect_to_agents(player_agents):
    """
    As long as player agents passed into the game are correctly keyworded etc
    will call a class based off of their name to construct a player and agent class
    to play the game

    :param player_agents:
    :return: players -> a list of object references to agent instances which
                        contain player instances as a class parameter
    """
    players = []
    n = len(player_agents)
    player_ids = list(range(0,n))
    for i, player_agent in enumerate(player_agents):
        #build the actual player class to store game specific information
        player_class = inis_player_class.inis_player(player_id = i)
        #build references classes with the player ids for agent to use to store information about each player
        player_reference_classes = []
        for j in player_ids:
            if j != i:
                player_reference_classes.append( inis_player_class.inis_player(player_id = j) )
        player_agent = inis_player_agents.player_agent(player = player_class,
                                                       player_references = player_reference_classes)
        players.append(player_agent)
    return player_agent_instances


if __name__=="__main__":
    #Test 1 - Build a new game setup?
    #probably best to do in another module like main