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
import importlib

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
        """
        Need to turn this into a bit of ASCII art of something with a character counter
        and word writer to terminal to make text in a nice display format i.e
        ----------------------
        |-<NAME>             |
        |-<TYPE>             |
        |-<Action>           |
        |-<Action #1 Text>   |
        |-<OR>               |
        |-<Action #2 Text>   |
        ----------------------
        Size to the largest card somehow??
        :return:
        """
        card_width = 30
        card_height = 12
        self.j = 0

        #new line in display
        print(' ')
        # initial row
        print("|" + card_width*"-" + "|")
        self.print_section( self.name, card_width )
        self.print_section( self.type, card_width )
        print("|" + card_width * " " + "|")
        self.print_section( self.blurb, card_width )
        for i in range(self.j, card_height):
            print("|" + card_width * " " + "|")
        print("|" + card_width * "-" + "|")

    def print_section(self, text: str, card_width: int):
        line = ''
        n = len( text.split() )
        for i, word in enumerate( text.split()):
            sum = len(line) + 1 + len(word)
            if (word[-1] == ":") and (sum <= card_width):
                line += ' ' + word
                self.print_row(line, (card_width - len(line)))
                line = ''
            elif sum <= card_width:
                line += ' ' + word
            else:
                self.print_row(line, (card_width - len(line) ) )
                line = '' + word

            if i == (n-1):
                self.print_row(line, (card_width - sum))

    def print_row(self, line: str, remainder: int):
        print("|" + line + remainder*' ' + "|")
        self.j += 1

def create_card_objects_from_module(module_name: str, player_count: int) -> list:
    """
    Bit fancy, relies on modules having cards of only one type
    Could add a check for class attributes to double check this when instance
    is created and destory the instance if it's incorrect
    :param module_name:
    :return:
    """
    importlib.import_module(module_name)
    cards = {}
    for name, obj in inspect.getmembers(sys.modules[module_name]):
        if ( inspect.isclass(obj) ) and (not inspect.isabstract(obj)):
            class_ = getattr(sys.modules[module_name], name)
            instance = class_()
            if instance.min_player_count <= player_count:
                cards.update( {name : instance} )
    return cards


def create_card_objects(player_count: int) -> dict:
    modules = ['inis_action_cards', 'inis_advantage_cards', 'inis_epic_tale_cards']
    cards = dict( (module, create_card_objects_from_module(module, player_count)) for module in modules)
    return cards

def test_cards(player_count: int) -> None:
    a = create_card_objects(player_count)
    for module, card_deck in a.items():
        for _, card in card_deck.items():
            card.display_card()
    return

if __name__ == "__main__":
    #TEST 1 = Create Card Decks
    #A = Warlord()
    #A.display_card()

    #TEST 2 - Deal a Card
    test_cards(2)
