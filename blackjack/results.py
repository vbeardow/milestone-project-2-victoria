def player_win(chips) -> None:
    """Print result if player wins and add chips to players chips

    Args:
        chips (Chips): Chips object representing the player's betting chips
    """
    chips.win_bet()
    print("Player wins! Dealer loses.")


def player_lose(chips) -> None:
    """Print result if player loses and remove chips from players chips

    Args:
        chips (Chips): Chips object representing the player's betting chips
    """
    chips.lose_bet()
    print("Player loses! Dealer wins.")
