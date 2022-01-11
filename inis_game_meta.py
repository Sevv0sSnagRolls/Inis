"""
Rather than store all of the data that I don't want to be accessable by an ai with the
reference to the game state object

This allows everything to be brought together which is:
- players and agents
- game state
- game log
- card decks
- tile deck
"""

class inis_game():

    def __init__(self, player_agents list, players: list, game_state: object,
                 game_log: object):

        #Players
        #Handle to each player object created
        #Players list needs to be immutable - convert to a set
        #this means player order can change, but as list indexing is used by player id which is also
        #the position in a list because I'm lazy, better to make this data structure a const
        self.players = set(players)

        #Game Logger
        #
        self.game_log = game_log

        #Game State
        self.game_state = game_state

        #Tiles - References to instances of tile classes which make up the board
        #Tile index in the tiles list is the identifier used in the map matrix to allocate tile positions
        #Inis_game_state holds a method to find adjacent tiles and has a dictionary component which keeps
        #this information up to date
        #self.tile_deck = tile_deck

        #Cards - Handled by External Classes - These are references to those classes
        #self.action_cards = action_deck
        #self.epic_tale_cards = epic_tale_deck
        #self.advantage_cards = advantage_card_deck


if __name__ == "__main__":



