"""

"""
from abc import ABC, abstractmethod


class agent(ABC):
    """
    Essentially the player can be boiled down to having four things asked of it
    1) Draft Cards
        Select Cards to keep and cards to pass from given hand
    2) play a round in a turn of the season phase where they can
        2.1) Select a season card to play
        2.2) Pass
        2.3) take a pretender token
    3) Play a triskel action in response to any event where it becomes a valid action
        The game logic code will prompt for triskel responses from every player after every action
    4) Clash Manouevre
        4.1) Citadel
        4.2) Peacefully resolve?
        4.3) Attack, retreat,
    """
    def __init__(self, player_id: int, name: str):
        self.player_id = player_id

        self.name = name
        #points to instances of player classes created which agent can use to model, simulate and store
        #visibile information about other players in the game
        #constructed as a list with the player_id == the player id/index of player in the game
        #so game state winners can "easily" be converted to mapping out what players might do...
        #self.reference_players = {}

        #game object for reference that gets updated as part of each main game loop
        #this allows agent to simulate or model shit...
        #self.reference_game = None

        self.is_bren = False
        self.clans_in_reserve = 12
        self.deeds = 0
        # Hand ==  list of card objects. Each Card has a name, type and function which is points to
        # Each Card will accept the game object and player and return the possible outcomes
        # from playing the card
        # the actual logic of what cards can be played in what order (permutations) for each turn
        # is left up to a function in this player class
        self.hand = []

    def generate_list_of_possible_actions(self, game, *hand):
        '''
        The idea of the function is to work out what combinations of cards can be played

        '''
        hand = self.hand if not hand

        for card in hand:
            actions.append(card(game, self.player_ID))

        return

    def turn_actions(self):

    @abstractmethod
    def draft_phase_select_cards(self):
        pass

    @abstractmethod
    def play_turn(self):
        """
        Return action type
        :return:
        """
        pass

    @abstractmethod
    def play_triskel_action(self):
        pass

    @abstractmethod
    def play_clash_citadels(self):
        """Hide in a citadel or not?"""
        pass

    @abstractmethod
    def play_resolve_clash(self):
        """Peacefully resolve request?"""
        pass

    @abstractmethod
    def play_clash_manouevre(self):
        """play manouevres"""
        pass


class human_agent(agent):
    '''
    Extends to funcationality to have terminal interaction with the game or potentially pygame if I cbf
    '''

    @abstractmethod
    def draft_phase_select_cards(self, possible_hands_to_keep):
        """
        :return:
        """
        print(self.player.hand)
        selected = raw_input('Select Card to play via index in hand: [0,1,2,3]': )
        return selected

    @abstractmethod
    def play_turn(self):
        pass

    @abstractmethod
    def play_triskel_action(self):
        pass

    @abstractmethod
    def play_clash_citadels(self):
        """Hide in a citadel or not?"""
        pass

    @abstractmethod
    def play_resolve_clash(self):
        """Peacefully resolve request?"""
        pass

    @abstractmethod
    def play_clash_manouevre(self):
        """play manouevres"""
        pass


class dumbass_test_agent(agent):
    '''
    Extends to funcationality to have terminal interaction with the game or potentially pygame if I cbf
    '''

    @abstractmethod
    def draft_phase_select_cards(self, possible_hands_to_keep: list):
        """
        :param: possible_hands_to_keep
                list of possible hands to keep which are lists of lists of function objects
                Can try out what will happen with each function object in agent
        :return:
        """
        return possible_hands_to_keep[0]

    @abstractmethod
    def play_turn(self):
        pass

    @abstractmethod
    def play_triskel_action(self):
        pass

    @abstractmethod
    def play_clash_citadels(self):
        """Hide in a citadel or not?"""
        pass

    @abstractmethod
    def play_resolve_clash(self):
        """Peacefully resolve request?"""
        pass

    @abstractmethod
    def play_clash_manouevre(self):
        """play manouevres"""
        pass

