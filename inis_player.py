"""
Module for player class

player is ab object that holds player attributes

It also holds methods that will be useful to any agent acting as the player
Such as finding out all actions available to the agent each turn from their hand

This function can also be used on each other player in the game
Based off of the action card deck, can use logic to estimate probability of something occuring
Knowledge from draft phase means it can maybe workout who is most likely to have what...

Generate_list_of()... is useful in the drafting phase too, as it will help assign a value to each card
"""


class inis_player():
    '''
    Class built from knowledge of other classes extistence

    '''
    def __int__(self):
        self.player_ID =
        self.is_bren = False
        self.clans_in_reserve = 12
        self.deeds = 0

        #Hand ==  list of card objects. Each Card has a name, type and function which is points to
        #Each Card will accept the game object and player and return the possible outcomes
        #from playing the card
        #the actual logic of what cards can be played in what order (permutations) for each turn
        #is left up to a function in this player class
        self.hand = []

        self.victory =


    def generate_list_of_possible_actions(self, game):
        '''
        The idea of the function is to work out what combinations of cards can be played

        '''
        for card in self.hand:
            actions.append( card(game, self.player_ID) )
