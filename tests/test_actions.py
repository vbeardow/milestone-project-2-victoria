from unittest.mock import patch, call
import pytest
from blackjack.hand import Hand
from blackjack.deck import Deck
from blackjack.deck import Card
from blackjack.actions import continue_playing, twist, stick_or_twist, reveal_cards
import config


def test_twist(my_hand: Hand, card_deck: Deck):
    """Test that after twist the number of cards in my_hand is 1

    Args:
        my_hand (Hand): A hand of cards
        deck (Deck): A deck of cards
    """
    twist(my_hand, card_deck)
    final_cards = my_hand.cards
    assert len(final_cards) == 1


@patch("builtins.input", side_effect=["x", "s"])
@patch("builtins.print")
def test_stick_or_twist_invalid_input(
    mock_print, mock_input, my_hand: Hand, card_deck: Deck
):
    """Tests exception is raised if invalid input is provided to stick or twist request

    Args:
        my_hand (Hand): Hand object representing a hand of cards
        card_deck (Deck): Deck object representing a deck of cards
    """
    stick_or_twist(my_hand, card_deck)
    mock_print.assert_called_once_with("Invalid input. Please enter either s or t.")


@patch("builtins.input", lambda *args: "s")
@patch("builtins.print")
def test_stick_is_printed(mock_print, my_hand: Hand, card_deck: Deck):
    """Test print output if user chooses to stick

    Args:
        mock_print (_type_): mock built in print function
        my_hand (Hand): Hand object representing a hand of cards
        card_deck (Deck): Deck object representing a deck of cards
    """
    stick_or_twist(my_hand, card_deck)
    mock_print.assert_called_once_with("Player has chosen to stick.")


@patch("builtins.input", lambda *args: "t")
@patch("blackjack.actions.twist")
def test_twist_is_called(mock_twist, my_hand: Hand, card_deck: Deck):
    """Test twist function is called if user chooses to twist

    Args:
        twist (_type_): mock function of twist action
        my_hand (Hand): Hand object representing a hand of cards
        card_deck (Deck): Deck object representing a deck of cards
    """
    stick_or_twist(my_hand, card_deck)
    mock_twist.assert_called_once_with(my_hand, card_deck)


@patch("builtins.print")
def test_reveal_one_card(mock_print, my_hand: Hand):
    """Tests print output if reveal one card is called

    Args:
        mock_print (_type_): mock built in print function
        my_hand (Hand): Hand object representing a hand of cards
    """
    my_hand.cards = [Card("Two", "Hearts"), Card("Four", "Spades")]
    reveal_cards(my_hand, False)
    mock_print.assert_called_once_with("Two of Hearts")


@patch("builtins.print")
def test_reveal_all_cards(mock_print, my_hand: Hand):
    """Tests print output if reveal all cards is called

    Args:
        mock_print (_type_): mock built in print function
        my_hand (Hand): Hand object representing a hand of cards
    """
    my_hand.cards = [Card("Two", "Hearts"), Card("Four", "Spades")]
    reveal_cards(my_hand, True)
    mock_print.assert_has_calls([call("Two of Hearts"), call("Four of Spades")])


@patch("builtins.input", lambda *args: "y")
def test_continue_playing_yes():
    """Asserts that config.playing is true after continue_playing is called and the user input "y" """
    config.playing = False
    continue_playing()
    assert config.playing is True


@patch("builtins.input", lambda *args: "n")
def test_continue_playing_no():
    """Asserts that config.game_on is false after continue_playing is called and the user input "n" """
    config.game_on = True
    continue_playing()
    assert config.game_on is False


@patch("builtins.input", side_effect=["x", "n"])
@patch("builtins.print")
def test_continue_playing_invalid_argument(mock_print, mock_input):
    """Asserts that and exception is raised if continue_playing is called and the user inputs an invalid value"""
    continue_playing()
    mock_print.assert_called_once_with("Invalid input. Please enter either y or n.")
