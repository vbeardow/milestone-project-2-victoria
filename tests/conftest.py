"""Creates fixtures that are repeatedly used throughout tests"""

import pytest
from blackjack.hand import Hand
from blackjack.deck import Deck
from blackjack.chips import Chips


@pytest.fixture(scope="module")
def player_hand() -> Hand:
    """Create hand object for testing

    Returns:
        Hand: A hand object representing a hand of cards
    """
    return Hand()


@pytest.fixture(scope="module")
def dealer_hand() -> Hand:
    """Create hand object for testing

    Returns:
        Hand: A hand object representing a hand of cards
    """
    return Hand()


@pytest.fixture(scope="class")
def card_deck() -> Deck:
    """Create deck object for testing

    Returns:
        Deck: A deck object representing a deck of cards
    """
    return Deck()


@pytest.fixture(scope="class")
def chips() -> Chips:
    """Create chips class for testing
    Returns:
        _type_: an instance of a class of chips
    """
    return Chips()
