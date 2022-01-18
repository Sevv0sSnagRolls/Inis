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
    """
    card_width = 30
    card_height = 12

    def __init__(self):
        self.name: str = ""
        self.type: str = ""
        self.blurb: str = ""

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
        self.j = 0

        #new line in display
        print(' ')
        # initial row
        print("|" + self.card_width*"-" + "|")
        self.print_section( self.name )
        self.print_section( self.type )
        print("|" + self.card_width * " " + "|")
        self.print_section( self.blurb )
        for i in range(self.j, self.card_height):
            print("|" + self.card_width * " " + "|")
        print("|" + self.card_width * "-" + "|")

    def print_section(self, text: str):
        line = ''
        n = len( text.split() )
        for i, word in enumerate( text.split()):
            sum = len(line) + 1 + len(word)
            if (word[-1] == ":") and (sum <= self.card_width):
                line += ' ' + word
                self.print_row(line, (self.card_width - len(line)))
                line = ''
            elif sum <= self.card_width:
                line += ' ' + word
            else:
                self.print_row(line, (self.card_width - len(line) ) )
                line = '' + word

            if i == (n-1):
                self.print_row(line, (self.card_width - sum))

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





if __name__ == "__main__":
    #TEST 1 = Create Card Decks
    #A = Warlord()
    #A.display_card()
    # TEST CODE
    def create_card_objects(player_count: int) -> dict:
        modules = ['inis_action_cards', 'inis_advantage_cards', 'inis_epic_tale_cards']
        cards = dict((module, create_card_objects_from_module(module, player_count)) for module in modules)
        return cards

    def test_cards_module(display_cards=False) -> None:
        import inis_constants
        tests_passed = False

        for player_count in range(2, 4):
            a = create_card_objects(player_count)

            for module, card_deck in a.items():

                if display_cards:
                    for _, card in card_deck.items():
                        card.display_card()

                if module == 'inis_action_cards':
                    if player_count == 4:
                        if len(card_deck) == 17:
                            tests_passed = True
                        else:
                            tests_passed = False
                    else:
                        if len(card_deck) == 13:
                            tests_passed = True
                        else:
                            tests_passed = False

                if module == 'inis_advantage_cards':
                    if len(card_deck) == len(inis_constants.TILES):
                        tests_passed = True
                    else:
                        tests_passed = False

                    tile_names = [tile[0] for tile in inis_constants.TILES]
                    for _, card in card_deck.items():
                        if card.name not in tile_names:
                            print(card.name)
                            print(tile_names)
                            tests_passed = False
                            print("                ")
                            print("Advantage cards names failed")
                            print("                ")
                            return

        if tests_passed:
            print("                ")
            print("ALL TESTS PASSED")
            print("                ")

        return

    #TEST 2 - Deal a Card
    test_cards_module()
