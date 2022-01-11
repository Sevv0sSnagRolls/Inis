"""

"""
from abc import ABC, abstractmethod
import inis_player_class

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
    def __init__(self, name: str, player: object, reference_players: list, reference_game: object):
        self.name = name

        #points to the instance of the class which holds information about the components etc
        #for agent to use in game
        self.player = player

        #points to instances of player classes created which agent can use to model, simulate and store
        #visibile information about other players in the game
        #constructed as a list with the player_id == the player id/index of player in the game
        #so game state winners can "easily" be converted to mapping out what players might do...
        self.reference_players = reference_players

        #game object for reference that gets updated as part of each main game loop
        #this allows agent to simulate or model shit...
        self.reference_game = reference_game

    @abstractmethod
    def draft_phase_select_cards(self):
        pass

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

