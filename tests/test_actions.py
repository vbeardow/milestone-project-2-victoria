import pytest
from blackjack.hand import Hand
from blackjack.deck import Deck
from blackjack.actions import *


@pytest.fixture
def my_hand():
    return Hand()


@pytest.fixture
def deck():
    return Deck()


def test_twist(my_hand: Hand, deck: Deck):
    """Test that after twist the number of cards in my_hand is 1

    Args:
        my_hand (Hand): A hand of cards
        deck (Deck): A deck of cards
    """
    twist(my_hand, deck)
    final_cards = my_hand.cards
    assert len(final_cards) == 1


def test_stick_or_twist():
    pass


def test_reveal():
    pass
