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
import itertools

class inis_player():
    '''
    Class built from knowledge of other classes extistence

    '''
    def __int__(self, agent):
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

        #reference to the agent object which will be playing the game
        self.agent = agent


    def generate_draft_selections(self, turn_number):
        """
        For drafting phase, this function will
        - Generate hands possible to keep based on cards passed to the player
        - Generate lists of actions for each combination of hands to keep and permutation of play order
        - Generate
        :param turn_number:
        :return:
        """
        itertools.permutations

    def generate_list_of_possible_actions(self, game, *hand):
        '''
        The idea of the function is to work out what combinations of cards can be played

        '''
        hand = self.hand if not hand

        for card in hand:
            actions.append( card(game, self.player_ID) )
