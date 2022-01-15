"""
MODULE - Cards Handling
---------------------------------------------------------
Uses Factory Pattern to create cards
probably a bad implementation case for it, but wanted to try it.

Constructor classes (decks) will build the correct card classes
as instanced for a game instigated by the setup function.
"""
from abc import ABC, abstractmethod


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


class Conquest(Card):

    def __init__(self):
        self.name = 'Conquest'
        self.type = 'Action'
        self.blurb =   "Season Action: \n" \
                     + "Chose 1 territory. You may move any number of your clans from territories adjacent" \
                     + "to this chosen territory into it\n"

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


class Warlord(Card):

    def __init__(self):
        self.name = 'Warlord'
        self.type = 'action'
        self.blurb =   "Season Action: \n" \
                     + " Initiate a clash in a territory where you are present with you as the instigator \n" \
                     + "OR \n" \
                     + "Triskel Action: \n" \
                     + " During a clash with you involved, after a manoeuvre is performed, \n" \
                     + " place 1 clan in the territory and choose who performs the next manoeuvre\n"

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



class Druid(Card):

    def __init__(self):
        self.name = 'Druid'
        self.type = 'action'
        self.blurb =   "Season Action: \n" \
                     + " If Druid is the last action card in your hand, you cannot play it \n" \
                     + " Look at the discarded action cards and add 1 to your hand\n"

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


class NewAlliance(Card):

    def __init__(self):
        self.name = 'New Alliance'
        self.type = 'action'
        self.blurb =   "Season Action: \n" \
                     + " In a territory where you are present either:" \
                       "  Place 1 clan \n" \
                     + "  OR \n" \
                     + "  Choose an opponent with two or more clans in this territory \n" \
                     + "  and replace on of their clans with one of yours\n"

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


class Citadel(Card):

    def __init__(self):
        self.name = 'Citadel'
        self.type = 'action'
        self.blurb =   "Season Action: \n" \
                     + " Place 1 citadel In a territory where you are present." \
                       " If the advantage card for that territory has not been played,  \n" \
                     + " add it to your hand \n"

    def season(self, inis_game_state, player_id) -> 'Season action':
        actions = []

        return actions

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class Festival(Card):

    def __init__(self):
        self.name = 'Festival'
        self.type = 'action'
        self.blurb =   "Season Action: \n" \
                     + " In a territory where you are present and that has a sanctuary" \
                       " place one of your clans and the festival token there \n" \
                     + " Any player that initiates a clash in that territory removes one of \n" \
                     + " their clans from there. At the end of the seasons round. \n" \
                     + " remove the festival token"

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


class CraftsmenAndPeasants(Card):

    def __init__(self):
        self.name = 'Craftsmen & Peasants'
        self.type = 'action'
        self.blurb =   "Season Action: \n" \
                     + " In each territory where you are present, you may place 1 clan" \
                     + " for each citadel in that territory"

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


class Geis(Card):

    def __init__(self):
        self.name = 'Geis'
        self.type = 'action'
        self.blurb =   "Triskel Action: \n" \
                     + " When an opponent plays an action card," \
                     + " Ignore the effect and discard it"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class Exploration(Card):

    def __init__(self):
        self.name = 'Exploration'
        self.type = 'action'
        self.blurb =   "Season Action: \n" \
                     + " The Brenn chooses an emty location adjacent to 2 territories, \n" \
                     + " Draw one new terrirtory and place it there. \n" \
                     + " Place 1 clan on the new territory \n"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class MasterCraftsman(Card):

    def __init__(self):
        self.name = 'Master Craftsman'
        self.type = 'action'
        self.blurb =   "Season Action: \n" \
                     + " Discard one card (any type) if able then draw 1 epic tale card, \n" \
                     + " If not able, draw one epic tale card. \n" \
                     + " OR \n" \
                     + " Triskel Action \n" \
                     + " After you play and epic tale card, instead of discarding it, \n" \
                     + " give it to another player and gain one deed"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class Migration(Card):

    def __init__(self):
        self.name = 'Master Craftsman'
        self.type = 'action'
        self.blurb =   "Season Action: \n" \
                     + " Discard one card (any type) if able then draw 1 epic tale card, \n" \
                     + " If not able, draw one epic tale card. \n" \
                     + " OR \n" \
                     + " Triskel Action \n" \
                     + " After you play and epic tale card, instead of discarding it, \n" \
                     + " give it to another player and gain one deed"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


if __name__ == "__main__":
    #TEST 1 = Create Card Decks
    A = Warlord()
    A.display_card()

    #TEST 2 - Deal a Card

    #TEST 3 - Deal multiple Cards

    #TEST 4 - Deal Action Card Deck

    #TEST 5 - Deal Action Card Deck
