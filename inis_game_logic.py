'''
Game Logic
--------------------------------------------------------------------
Module for holding all the functions that change the game state class.
Essentially enacting the ruleset

'''
#Object for allowing game instances to start at a specific spot
#in the turn order with a given game state object
GAME_TURNS = { 'assembly' : 0,
               'drafting' : 1,
               'seasons'  : 2 }


def play_inis_game(inis_game_state: object, turn_start: str,
                   max_qty_of_turns: int = 200)-> object:
    """
    Function reponsible for playing game logic on game state

    Can return with a specific depth/round of turns played as a helper
    function for Ai agents

    :param : inis_game_state -> inis_game_state class instance to be played
    :param : turn_start -> str description of where to start playing from GAME_TURNS global
    :param : max_qty_of_turns -> How many turns to play

    :return: game_state, winner
    """
    assert(turn_start) in GAME_TURNS.keys()
    turn_start_number = GAME_TURNS[turn_start]

    number_of_turns_played = 0
    winner = None
    while winner == None or number_of_turns_played >= max_qty_of_turns:
        winner = play_inis_turn(inis_game_state, turn_start_number)
        number_of_turns_played += 1
    return inis.winner.name


def play_inis_turn(inis_game_state: object, turn_start_number: int) -> bool:
    """
    Turn Logic for Inis Game

    :param : inis_game_state -> inis_game_state class instance to be played
    :param : turn_start -> str description of where to start playing from GAME_TURNS global

    :return: pdated Game State, Winner Found T/F
    """
    if turn_start_number == 0:
        if play_inis_assembly_phase(inis_game_state):
            return True

    if turn_start_number <= 1:
        play_inis_draft_phase(inis_game_state)

    if turn_start_number <= 2:
        play_inis_seasons_phase(inis_game_state)

    return False


def play_inis_assembly_phase(inis_game_state: object) -> bool:
    """
    Follows through Inis assembly phase procedure

    Returns a winner is the assembly phase specific winner function returns a winner

    :param inis_game_state:
    :return: game_state and winner ture/false
    """
    if inis_game_state.assembly_phase_check_for_victory():
        return True

    #run functions/methods of the class to update the game state
    #should place this in some other function or a class method to make it cleaner....
    inis_game_state.assign_chieftans()
    inis_game_state.assign_bren()
    inis_game_state.assign_advantage_cards()
    inis_game_state.flip_crows_token()
    inis_game_state.resolve_tiles_actions()
    return False


def play_inis_draft_phase(inis_game_state: object) -> None:
    """
    Plays through drafting by assigning action cards to each player

    Trick here is to understand what is visibile information for each player and be able to record that
    The visible information is which cards they passed along to the next player.
    So basically this choice of cards to be passed along can be stored in the player class
    as the passed on cards this turn.
    It then helps give a guesstimate of where each card ended up with the right logic...

    This function ultimately only ends up being the selector between which draft to run based off of player count

    :param inis_game_state:

    :return: None
    """
    if inis_game_state.player_count == 2:
        return draft_two_player_game(inis_game_state)
    return draft_phase_normal_game(inis_game_state)


def draft_phase_two_player_game(inis_game_state: object) -> None:

    return


def draft_phase_normal_game(inis_game_state: object) -> None:
    """
    Module to prompt players for a card selection/draft

    Relies on relation to inis card decks

    :return: None, game state will be updated
    """
    game_draft_log = {}
    for hand in inis_game_state.action_cards.deal_cards():
        players[i].hand = hand
        game_draft_log{player}

    for cards_to_pass in list(reversed(range(1, 4))):
        for player in inis_game_state.player_order:
            selection_made = False
            valid_move = False
            while (selection_made == False) and (valid_move == False):
                passed_hand, hand = player.agent.select_cards(cards_to_pass)
                validate_draft_action(hand, passed_hand, player)
    return


def play_inis_seasons_phase(inis_game_state: object) -> None:
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


def clash(inis_game_state):
    """
    Attempts to resolve a clash
    :param inis_game_state:
    :return:
    """


    return

def validate_draft_action(player, passed_on_cards, turn_number):
    """
    Function just to validate that move AI has chosen is correct
    Probably should just generate options for the AI player in the player class....
    :param player:
    :param passed_on_cards:
    :param turn_number:
    :return:
    """
    if player.hand ==  :
        print(player.name + " Has played an invalid drafting move)" )
        print(move...)
        return False
    if passed_cards == :
        print(player.name + " Has played an invalid drafting move)")
        return False
    if

    return True


def validate_seasons_move(player, passed_on_cards, turn_number):
    """
    Function just to validate that move AI has chosen is correct
    Probably should just generate options for the AI player in the player class....
    :param player:
    :param passed_on_cards:
    :param turn_number:
    :return:
    """
    if player.hand ==  :
        print(player.name + " Has played an invalid drafting move)" )
        print(move...)
        return False
    if passed_cards == :
        print(player.name + " Has played an invalid drafting move)")
        return False
    if

    return True


if __name__ == "__main__":
    #TESTS