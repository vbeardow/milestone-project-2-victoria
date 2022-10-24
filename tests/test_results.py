from unittest.mock import patch
import pytest
from blackjack.results import *
from blackjack.hand import Hand
from blackjack.chips import *


@patch("builtins.print")
@patch("blackjack.chips.Chips.win_bet")
def test_player_win(mock_win_bet, mock_print, chips: Chips):
    """Test print and win_bet are called correctly if player wins

    Args:
        mock_win_bet (_type_): mock win_bet function
        mock_print (_type_): mock built in print function
        chips (Chips): Chips object representing the player's betting chips
    """
    player_win(chips)
    mock_print.assert_called_once_with("Player wins! Dealer loses.")
    mock_win_bet.assert_called_once()


@patch("builtins.print")
@patch("blackjack.chips.Chips.lose_bet")
def test_player_lose(mock_lose_bet, mock_print, chips: Chips):
    """Test print and lose_bet are called correctly if player loses

    Args:
        mock_lose_bet (_type_): mock lose_bet function
        mock_print (_type_): mock built in print function
        chips (Chips): Chips object representing the player's betting chips
    """
    player_lose(chips)
    mock_print.assert_called_once_with("Player loses! Dealer wins.")
    mock_lose_bet.assert_called_once()
