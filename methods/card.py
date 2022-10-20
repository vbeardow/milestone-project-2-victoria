suits = {'Hearts', 'Diamonds', 'Spades', 'Clubs'}
ranks = {'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'}
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

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
        return f'{self.rank} of {self.suit}'