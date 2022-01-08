"""
MODULE - Cards Handling
---------------------------------------------------------

Uses Factory Pattern probably a bad implementation case for it, but wanted to try it.

"""

from abc import ABC, abstractmethod

class card(ABC):
    """
    Class to hold meta info around each card function
    name = card name for terminal/UI
    type = [action, epic, advantage]
    Every function is designed to have the same set of inputs
    will possibly decorate every function to the form f(*args, *kwargs)
    to make sure I can account for every possibility...
    """

    def __init__(self, name, type):
        self.name = name
        self.type = type

    @abstractmethod
    def season(self, game, player) -> "Season action":
        """
        Possible season action for the card
        """

    @abstractmethod
    def triskel(self, game, player) -> "Triskel action":
        """
        Possible season action for the card
        """
        pass


class conquest(card):
    """
    Specific implementation of ABC 'card' for the conquest card


    """
    def __init__(self):
        self.name = 'conquest'
        self.type = 'action'

    def season(self, game, player) -> "season action":
        actions = []


        return actions

    def conquest_action(self, start_tile, end_tile, qty):

        return

    def triskel(self, game, player) -> "Triskel action":
        return None







def build_card_deck_objects(number_of_players):
    action_cards = getmembers(actions, isfunction)
    epic_tale_cards = getmembers(epic_tales, isfunction)
    advantage_cards = getmembers(advantages, isfunction)

    if number_of_players < 4:
        actions_cards.pop()

    '''
    BUILD
    '''
    triskels = []
    cards_a = []
    for _ in range(0,len(action_cards)):
        if card



    return action_cards, epic_tale_cards, advantage_cards


if __name__ == "__main__":
    action_cards = getmembers(actions, isfunction)
    epic_tale_cards = getmembers(epic_tales, isfunction)
    advantage_cards = getmembers(advantages, isfunction)
    #TEST 1 = Create Card Decks
    print(action_cards)
    print(epic_tale_cards)
    print(advantage_cards)

    #TEST 2 - Deal a Card

    #TEST 3 - Deal multiple Cards

    #TEST 4 - Deal Action Card Deck

    #TEST 5 - Deal Action Card Deck
