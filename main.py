'''
Main Game Function is a wrapper for making changes to the Inis game class
Handling Turn Events and exiting when a winner is found
'''


#Object for allowing game instances to start at a specific spot in the turn order with a given game state object
GAME_TURNS = { 'assembly' : 0,
               'drafting' : 1,
               'seasons'  : 2 }

def main():
    """
    Should handle menu items and all that bs that will convert it to pygame or maybe even JS

    So python is backend and JS will pass JSONs to python module to be convertd into
    game states to be represented on each players screen etc

    bit of a stretch goal so maybe pygame is easier...
    :return:
    """
    return


def setup_inis(players):
    """
    Function responsible for calling all sub modules and functions to setup game and players
    to allow turns to be played
    """
    inis_game_state = build_game_state_object()
    build_decks(number_of_players)
    return


def play_inis_game(inis_game_state: object, turn_start: str, depth: int = 200)-> object:
    """
    Function reponsible for playing game logic on game state
    Can return with a specific depth/round of turns played as a helper
    function for Ai agents
    :param inis: How many
    :param depth: How many turns to play - Will also exit and consider is a draw
    to avoid the game getting stuck
    :return: game_state, winner
    """
    assert(turn_start) in GAME_TURNS.keys()

    i = 0
    winner = None
    while winner == None or i >= depth:
        inis_game_state, winner = play_inis_turn(inis_game_state, turn_start)
        i += 1
    return inis_game_state, inis.winner.name


def play_inis_turn(inis_game_state, turn_start):
    """
    Turn Logic for Inis Game
    :params: passes the reference to the class instance holding all the information about the current game
    That needs to be played through.
    This could be the real game or an AI simulation of game turns to develop the best strategy.

    :return: Updated Game State, Winner Found T/F
    """
    if turn_start == 0:
        assembly_phase(inis_game_state)

    if turn_start <= 1:
        draft(inis_game_state)

    if turn_start <= 2:
        seasons_phase(inis_game_state)

    return inis_game_state, False


def assembly_phase(inis_game_state: object) -> None:
    if inis_game_state.check_for_victory():
        return inis_game_state, True
    inis_game_state.assign_bren()
    inis_game_state.assign_advantage_cards()
    inis_game_state.flip_crows_token()
    inis_game_state.resolve_tiles_actions()
    return


def draft_phase(inis_game_state: object) -> None:
    """
    Plays through drafting by assigning action cards to each player

    Action cards have been chosen to be represented in a slightly odd way...

    Trick here is to understand what is visibile information for each player and be able to record that
    The visible information is which cards they passed along to the next player.
    So basically this choice of cards to be passed along can be stored in the player class
    as the passed on cards this turn.
    It then helps give a guesstimate of where each card ended up with the right logic...

    This function ultimately only ends up being the selector between which draft to run based off of player count

    :param inis_game_state:

    :return:
    """
    if inis_game_state.player_count == 2
        return draft_two_player_game(inis_game_state)
    return draft_game(inis_game_state)


def draft_two_player_game():
    return


def draft_game(inis_game_state):
    """
    Module to prompt players for a card selection/draft

    :return: None, game state will be updated
    """
    # deal cards
    hand: object
    for hand in inis_game_state.action_cards.deal_cards():
        players[i].hand = hand

    for i in list(reversed(range(1, 4))):
        for player in inis_game_state.player_order:
            selection_made = False
            valid_move = False
            while (selection_made == False) and (valid_move == False):
                passed_hand, hand = player.select_cards()
                validate_draft(hand, passed_hand, player)

    return


def seasons_phase(inis_game_state):
    """
    Play throuh a full seasons phase

    :param inis_game_state:
    :return:
    """

    all_pass = False:
    while all_pass = False:
        '''
        I almost want a function to update all chieftans and everything so all new info is available to AI
        every time anything happens
        '''
        inis.update()

        #step 1 - Make sure every player agent is aware of the victory conditions met by each player each turn
        inis.check_victory_conditions()

        #step 2 -

        inis.update
        if inis.clash():
            inis.play_clash()

    return inis_game_state



#use deepcopy to pass the game object to any players to allow decision making from current game state
#they have access to all the functions...

'''
Do i need some form of action validation to make sure no AI is cheating??
'''

def validate_draft_move(player, passed_on_cards, turn_number):
    '''
    Function just to validate that move AI has chosen is correct
    Probably should just generate options for the AI player in the player class....
    :param player:
    :param passed_on_cards:
    :param turn_number:
    :return:
    '''


if __name__ == "__main__":
    #TESTS