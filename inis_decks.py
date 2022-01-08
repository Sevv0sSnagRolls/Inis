'''
Module to create all cards and all decks used in inis

Decks will be passed back to the game module

Cards are written as classes with an action/method specific to each card
'''
from random import shuffle
from inspect import getmembers, isfunction
import inis_action_cards as actions
import inis_epic_tale_cards as epic_tales
import inis_advantage_cards as advantages


class inis_deck():
    """
    Meta class to hold all card objects of a certain type

    This will allow a method of dealing epic tale cards

    Will be extended to include some complex functionality for handling
    cards that interact with 'dealing'. i.e take 2, return one
    """

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.cards = []
        self.discard = []
        self.deck_size = len(self.cards) + len(self.discard)

    def shuffle_deck(self):
        shuffle(self.cards)
        return

    def deal_cards(self, qty=1):
        """
        Returns a list of references to card objects
        Adds these objects to discard pile
        Can do any quantity
        """
        assert qty <= self.deck_size

        if not self.cards:
            self.cards = self.discard
            self.discard = []
            self.shuffle_deck()

        if qty > len(self.cards):
            remainder = qty - len(self.cards)
            self.discard += [self.cards.pop() for _ in range(0, len(self.cards)) ]
            self.deal_cards(remainder) #this is cheeky and a bit shit

        return self.discard[-qty:]


class action_card_deck(inis_deck):

    def assembly_deal(self):
        for card in self.cards:
            deal_card


class advantage_card_deck(inis_deck):

    def advantage_card_deal(self):
        pass
