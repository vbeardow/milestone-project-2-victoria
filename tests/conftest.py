import pytest
from blackjack.hand import Hand
from blackjack.deck import Deck
from blackjack.chips import Chips


@pytest.fixture(scope="module")
def my_hand() -> Hand:
    """Create hand object for testing

    Returns:
        Hand: A hand object representing a hand of cards
    """
    return Hand()


@pytest.fixture(scope="module")
def deck() -> Deck:
    """Create deck object for testing

    Returns:
        Deck: A deck object representing a deck of cards
    """
    return Deck()


@pytest.fixture(scope="module")
def chips():
    """Create chips object for testing

    Returns:
        _type_: A Chips object representing a players betting chips
    """
    return Chips()
