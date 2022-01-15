"""
WHY

"""

from setup_new_inis_game import setup_inis
import inis_game_logic
import inis_player_agents

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
    start_new_game()

    #if selection == 'new_game':
    #   start_new_game()

    return


def start_new_game() -> None:
    """
    :param agents: List of agents playing the game - references to objects??

    :return:
    """
    player_agents = select_players()
    current_game = setup_inis(player_agents)
    #inis_game_logic.play_inis_game(current_game)
    return current_game


def select_players() -> dict:
    """
    Need some method of selecting who is playing each game

    :return:
    """
    player_0 = {
                name: 'Doug',
                player_agent: inis_player_agents.dumbass_test_agent()
                }

    player_1 = {
                name: 'John',
                player_agent: inis_player_agents.dumbass_test_agent()
                }

    player_2 = {
                name: 'Brad',
                player_agent: inis_player_agents.dumbass_test_agent()
                }

    player_3 = {
                name: 'Test 2',
                player_agent: inis_player_agents.dumbass_test_agent()
                }

    player_agents = { 0: player_0,
                      1: player_1,
                      2: player_2,
                      3: player_3
                      }

    return player_agents


def watch_game(database, game_index) -> None:
    return


if __name__ == "__main__":
    #TESTS
    main()