"""

"""
from abc import ABC, abstractmethod
import re

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
    def __init__(self, name: str):
        self.player_id = None
        self.name = name
        self.is_bren = False
        self.clans_in_reserve = 12
        self.deeds = 0
        self.hand = []

    def generate_list_of_possible_actions(self, game, *hand):
        """Combinations of cards can be played"""
        # hand = self.hand if not hand
        # for card in hand:
        #     actions.append(card(game, self.player_ID))
        return

    def turn_actions(self):
        pass

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

    def draft_phase_select_cards(self, possible_hands_to_keep) -> list:
        """Shoulw be able to display hand and allow selection via indexes"""
        for i, hand in enumerate(possible_hands_to_keep):
            print("Hand Option ", i)
            for card in hand:
                card.display_card()
        input_valid = False
        # num_format = re.compile(r'^\-?[1-9][0-9]*$')
        while not input_valid:
            user_input = input("Select Hand Via Index 0, 1, 2...: ")
            if not user_input.isnumeric():
                print("input invalid, try a number")
            elif int(user_input) < 0 or int(user_input) > len(possible_hands_to_keep):
                print("input invalid, try a number in the available range")
            else:
                input_valid = True
        return possible_hands_to_keep[int(user_input)]

    def play_turn(self):
        pass

    def play_triskel_action(self):
        pass

    def play_clash_citadels(self):
        """Hide in a citadel or not?"""
        pass

    def play_resolve_clash(self):
        """Peacefully resolve request?"""
        pass

    def play_clash_manouevre(self):
        """play manouevres"""
        pass


class dumbass_test_agent(agent):
    '''
    Extends to funcationality to have terminal interaction with the game or potentially pygame if I cbf
    '''

    def draft_phase_select_cards(self, possible_hands_to_keep: list):
        """
        :param: possible_hands_to_keep
                list of possible hands to keep which are lists of lists of function objects
                Can try out what will happen with each function object in agent
        :return:
        """
        return possible_hands_to_keep[0]

    def play_turn(self):
        pass

    def play_triskel_action(self):
        pass

    def play_clash_citadels(self):
        """Hide in a citadel or not?"""
        pass

    def play_resolve_clash(self):
        """Peacefully resolve request?"""
        pass

    def play_clash_manouevre(self):
        """play manouevres"""
        pass

