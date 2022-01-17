"""
----------------------------------------------
inis_main.py
---------------------------------------------
Here to be process director for either using pygame or wtv for setups and divert
for AI only play, human play who knows.
"""


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
    """
    Aim is to basically setup a cmd line interaction with main

    which will start a webpage and JS file
    s
    or just have standalone JS which will replace a game from game log
    or SQL database of previous games
    maybe should have built this in JS?? fuck me

    :param database:
    :param game_index:
    :return:
    """

    return


if __name__ == "__main__":
    #TESTS
    main()