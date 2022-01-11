"""
WHY
"""
from setup_new_inis_game import setup_inis
import inis_game_logic

#Object for allowing game instances to start at a specific spot in the turn order with a given game state object
GAME_TURNS = { 'assembly' : 0,
               'drafting' : 1,
               'seasons'  : 2 }


def main() -> None:
    """
    Should handle menu items and all that bs that will convert it to pygame or maybe even JS

    So python is backend and JS will pass JSONs to python module to be convertd into
    game states to be represented on each players screen etc

    bit of a stretch goal so maybe pygame is easier...
    :return:
    """

    #prompt user selection, play game? or watch game?...

    if selection == 'new_game':
        start_new_game(player_agents)
        #might need to select whether game is viewed in terminal or wtv

    return


def start_new_game(player_agents: list, terminal_print=True) -> None:
    """
    :param agents: List of agents playing the game - references to objects, file paths containing the ABC
    of the agent desired? Idk
    :return:
    """
    current_game = setup_inis(player_agents)
    inis_game_logic.play_inis_game(current_game, terminal_print)
    return


def watch_game(database, game_index) -> None:
    return


if __name__ == "__main__":
    #TESTS