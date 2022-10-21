from blackjack.card import Card


class Hand:
    """Class representing a hand of cards"""

    def __init__(self) -> None:
        """Defines the attributes of cards, value and aces. Default is no cards in the hand."""
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card: Card) -> None:
        """Adds a single card to hand and adjusts the value and aces count of the hand

        Args:
            card (Card): A single card object
        """
        self.cards.append(card)
        self.value += card.value
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self) -> None:
        """Adjusts the value of a hand if it includes aces and the value is above 21"""
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
