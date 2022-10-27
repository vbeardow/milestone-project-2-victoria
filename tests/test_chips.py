"""Tests the class Chips, the associated methods and attributes"""

from unittest.mock import patch
from blackjack.chips import Chips
import blackjack.game_config as game_config


def test_win_bet(chips: Chips) -> None:
    """Test the chips total increases if bet is won

    Args:
        chips (Chips): A chips class with a total of 100
    """
    chips.bet = 10
    chips.win_bet()
    assert chips.total == 100 + 10


def test_lose_bet(chips: Chips) -> None:
    """_summary_

    Args:
        chips (Chips): A chips class with a total of 100
    """
    chips.bet = 10
    chips.lose_bet()
    assert chips.total == 100 - 10


@patch("builtins.input", lambda *args: 12)
def test_place_bet(chips: Chips) -> None:
    """Tests that if the function place_bet is called,
    the property bet of the chips is equal to the user input

    Args:
        chips (Chips): A chips class with a total of 100
    """
    chips.place_bet()
    assert chips.bet == 12


@patch("builtins.input", side_effect=["twelve", 12])
@patch("builtins.print")
def test_place_bet_non_integer(mock_print, mock_input, chips: Chips) -> None:
    """Tests that a value error is thrown if the bet the user inputs is not an integer value

    Args:
        mock_print (_type_): mock built in print function
        mock_input (_type_): mock built in input function
        chips (Chips): A chips class with a total of 100
    """
    chips.place_bet()
    mock_print.assert_called_once_with("Please enter an integer")


@patch("builtins.input", side_effect=[110, 12])
@patch("builtins.print")
def test_place_bet_exceeds_total(mock_print, mock_input, chips: Chips) -> None:
    """Tests that correct print statement is called if the user inputs a bet that exceeds the total chips

    Args:
        mock_print (_type_): mock built in print function
        mock_input (_type_): mock built in input function
        chips (Chips): A chips class with a total of 100
    """
    chips.place_bet()
    mock_print.assert_called_once_with(
        f"You can not place a bet higher than your current total of {chips.total}."
    )


@patch("builtins.input", side_effect=[-10, 12])
@patch("builtins.print")
def test_negative_bet(mock_print, mock_input, chips: Chips) -> None:
    """Tests that correct print statement is called if the user inputs a negative bet

    Args:
        mock_print (_type_): mock built in print function
        mock_input (_type_): mock built in input function
        chips (Chips): A chips class with a total of 100
    """
    chips.place_bet()
    mock_print.assert_called_once_with(
        "You can not place a negative bet, please try again."
    )


def test_no_chips_remaining_returns_false(chips: Chips) -> None:
    """Tests that no_chips_remaining returns False if chips.total is larger than 0

    Args:
        chips (Chips): A Chips object representing a player's betting chips
    """
    chips.total = 100
    output = chips.no_chips_remaining()
    assert output is False


def test_no_chips_remaining_returns_true(chips: Chips) -> None:
    """Tests that no_chips_remaining returns True if chips.total is zero

    Args:
        chips (Chips): A Chips object representing a player's betting chips
    """
    chips.total = 0
    output = chips.no_chips_remaining()
    assert output is True


@patch("builtins.print")
def test_no_chips_remaining_prints_statement_to_player(
    mock_print, chips: Chips
) -> None:
    """Tests that no_chips_remaining prints correct statement to user if chips.total is zero

    Args:
        mock_print (_type_): mock built in print function
        chips (Chips): A Chips object representing a player's betting chips
    """
    chips.total = 0
    chips.no_chips_remaining()
    mock_print.assert_called_once_with("You have no chips left! Game over.")


def test_no_chips_remaining_ends_game(chips: Chips) -> None:
    """Tests that no_chips_remaining sets game_on to False and ends the game if chips.total is zero

    Args:
        mock_print (_type_): mock built in print function
        chips (Chips): A Chips object representing a player's betting chips
    """
    chips.total = 0
    chips.no_chips_remaining()
    assert game_config.game_on is False
