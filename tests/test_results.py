"""Tests the results functions for the game blackjack"""


from unittest.mock import patch
import pytest
from blackjack.results import player_win, player_lose, player_bust, determine_winner
from blackjack.chips import Chips
from blackjack.hand import Hand


@pytest.fixture
def player_hand():
    return Hand()


@pytest.fixture
def dealer_hand():
    return Hand()


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


@patch("builtins.print")
@patch("blackjack.chips.Chips.lose_bet")
def test_player_bust(mock_lose_bet, mock_print, chips: Chips):
    """Test print and lose bet are called correctly if player is bust

    Args:
        mock_lose_bet (_type_): mock lose_bet function
        mock_print (_type_): mock built in print function
        chips (Chips): Chips object representing the player's betting chips
    """
    player_bust(chips)
    mock_print.assert_called_once_with("Player bust! Dealer wins.")
    mock_lose_bet.assert_called_once()


@patch("blackjack.results.player_win")
def test_determine_winner_dealer_bust(
    mock_player_win, player_hand: Hand, dealer_hand: Hand, chips: Chips
):
    """Tests that determine winner will call player_win if dealer hand is > 21

    Args:
        mock_player_win (_type_): mock player win function
        player_hand (Hand): Hand object representing the player's hand
        dealer_hand (Hand): Hand object representing the dealer's hand
        chips (Chips): _description_
    """
    dealer_hand.value = 22
    determine_winner(player_hand, dealer_hand, chips)
    mock_player_win.assert_called_once()


@patch("blackjack.results.player_win")
def test_determine_winner_player_wins(
    mock_player_win, player_hand: Hand, dealer_hand: Hand, chips: Chips
):
    """Test that determine winner will call player_win if the
    total value of the player's hand is more than the dealer's hand

    Args:
        mock_player_win (_type_): mock player win function
        player_hand (Hand): Hand object representing the player's hand
        dealer_hand (Hand): Hand object representing the dealer's hand
        chips (Chips): Chips object representing the player's betting chips
    """
    player_hand.value = 21
    dealer_hand.value = 18
    determine_winner(player_hand, dealer_hand, chips)
    mock_player_win.assert_called_once()


@patch("blackjack.results.player_lose")
def test_determine_winner_player_loses(
    mock_player_lose, player_hand: Hand, dealer_hand: Hand, chips: Chips
):
    """Test that determine winner will call player_lose if the
    total value of the player's hand is less than the dealer's hand

    Args:
        mock_player_win (_type_): mock player win function
        player_hand (Hand): Hand object representing the player's hand
        dealer_hand (Hand): Hand object representing the dealer's hand
        chips (Chips): Chips object representing the player's betting chips
    """
    player_hand.value = 18
    dealer_hand.value = 21
    determine_winner(player_hand, dealer_hand, chips)
    mock_player_lose.assert_called_once()


@patch("builtins.print")
@patch("blackjack.results.player_lose")
def test_determine_winner_draw_player_loses(
    mock_player_lose, mock_print, player_hand: Hand, dealer_hand: Hand, chips: Chips
):
    """Test that determine winner will call player_lose if the total value of the player's hand is equal to the dealer's hand

    Args:
        mock_print(_type_): mock built in print function
        mock_player_win (_type_): mock player win function
        player_hand (Hand): Hand object representing the player's hand
        dealer_hand (Hand): Hand object representing the dealer's hand
        chips (Chips): Chips object representing the player's betting chips
    """
    player_hand.value = 20
    dealer_hand.value = 20
    determine_winner(player_hand, dealer_hand, chips)
    mock_print.assert_called_once_with("Draw!")
    mock_player_lose.assert_called_once()
