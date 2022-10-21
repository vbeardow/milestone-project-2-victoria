from blackjack.hand import Hand
from blackjack.deck import Deck


def twist(hand: Hand, deck: Deck):
    hand.add_card(deck.deal())


def stick_or_twist():
    pass
