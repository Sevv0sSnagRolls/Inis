"""
MODULE - Cards Handling
---------------------------------------------------------
Uses Factory Pattern to create cards
probably a bad implementation case for it, but wanted to try it.

Constructor classes (decks) will build the correct card classes
as instanced for a game instigated by the setup function.
"""
from abc import ABC, abstractmethod


class card(ABC):
    """
    Class to hold meta info around each card function
    name = card name for terminal/UI
    type = [action, epic, advantage]

    Every function is designed to have the same set of inputs
    as each card can have a season, triskel or both

    discard handled seperately
    """

    def __init__(self, name, type, blurb):
        self.name = name
        self.type = type
        self.blurb = blurb

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


class conquest(card):
    """
    Specific implementation of ABC 'card' for the conquest card
    Must return all possible actions the player can take as a formatted change of game state?
    """
    def __init__(self):
        self.name = 'conquest'
        self.type = 'action'
        self.blurb = 'Move one or move clans from one territory to an opposing territory'

    def season(self, inis_game_state, player_id) -> 'Season action':
        actions = []
        clans_copy = inis_game_state.clans.copy()
        for tile_id, clan_qty in enumerate(inis_game_state.clans[player_id]):
            #relies on adjacent tiles being a dynamically updated list as each tile is added to the game
            #so it doesn't need to update every time a tile is added'
            for adjacent_tile_id in tiles[tile_id].adjacent_tiles:
                for i in range(0, clan_qty):
                    pass

        return actions

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None

    def __str__(self):
        return 'conquest'







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
