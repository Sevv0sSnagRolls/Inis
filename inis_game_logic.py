'''
Game Logic
--------------------------------------------------------------------
Module for holding all the functions that change the game state class.
Essentially enacting the ruleset

'''
import itertools
from inis_constants import GAME_TURNS


def play_inis_game(inis_game_obj: object, turn_start: str = 'assembly',
                   max_qty_of_turns: int = 200)-> object:
    """
    Function reponsible for playing game logic on game state

    Can return with a specific depth/round of turns played as a helper
    function for Ai agents

    :rtype: object
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
        winner = play_inis_turn(inis_game_obj, turn_start_number)
        number_of_turns_played += 1
    return inis.winner.name


def play_inis_turn(inis_game_obj: object, turn_start_number: int) -> bool:
    """
    Turn Logic for Inis Game

    This could also be handled by public and private functions and moving entire logic
    module ontop of game state...

    :param : inis_game_state -> inis_game_state class instance to be played
    :param : turn_start -> str description of where to start playing from GAME_TURNS global

    :return: pdated Game State, Winner Found T/F
    """
    if turn_start_number == 0:
        #checks for victory in assembly phase
        if play_inis_assembly_phase(inis_game_obj):
            return True

    if turn_start_number <= 1:
        play_inis_draft_phase(inis_game_obj)

    if turn_start_number <= 2:
        play_inis_seasons_phase(inis_game_obj)

    return False


def play_inis_assembly_phase(inis_game_state) -> bool:
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
    reset_all_players_hands(inis_game_state)
    if inis_game_state.player_count == 2:
        return draft_two_player_game(inis_game_state, 3)
    return draft_phase_normal_game(inis_game_state, 4)


def reset_all_players_hands(inis_game_state: object) -> None:
    for player in inis_game_state.players():
        player.hand = []
    return


def draft_phase_two_player_game(inis_game_state: object, hand_size: int) -> None:
    """
    Two Player game plays two drafting rounds with three cards in each
    :param inis_game_state: 
    :param hand_size: 
    :return:
    """
    #this is fucking dumb
    play_draft_phase(inis_game_state, hand_size)
    play_draft_phase(inis_game_state, hand_size)
    return


def draft_phase_normal_game(inis_game_state: object, hand_size: int) -> None:
    play_draft_phase(inis_game_state, hand_size)
    return


def play_draft_phase(inis_game_state: object, hand_size: int, verbose=True) -> 'List of hands by player_id':
    """
    Module to prompt players for a card selection/draft

    Relies on relation to inis card decks

    :return: None, game state will be updated
    """
    #need to add logger functionality here...
    if inis_game_state.event_logging():
        pass

    #player order
    player_order = itertools.cycle(inis_game_state.player_order)
    #dodgily do the first step to setup for passing cards onwards
    next(player_order)

    #Initialise the passed hands list/container
    #Need to make a dictionary so no confusion occur with the indexing
    passed_hands = {player_id: [] for player_id in player_order}
    drafted_hands = passed_hands.copy()
    hands = passed_hands.copy()

    #deal initial hands
    #deal cards container random shuffle element
    #will then assign each dealt container to each hand via keys
    dealt_lists = inis_game_state.action_cards.deal_cards(hand_size)
    for i in hands.keys():
        hands[i] = dealt_lists[i]

    for qty_of_cards_to_keep in list(range(1, hand_size)):
        #would be a good place to include multithreading if I knew what was going on....
        for player_id in inis_game_state.player_order:
            selection_made = False
            valid_move = False
            count = 0
            while (selection_made == False) and (valid_move == False):
                possible_hands = generate_possible_hands(hands[player_id], qty_of_cards_to_keep)
                selected_hand = player[player_id].agent.select_cards(possible_hands, qty_of_cards_to_keep)
                valid_move = validate_draft_selection_action(possible_hands, selected_hand)
                count += 1
                if count >= 10:
                    raise Exception('Error: too many attempts at drafting card objects')
            drafted_hands[player_id] = selected_hand.copy()
            passed_hand = generate_passed_hand( hands[player_id], selected_hand )
            next_player_id = next(player_order) #pull the next player from itertools.cycle
            passed_hands[next_player_id] = passed_hand
            if verbose:
                print("Drafting Phase")
                print("Quantity of Cards to keep: " + str(qty_of_cards_to_keep))
                print("Player: " + str(players[player_id].name))
                print("Current Hand: ")
                print(hands[player_id])
                print("Possible Hands to Draft: ")
                print(possible_hands)
                print("Selected Hand:")
                print(selected_hand)
                print("Passed on Cards")
                print(passed_hand)
        hands = pass_hands(drafted_hands.copy(), passed_hands)
    assign_drafted_cards(inis_game_state, hands)
    return True


def assign_drafted_cards(inis_game_state:object, drafted_hands:dict)->None:
    for player_id for in drafted_hands.keys():
        inis_game_state.players[player_id].hand += drafted_hands[player_id].copy()
    return True


def pass_hands(hands: dict, passed_hands: dict) -> list:
    for key in hands.keys():
        hands[key] = hands[key] + passed_hands[key]
    return hands


def generate_possible_hands(hand: list, qty_of_cards_to_keep: int) -> list:
    """
    Function to deal with return of itertools being a list of sets...
    :param qty_of_cards_to_keep: int specifying number of cards to keep this round
    :param hand: list of card object instances
    """
    return [ list(c) for c in list( itertools.combinations(hand, qty_of_cards_to_keep) ) ]


def generate_passed_hand(hand: list, selected_hand: list) -> list:
    """
    Find what was passed on from generated hands
    """
    return [card for card in hand if card not in selected_hand]


def play_inis_seasons_phase(inis_game_state: object) -> None:
    """
    Play through a full seasons phase

    Keeps playing until:
    All players pass or all players are out of cards
    and
    Each player has a pretender token that can have one

    :param inis_game_state:
    :return:
    """
    player_order = itertools.cycle(inis_game_state.player_order)

    all_have_pretender = False
    all_have_no_cards_playable = False
    all_pass = False:
    while (all_pass) or (all_have_no_cards_playable and all_have_pretender):
        inis_game_state.update()
        current_player_id = next(player_order)
        play_inis_seasons_turn(inis_game_state, current_player_id)
    return


def play_inis_seasons_turn(inis_game_state: object, current_player_id: int) -> None:
    """
    Handles a single players turn in Inis

    :param inis_game_state:
    :param current_player_id:
    :return:
    """
    current_player = inis_game_state.players[current_player_id]

    isValidAction = False
    while isValidAction == False:
        action_type, card = prompt_player_season_action(current_player)

        if action_type == 'seasons_card':
            #construct a new action queue object to be used by triskel cards
            #will by auto destructed by python at the end of the turn.

            current_actions_queue = action_queue()
            actions_queue.add( prompt_player_season_action(current_player) )
            for player in inis_game_state.players():
                actions_queue.append( prompt_player_triskel_action(player) )
            resolve_actions( actions_queue )
            inis.update()
            if inis.clash():
                inis.play_clash()

        elif action_type == 'pretender_token':
            take_pretender_token()

        elif action_type == 'pass':

            #resolve the pretender token or
    return

def prompt_player_season_action(turn_player_id):
    """
    Design some clever heap of actions
    :param turn_player_id:
    :return:
    """
    return

def prompt_player_triskel_action(player):


def resolve_actions(actions):
    """
    In order resolves the actions of a particular player - if they pass a list of actions
    makes a stack or wtv and in order works through them....
    :param actions:
    :return:
    """

def clash(inis_game_state: object) -> None:
    """
    Attempts to resolve a clash

    Card type must be an epic tale....

    :param inis_game_state:

    :return:
    """


    return


def validate_draft_selection_action(possible_hands: list, selected_hand: list) -> object:
    """
    Function just to validate that move AI has chosen is correct
    Probably should just generate options for the AI player in the player class....
    :param player:
    :param passed_on_cards:
    :param turn_number:
    :return:

    if player.hand ==  :
        print(player.name + " Has played an invalid drafting move)" )
        print(move...)
        return False
    if passed_cards == :
        print(player.name + " Has played an invalid drafting move)")
        return False
    if
    """
    if selected_hand in possible_hands:
        return True
    return False


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


class card_queue():

    def __init__(self):
        self.player = prompt_pl

if __name__ == "__main__":
    #TESTS