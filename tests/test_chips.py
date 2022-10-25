"""Tests the class Chips, the associated methods and attributes"""

from unittest.mock import patch
from blackjack.chips import Chips


def test_win_bet(chips: Chips):
    """Test the chips total increases if bet is won

    Args:
        chips (Chips): A chips class with a total of 100
    """
    chips.bet = 10
    chips.win_bet()
    assert chips.total == 100 + 10


def test_lose_bet(chips: Chips):
    """_summary_

    Args:
        chips (Chips): A chips class with a total of 100
    """
    chips.bet = 10
    chips.lose_bet()
    assert chips.total == 100 - 10


@patch("builtins.input", lambda *args: 12)
def test_place_bet(chips: Chips):
    """Tests that if the function place_bet is called,
    the property bet of the chips is equal to the user input

    Args:
        chips (Chips): A chips class with a total of 100
    """
    chips.place_bet()
    assert chips.bet == 12


@patch("builtins.input", side_effect=["twelve", 12])
@patch("builtins.print")
def test_place_bet_non_integer(mock_print, mock_input, chips: Chips):
    """Tests that a value error is thrown if the bet the user inputs is not an integer value

    Args:
        chips (Chips): A chips class with a total of 100
    """
    chips.place_bet()
    mock_print.assert_called_once_with("Please enter an integer")


@patch("builtins.input", side_effect=[110, 12])
@patch("builtins.print")
def test_place_bet_exceeds_total(mock_print, mock_input, chips: Chips):
    """Tests that correct print statement is called if the bet the user inputs exceeds the total

    Args:
        chips (Chips): A chips class with a total of 100
    """
    chips.place_bet()
    mock_print.assert_called_once_with(
        f"You can not place a bet higher than your current total of {chips.total}."
    )
