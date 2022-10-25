"""Defines the class "Card" which represents a single card within a playing deck"""

from blackjack.constants import values


class Card:
    """A class representing a single card"""

    def __init__(self, rank: str, suit: str) -> None:
        """
        Args:
            rank (str): rank or name of the card
            suit (str): suit of the card (Heart, Diamond, Spade or Club)
        """
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self) -> str:
        """Returns a string describing the card as '<rank> of <suit>'

        Returns:
            str: description of the rank and suit of the card
        """
        return f"{self.rank} of {self.suit}"
