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
    def __init__(self):

    @abstractmethod
    def select_cards(self):
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
    def __init__(self):

    @abstractmethod
    def select_cards(self):
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



