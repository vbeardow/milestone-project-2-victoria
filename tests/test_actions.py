import pytest
import sys
from unittest.mock import patch
from unittest.mock import MagicMock
from blackjack.hand import Hand
from blackjack.deck import Deck
from blackjack.actions import *


@pytest.fixture
def my_hand() -> Hand:
    return Hand()


@pytest.fixture
def deck() -> Deck:
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


@patch("builtins.input", lambda *args: "x")
def test_stick_or_twist_invalid_input(my_hand: Hand, deck: Deck):
    """Tests exception is raised if invalid input is provided to stick or twist request

    Args:
        my_hand (Hand): Hand object representing a hand of cards
        deck (Deck): Deck object representing a deck of cards
    """
    with pytest.raises(Exception, match="Please enter either s or t"):
        stick_or_twist(my_hand, deck)


@patch("builtins.input", lambda *args: "s")
@patch("builtins.print")
def test_stick_is_printed(mock_print, my_hand: Hand, deck: Deck):
    """Test print output if user chooses to stick

    Args:
        mock_print (_type_): mocking built in print function
        my_hand (Hand): Hand object representing a hand of cards
        deck (Deck): Deck object representing a deck of cards
    """
    stick_or_twist(my_hand, deck)
    mock_print.assert_called_once_with("Player has chosen to stick.")


@patch("builtins.input", lambda *args: "t")
@patch("blackjack.actions.twist")
def test_twist_is_called(twist, my_hand, deck):
    """Test twist function is called if user chooses to twist

    Args:
        twist (_type_): mock function of twist action
        my_hand (Hand): Hand object representing a hand of cards
        deck (Deck): Deck object representing a deck of cards
    """
    stick_or_twist(my_hand, deck)
    twist.assert_called_once_with(my_hand, deck)
