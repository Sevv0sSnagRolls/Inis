"""
inis_action_cards.py


"""
from inis_cards import Card

#ACTION CARDS
#------------------------------------------------------------------------------------------------------------
class Conquest(Card):

    def __init__(self):
        self.name = 'Conquest'
        self.type = 'Action'
        self.blurb =   "Season Action: \n" \
                     + " Chose 1 territory. You may move any number of your clans from territories adjacent" \
                     + " to this chosen territory into it\n"

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
                     + " remove the festival token\n"

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
                     + " for each citadel in that territory\n"

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
                     + " Ignore the effect and discard it\n"

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
                     + " give it to another player and gain one deed\n"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class Migration(Card):

    def __init__(self):
        self.name = 'Migration'
        self.type = 'action'
        self.blurb =   "Season Action: \n" \
                     + " Choose 1 territory. Move 1 or more of your clans from there, \n" \
                     + " to 1 or more adjacent territories \n"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class Emissaries(Card):

    def __init__(self):
        self.name = 'Emissaries'
        self.type = 'action'
        self.blurb =   "Season Action: \n" \
                     + " Move 1 or more clans to an adjacent territory, \n" \
                     + " This does not initiate a clash \n"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class NewClans(Card):

    def __init__(self):
        self.name = 'New Clans'
        self.type = 'action'
        self.blurb =   "Seasons Action: \n" \
                     + " Place two clans in territories where you are present, \n" \
                     + " This can be in the same of different territories \n" \
                     + " If the attacked player has no action cards, remove 1 exposed clan instead. \n"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class Bard(Card):

    def __init__(self):
        self.name = 'Bard'
        self.type = 'action'
        self.blurb =   "Season Action: \n" \
                     + " Draw 1 Epic Tale Card \n" \
                     + " OR \n" \
                     + " Triskel Action \n" \
                     + " After 1 of your manoeuvres removes one or more opposing clans, \n" \
                     + " gain 1 deed \n"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return 1


class Raid(Card):

    def __init__(self):
        self.name = 'Raid'
        self.type = 'action'
        self.blurb =   "Triskel Action: \n" \
                     + " During a clash, after you have performed an attack manoeuvre, \n" \
                     + " Take 1 random action card from the attacked player's hand \n"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class ScoutsAndSpies(Card):

    def __init__(self):
        self.name = 'Scouts & Spies'
        self.type = 'action'
        self.blurb =   "Season Action: \n" \
                     + " Look at action cards in 1 opponent's hand \n" \
                     + " Then you may move 1 or more of your clans from 1 territory \n" \
                     + " to an adjacent territory \n"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None


class Sanctuary(Card):

    def __init__(self):
        self.name = 'Sanctuary'
        self.type = 'action'
        self.blurb =   "Season Action: \n" \
                     + " Place one sanctuary in any territory where you are present \n" \
                     + " Draw 1 Epic Tale Card \n"

    def season(self, inis_game_state, player_id) -> 'Season action':
        return None

    def triskel(self, inis_game_state, player) -> 'Triskel action':
        return None

#ACTION CARDS
#------------------------------------------------------------------------------------------------------------