"""Defines the methods which determine and act on the result of the game blackjack"""
from blackjack.chips import Chips
from blackjack.hand import Hand
import blackjack.game_config as game_config


def player_win(chips: Chips) -> None:
    """Print result if player wins and add chips to players chips

    Args:
        chips (Chips): Chips object representing the player's betting chips
    """
    chips.win_bet()
    print("Player wins! Dealer loses.")


def player_lose(chips: Chips) -> None:
    """Print result if player loses and remove chips from players chips

    Args:
        chips (Chips): Chips object representing the player's betting chips
    """
    chips.lose_bet()
    print("Player loses! Dealer wins.")


def player_bust(chips: Chips) -> None:
    """Print result if player goes bust and remove chips from players chips

    Args:
        chips (Chips): Chips object represernting the player's betting chips
    """
    chips.lose_bet()
    game_config.playing = False
    print("Player bust! Dealer wins.")


def determine_winner(player_hand: Hand, dealer_hand: Hand, chips: Chips) -> None:
    """Determine the winner of the game. The player wins if their hand is larger than the
    dealers or the dealer's hand is larger than 21 (bust)

    Args:
        player_hand (Hand): Hand object representing the player's hand
        dealer_hand (Hand): Hand object representing the dealer's hand
        chips (Chips): Chips object representing the player's betting chips
    """
    if dealer_hand.value > 21 or player_hand.value > dealer_hand.value:
        player_win(chips)
    elif player_hand.value < dealer_hand.value:
        player_lose(chips)
    elif player_hand.value == dealer_hand.value:
        print("Draw!")
        player_lose(chips)
