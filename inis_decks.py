"""
-----------------------------------------------------
inis_decks.py
-----------------------------------------------------
Module to create all cards and all decks used in inis
Decks will be passed back to the game module
Cards are written as classes with an action/method specific to each card
import or card objects is done by module naming conventions
construction of card deck
"""
import random

class inis_card_deck():
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
        random.shuffle(self.cards)
        return

    def deal_cards(self, qty=1):
        """
        Returns a list of references to card objects
        Adds these objects to discard pile
        Can do any quantity
        """
        assert qty <= self.deck_size

        #kind of cheating here as it's not the proper way to use up a deck and then reshuffle discard...
        if qty > len(self.cards):
            self.reset_deck()

        self.discard += [self.cards.pop() for _ in range(0, len(self.cards))]

        return self.discard[-qty:]

    def reset_deck(self):
        self.cards = self.discard
        self.discard = []
        self.shuffle_deck()


class advantage_card_deck(inis_deck):

    def advantage_card_deal(self):
        pass


