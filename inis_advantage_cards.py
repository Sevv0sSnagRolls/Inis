"""
inis_advantagen_cards.py


"""
from inis_cards import Card

#ACTION CARDS
#------------------------------------------------------------------------------------------------------------
class Plains(Card):

    def __init__(self):
        self.name = 'Plains'
        self.type = 'Advantage'
        self.min_player_count = 2
        self.blurb =   "Season Action:" \
                     + " Move one or more of your clans from the Plains to one or more adjacent" \
                     + " territories."

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


class GatesOfTirNaNog(Card):

    def __init__(self):
        self.name = 'Gates Of Tir Na Nog'
        self.type = 'Advantage'
        self.min_player_count = 2
        self.blurb =   "Triskel Action:" \
                     + " When resolving tile effect, draw one more epic tale card," \
                     + " keep one and discard the other."

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class Meadows(Card):

    def __init__(self):
        self.name = 'Meadows'
        self.type = 'Advantage'
        self.min_player_count = 2
        self.blurb =   "Season Action:" \
                     + "when drawing an epic tale card, draw one more epic tale card," \
                     + " keep one and discard the other."

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class Mountains(Card):

    def __init__(self):
        self.name = 'Meadows'
        self.type = 'Advantage'
        self.min_player_count = 2
        self.blurb =   "Triskel Action:" \
                     + " When moving one or more clans into the mountains," \
                     + " Ignore the mountains territory effect."

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class Highlands(Card):

    def __init__(self):
        self.name = 'Highlands'
        self.type = 'Advantage'
        self.min_player_count = 2
        self.blurb = "Triskel Action:" \
                     + " When starting resolution of a clash in the highlands," \
                     + " Choose one player with one or more exposed clans to start."

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class Forest(Card):

    def __init__(self):
        self.name = 'Forest'
        self.type = 'Advantage'
        self.min_player_count = 2
        self.blurb = "Triskel Action:" \
                     + " After you play an epic tale card," \
                     + " Draw 1 epic tale card."

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class Moor(Card):

    def __init__(self):
        self.name = 'Moor'
        self.type = 'Advantage'
        self.min_player_count = 2
        self.blurb = "Triskel Action:" \
                     + " At any time, look at the epic tale cards" \
                     + " in an opponents hand."

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None



class SaltMine(Card):

    def __init__(self):
        self.name = 'Salt Mine'
        self.type = 'Advantage'
        self.min_player_count = 2
        self.blurb = "Triskel Action:" \
                     + " After you play a seasons card, randomly take" \
                     + " one action card from an opponents hand." \
                     + " Then give that player one action card"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None



class Valley(Card):

    def __init__(self):
        self.name = 'Valley'
        self.type = 'Advantage'
        self.min_player_count = 2
        self.blurb = "Triskel Action:" \
                     + " After you play a seasons card, place" \
                     + " one clan in a territory where you are present."

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None



class StoneCircle(Card):

    def __init__(self):
        self.name = 'Stone Circle'
        self.type = 'Advantage'
        self.min_player_count = 2
        self.blurb = "Triskel Action:" \
                     + " After you play an epic tale card, you may remove one of your clans" \
                     + " from the territory where it was played to keep the card."

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None



class Swamp(Card):

    def __init__(self):
        self.name = 'Swamp'
        self.type = 'Advantage'
        self.min_player_count = 2
        self.blurb = "None"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class IronMine(Card):

    def __init__(self):
        self.name = 'Iron Mine'
        self.type = 'Advantage'
        self.min_player_count = 2
        self.blurb = "Triskel Action:" \
                     + " After you perform an attack manoeuvre, the attacked player" \
                     + " must remove a player and discard and action card."

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class Cove(Card):

    def __init__(self):
        self.name = 'Cove'
        self.type = 'Advantage'
        self.min_player_count = 2
        self.blurb = "Triskel Action:" \
                     + " After you play a seasons card. Take the card set aside and add it to your hand"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class MistyLands(Card):

    def __init__(self):
        self.name = 'Misty Lands'
        self.type = 'Advantage'
        self.min_player_count = 2
        self.blurb = "Seasons Action:" \
                     + " Discard one or more action cards to draw that many epic tale cards"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class Hills(Card):

    def __init__(self):
        self.name = 'Hills'
        self.type = 'Advantage'
        self.min_player_count = 2
        self.blurb = "Triskel Action:" \
                     + " When an attack manoeuvre is performed against you in the hills,"\
                     + " ignore the attack, do not remove clan or action card"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class LostVale(Card):

    def __init__(self):
        self.name = 'Lost Vale'
        self.type = 'Advantage'
        self.min_player_count = 2
        self.blurb = "Triskel Action:" \
                     + " When an attack manoeuvre is performed against you in the hills,"\
                     + " ignore the attack, do not remove clan or action card"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None
