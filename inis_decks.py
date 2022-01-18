"""
-----------------------------------------------------
inis_decks.py
-----------------------------------------------------
"""
import random
from inis_cards import create_card_objects_from_module

class inis_card_deck():

    def __init__(self, name: str, type: str, cards:list):
        self.name = name
        self.type = type
        self.cards = cards
        self._shuffle_deck()
        self.discard = []
        self.deck_size = len(self.cards) + len(self.discard)

    def deal_cards(self, qty=1, card_object_instance=None):
        """Deals qty of cards, adds to discard/used pile"""
        assert qty or card_object_instance

        if card_object_instance:
            self.discard = self.cards.pop( self.cards.index(card_object_instance) )
            return card_object_instance

        assert qty <= self.deck_size
        if qty > len(self.cards): #kind of cheating here as it's not the proper way to use up a deck and then reshuffle discard...
            self.reset_deck()
        self.discard += [self.cards.pop() for i in range(0, qty)]
        return self.discard[-qty:]

    def _reset_deck(self):
        """Make discard into deck"""
        self.cards = self.discard
        self.discard = []
        self.shuffle_deck()

    def _shuffle_deck(self):
        """ Guess """
        random.shuffle(self.cards)
        return

    @classmethod
    def create_action_deck(cls, player_count: int) -> object:
        """Creates action card deck instance"""
        cards = list(create_card_objects_from_module('inis_action_cards', player_count).values())
        return cls('actionDeck', 'action', cards)

    @classmethod
    def create_advantage_deck(cls, player_count: int) -> object:
        """Creates action card deck instance"""
        cards = list(create_card_objects_from_module('inis_advantage_cards', player_count).values())
        return cls('advantageDeck', 'advantage', cards)

    @classmethod
    def create_epic_tale_deck(cls, player_count: int) -> object:
        """Creates action card deck instance"""
        cards = list(create_card_objects_from_module('inis_epic_tale_cards', player_count).values())
        return cls('epicTaleDeck', 'epic_tale', cards)


if __name__ == "__main__":
    action_deck = inis_card_deck.create_action_deck(2)
    cards = action_deck.deal_cards(2)
    print( [card.name for card in cards] )
    print( [card.name for card in action_deck.cards])
    card = action_deck.deal_cards( 1, action_deck.cards[4] )
    print( card.name )
    action_deck._shuffle_deck()
    print([card.name for card in action_deck.cards])
    for card in action_deck.cards:
        card.display_card()