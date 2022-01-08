"""
Game Logic

Module for holding all the functions that change the game state class.
Essentially enacting the ruleset

"""

def setup_inis(players) -> object:
    """
    Function responsible for calling all sub modules and functions to setup game and players
    to allow turns to be played

    Players need to be of a particular format, may need some validatin function here for that purpose
    """
    current_game_log = inis_game_logger()
    inis_game_state = build_game_state_object()
    build_decks(number_of_players)
    return



