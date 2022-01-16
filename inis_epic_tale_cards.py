"""
inis_epic_tale_cards.py


"""
from inis_cards import Card

#EPIC TALE CARDS
#------------------------------------------------------------------------------------------------------------
class NuadaSilverhand(Card):

    def __init__(self):
        self.name = 'Nuada Silverhand'
        self.type = 'Epic_Tale'
        self.min_player_count = 2
        self.blurb =   "Season Action:" \
                     + " In each territory where you are chieftan. Place one clan for" \
                     + " each opponent who is also in that territory."

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


class BattleFrenzy(Card):

    def __init__(self):
        self.name = 'Battle Frenzy'
        self.type = 'Epic_Tale'
        self.min_player_count = 2
        self.blurb =   "Triskel Action:" \
                     + " During a clash, at the end of the citadels phase" \
                     + " Take all clans out, they are now all exposed clans."

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


class DagdasHarp(Card):

    def __init__(self):
        self.name = 'Dagdas_Harp'
        self.type = 'Epic_Tale'
        self.min_player_count = 2
        self.blurb =   "Seaons Action:" \
                     + " For each other epic tale card in your hand," \
                     + " place one clan in a territory where you are present." \
                     + " You can place at most three clans this way."

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



class TheDagdasClub(Card):

    def __init__(self):
        self.name = 'The_Dagdas_Club'
        self.type = 'Epic_Tale'
        self.min_player_count = 2
        self.blurb =   "Triskel Action:" \
                     + " When one of your clans would be removed, the clan stays," \
                     + " OR" \
                     + " When you attack, choose if the player loses a clan or a card."

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


class TheFianna(Card):

    def __init__(self):
        self.name = 'The_Fianna'
        self.type = 'Epic_Tale'
        self.min_player_count = 2
        self.blurb =   "Triskel Action:" \
                     + " During a clash, as a manoeuvre move one or more of your clans," \
                     + " exposed or not, to an adjacent territory." \
                     + " This does not initiate a clash"

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



class OgmasEloquence(Card):

    def __init__(self):
        self.name = 'Ogmas_Eloquence'
        self.type = 'Epic_Tale'
        self.min_player_count = 2
        self.blurb =   "Triskel Action:" \
                     + " During a clash, as a manoeuvre. The clash ends immediately"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class TheMorrigan(Card):

    def __init__(self):
        self.name = 'The_Morrigan'
        self.type = 'Epic_Tale'
        self.min_player_count = 2
        self.blurb =   "Seasons Action:" \
                     + " You may flip over the flock of crows token"\
                     + " You may initiate a clash in any territory, you" \
                     + " chose who is the instigator"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class ManannansHorses(Card):

    def __init__(self):
        self.name = 'Manannans_Horses'
        self.type = 'Epic_Tale'
        self.min_player_count = 2
        self.blurb =   "Seasons Action:" \
                     + " Move up to three of your clans from 1 territory to"\
                     + " 1 other territory anywhere in play"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class TheOtherWorld(Card):

    def __init__(self):
        self.name = 'The_Other_World'
        self.type = 'Epic_Tale'
        self.min_player_count = 2
        self.blurb =   "Seasons Action:" \
                     + " In a territory where you are present, for each sanctuary"\
                     + " in this territory you may place and or remove 1 clan there" \
                     + " You can do this up to three times" \

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class LugsSpear(Card):

    def __init__(self):
        self.name = 'Lugs_Spear'
        self.type = 'Epic_Tale'
        self.min_player_count = 2
        self.blurb =   "Triskel Action:" \
                     + " At the start of a clash,"\
                     + " triskel card cannot be played this clash"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None
























