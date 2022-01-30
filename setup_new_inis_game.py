"""
SETUP
--------------------------------------------------------------
Creates all objects and references necessary to start a new game
Validates the agents passed exist and can be used for the game
"""
import numpy as np
import random
import inis_game_state
import inis_tiles
import inis_decks
import inis_game_log
import inis_map


def setup_inis(player_agent_instances: list) -> object:
    """    Sets up game state variable and dependencies based on players"""
    if not validate_player_agents(player_agent_instances):
        raise Exception("One or more player agents are incorrectly built or referenced")
    current_game_state = setup_inis_instance(player_agent_instances, logging=True)
    # build_player_reference_instances_and_connect_to_agents(player_agent_instances)
    # setup fake games for the players for sims...
    #
    # ...
    #
    return current_game_state


def setup_inis_instance(player_agent_instances: list, logging: bool = False) -> object:
    """Constructs Game and all it's dependencies"""
    if validate_player_agents(player_agent_instances) == False:
        raise Exception("One or more player agents are incorrectly built or referenced")
    n = len(player_agent_instances)
    tile_deck = inis_tiles.create_tiles()
    game_state_instance = inis_game_state.InisGameState(player_agent_instances, tile_deck)
    action_deck = inis_decks.inis_card_deck.create_action_deck(n)
    advantage_deck = inis_decks.inis_card_deck.create_advantage_deck(n)
    epic_tale_deck = inis_decks.inis_card_deck.create_epic_tale_deck(n)
    tile_advantage_pairs = connect_tiles_and_advantage_cards(tile_deck, advantage_deck)
    kwargs = {}
    if logging:
        kwargs.update({'game_log': inis_game_log.game_logger(n)})
    kwargs.update({
        'tile_deck': tile_deck,
        'action_deck': action_deck,
        'epic_tale_deck': epic_tale_deck,
        'advantage_deck': advantage_deck,
        'tile_advantage_pairs': tile_advantage_pairs
    })
    game_state_instance.add_attributes(**kwargs)
    setup_game_board(game_state_instance)
    return game_state_instance


def setup_game_board(game_state_instance: object):
    """Creates Map Object and passes initial tiles to setup the map"""
    map = inis_map.Map(game_state_instance.tiles)
    # map.render()
    game_state_instance.map = map
    return


def validate_player_agents(player_agent_instances) -> bool:
    """Needs to check it fits the form of tha ABC created in the inis_player_agents file?"""
    return True


def build_player_reference_instances_and_connect_to_agents(player_agents_instances: dict) -> None:
    """Creates a obkject to use to track other players movements etc"""
    for player_id in player_agents_instances:
        pass
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

    tile_card_pairs = dict((tile, card) for tile in tile_deck.tiles \
                           for card in advantage_deck.cards if tile.name == card.name)
    return tile_card_pairs


if __name__ == "__main__":
    # Test 1 - Build a new game setup?
    import inis_player_agents

    game_player_agents = { '0':inis_player_agents.dumbass_test_agent(0, "test1"),
                      '1':inis_player_agents.dumbass_test_agent(0, "test1"),
                      '2':inis_player_agents.dumbass_test_agent(0, "test1"),
                      '3':inis_player_agents.dumbass_test_agent(0, "test1")
                      }

    setup_inis(game_player_agents)

    # player_0 = {
    #     'name': 'Doug',
    #     'player_agent': inis_player_agents.dumbass_test_agent()
    # }
    #
    # player_1 = {
    #     'name': 'John',
    #     'player_agent': inis_player_agents.dumbass_test_agent()
    # }
    #
    # player_2 = {
    #     'name': 'Brad',
    #     'player_agent': inis_player_agents.dumbass_test_agent()
    # }
    #
    # player_3 = {
    #     'name': 'Test 2',
    #     'player_agent': inis_player_agents.dumbass_test_agent()
    # }
    #
    # player_agents = {
    #     0: player_0,
    #     1: player_1,
    #     2: player_2,
    #     3: player_3
    # }

