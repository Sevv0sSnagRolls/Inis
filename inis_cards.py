"""
MODULE - Cards Handling
---------------------------------------------------------
Uses Factory Pattern to create cards
probably a bad implementation case for it, but wanted to try it.

Constructor classes (decks) will build the correct card classes
as instanced for a game instigated by the setup function.
"""
from abc import ABC, abstractmethod
import sys, inspect
import inis_action_cards

class Card(ABC):
    """
    Class to hold meta info around each card function
    name = card name for terminal/UI
    type = [action, epic, advantage]

    Every function is designed to have the same set of inputs
    as each card can have a season, triskel or both

    discard handled seperately
    """

    @abstractmethod
    def season(self, inis_game_state, player) -> "Season action":
        """
        Possible season action for the card
        """
        pass

    @abstractmethod
    def triskel(self, inis_game_state, player) -> "Triskel action":
        """
        Possible season action for the card
        """
        pass

    def display_card(self):
        print(self.name + ' - ' + self.type)
        print(self.blurb)


def create_card_objects(module_name: str) -> list:
    """
    Bit fancy, relies on modules having cards of only one type
    Could add a check for class attributes to double check this when instance
    is created and destory the instance if it's incorrect
    :param module_name:
    :return:
    """
    action_cards = {}
    for name, obj in inspect.getmembers(sys.modules[module_name]):
        if ( inspect.isclass(obj) ) and (not inspect.isabstract(obj)):
            class_ = getattr(sys.modules[module_name], name)
            action_cards.update( {name : class_()} )
    return action_cards


if __name__ == "__main__":
    #TEST 1 = Create Card Decks
    #A = Warlord()
    #A.display_card()

    #TEST 2 - Deal a Card
    a = create_card_objects('inis_action_cards')
    print( a['Bard'].triskel(0, 0) )

    for _, card in a.items():
        card.display_card()
    #TEST 3 - Deal multiple Cards

    #TEST 4 - Deal Action Card Deck

    #TEST 5 - Deal Action Card Deck
